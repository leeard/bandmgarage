#!/usr/bin/env python3
"""Parse partner deal URLs + coupon codes from a YouTube description.

Reads JSON on stdin: { "description": "..." }
Writes JSON array on stdout: [{host,url,name,code,deal}, ...]
"""
from __future__ import annotations

import json
import re
import sys

SKIP_HOST = re.compile(
    r"(youtube\.com|youtu\.be|instagram\.com|tiktok\.com|facebook\.com|"
    r"twitter\.com|\bx\.com\b|bandmsgarage)",
    re.I,
)
SKIP_URL = re.compile(r"amazon\.com/shop/", re.I)
URL_RE = re.compile(r"https?://[^\s)\"<>]+")
CODE_RE = re.compile(
    r"(?i)\b(?:discount\s*code|promo\s*code|coupon(?:\s*code)?|"
    r"(?:using\s+)?(?:this\s+)?code|code)\s*"
    r"(?:for\s+\$?\d+\s*%?\s*off)?\s*[:=\-–]?\s*"
    r"([A-Za-z0-9][A-Za-z0-9&%_.-]{1,24})"
)
DEAL_RE = re.compile(r"(?i)(\$\d+\s*off|\d+\s*%\s*off)")
BRAND_HINT = re.compile(
    r"^(?![#])(?!.*\b(?:code|discount|using|link|off|http)\b)"
    r"[A-Za-z][A-Za-z0-9 &/'+\-]{0,40}$",
    re.I,
)
PRODUCT_HOSTS = {"amazon.com", "a.co", "amzn.to", "geni.us"}


def host_of(url: str) -> str:
    u = re.sub(r"^https?://(www\.)?", "", url, flags=re.I)
    return u.split("/")[0].lower()


def clean_url(u: str) -> str:
    return re.sub(r"[\.,;]+$", "", u)


def normalize_deal(text: str) -> str:
    d = re.sub(r"\s+", " ", text.strip())
    d = re.sub(r"(?i)(\$\d+)\s*off", r"\1 OFF", d)
    d = re.sub(r"(?i)(\d+)\s*%\s*off", r"\1% OFF", d)
    return d


def extract_code(line: str) -> str | None:
    m = CODE_RE.search(line)
    if not m:
        return None
    code = m.group(1).rstrip(".,;")
    if code.lower() in {"code", "for", "off", "the", "this", "using", "link"}:
        return None
    return code


def extract_deal(line: str) -> str | None:
    m = DEAL_RE.search(line)
    return normalize_deal(m.group(1)) if m else None


def parse_description(desc: str) -> list[dict]:
    current: dict = {"name": None, "code": None, "deal": None}
    # After emitting a partner URL, trailing code/deal lines attach to it until
    # the next brand header (avoids Mushroom Bloom's code landing on Mowrator).
    attach_to_last = False
    seen: dict[str, dict] = {}
    order: list[str] = []

    def update_last(**kwargs):
        if not order or not attach_to_last:
            return
        h = order[-1]
        for k, v in kwargs.items():
            if not v:
                continue
            # Prefer later code/deal on the same partner block
            # (e.g. "5% OFF" link line then "10% Off discount code: bmgarage")
            seen[h][k] = v

    for raw in (desc or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        urls = [clean_url(u) for u in URL_RE.findall(line)]
        code = extract_code(line)
        deal = extract_deal(line)

        if code:
            current["code"] = code
        if deal:
            current["deal"] = deal

        if urls:
            for u in urls:
                if SKIP_HOST.search(u) or SKIP_URL.search(u):
                    continue
                h = host_of(u)
                if h in PRODUCT_HOSTS:
                    continue
                if h in seen:
                    continue
                https = u if u.startswith("https") else u.replace("http://", "https://", 1)
                seen[h] = {
                    "host": h,
                    "url": https,
                    "name": current["name"],
                    "code": current["code"],
                    "deal": current["deal"],
                }
                order.append(h)
                attach_to_last = True
            continue

        # Brand header starts a new block — stop attaching to previous partner
        if BRAND_HINT.match(line) and len(line) <= 42:
            current = {"name": line.strip(), "code": None, "deal": None}
            attach_to_last = False
            continue

        # Code/deal-only lines after a URL → same partner block
        if code or deal:
            update_last(code=code, deal=deal)

    return [seen[h] for h in order]


def main() -> None:
    raw = sys.stdin.read()
    if not raw.strip():
        print("[]")
        return
    try:
        payload = json.loads(raw)
        desc = payload.get("description", "") if isinstance(payload, dict) else str(payload)
    except json.JSONDecodeError:
        desc = raw
    print(json.dumps(parse_description(desc), ensure_ascii=False))


if __name__ == "__main__":
    main()
