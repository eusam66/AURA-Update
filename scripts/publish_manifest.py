#!/usr/bin/env python3
"""Produce a new release feed only after the exact signed APK is verified."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from validate_manifest import EXPECTED_CERT, EXPECTED_PACKAGE, validate

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--channel", choices=("stable", "lite"), required=True)
    p.add_argument("--version-code", type=int, required=True)
    p.add_argument("--version-name", required=True)
    p.add_argument("--sha256", required=True)
    p.add_argument("--size", type=int, required=True)
    p.add_argument("--notes", required=True)
    args = p.parse_args()
    path = Path(f"updates/android/{args.channel}.json")
    old = json.loads(path.read_text("utf-8"))
    validate(old, args.channel)
    if old["latest"] is not None and args.version_code <= old["latest"]["version_code"]:
        p.error("new versionCode must exceed existing channel version")
    tag = f"android-{args.channel}-vc{args.version_code}"
    asset = f"AURA-Glass-TV-{args.channel}-vc{args.version_code}.apk"
    payload = {
        "schema_version": 1, "platform": "android-tv", "channel": args.channel, "status": "released",
        "latest": {
            "version_code": args.version_code,
            "version_name": args.version_name,
            "package_name": EXPECTED_PACKAGE,
            "min_sdk": 28,
            "apk_url": f"https://github.com/eusam66/AURA-Update/releases/download/{tag}/{asset}",
            "apk_sha256": args.sha256.lower(),
            "apk_size_bytes": args.size,
            "signing_cert_sha256": EXPECTED_CERT,
            "notes": args.notes,
            "published_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        }
    }
    validate(payload, args.channel)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Prepared validated update feed: {path}")

if __name__ == "__main__":
    main()
