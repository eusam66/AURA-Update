#!/usr/bin/env python3
"""Offline manifest validation. Python stdlib only."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

EXPECTED_CERT = "f5e7ba845b611c41d3b8354a04c461609b47b9eacfa59f25b16bafcfb144e3b9"
EXPECTED_PACKAGE = "com.auratv.player.engine3"
PUBLIC_RELEASE_PREFIX = "https://github.com/eusam66/AURA-Update/releases/download/"
CHANNELS = ("stable", "lite")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
LATEST_KEYS = {"version_code", "version_name", "package_name", "min_sdk",
               "apk_url", "apk_sha256", "apk_size_bytes", "signing_cert_sha256",
               "notes", "published_at"}

def validate(data, channel):
    if channel not in CHANNELS:
        raise ValueError("invalid channel")
    if set(data) != {"schema_version", "platform", "channel", "status", "latest"}:
        raise ValueError("unexpected manifest top-level keys")
    if data["schema_version"] != 1 or data["platform"] != "android-tv" or data["channel"] != channel:
        raise ValueError("incorrect schema/platform/channel")
    if data["status"] == "unreleased":
        if data["latest"] is not None:
            raise ValueError("unreleased feed must not offer a version")
        return
    if data["status"] != "released":
        raise ValueError("unknown release status")
    latest = data["latest"]
    if not isinstance(latest, dict) or set(latest) != LATEST_KEYS:
        raise ValueError("unexpected release fields")
    if type(latest["version_code"]) is not int or latest["version_code"] <= 0:
        raise ValueError("invalid versionCode")
    if not isinstance(latest["version_name"], str) or not re.fullmatch(r"[A-Za-z0-9._+-]{1,80}", latest["version_name"]):
        raise ValueError("invalid versionName")
    if latest["package_name"] != EXPECTED_PACKAGE:
        raise ValueError("wrong Android package")
    if type(latest["min_sdk"]) is not int or latest["min_sdk"] < 28:
        raise ValueError("unsupported minSdk")
    if type(latest["apk_size_bytes"]) is not int or latest["apk_size_bytes"] <= 0:
        raise ValueError("invalid APK size")
    if latest["signing_cert_sha256"] != EXPECTED_CERT:
        raise ValueError("unexpected signing certificate")
    if not isinstance(latest["apk_sha256"], str) or not HEX64.fullmatch(latest["apk_sha256"]):
        raise ValueError("invalid APK sha256")
    url = latest["apk_url"]
    if not isinstance(url, str) or not url.startswith(PUBLIC_RELEASE_PREFIX):
        raise ValueError("APK must live in this public GitHub Releases repository")
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.netloc != "github.com" or parsed.query or parsed.fragment or parsed.username or parsed.password:
        raise ValueError("malformed GitHub release URL")
    suffix = url[len(PUBLIC_RELEASE_PREFIX):].split("/")
    if len(suffix) != 2 or not re.fullmatch(r"android-(stable|lite)-vc\d+", suffix[0]) or not suffix[0].startswith(f"android-{channel}-"):
        raise ValueError("wrong release tag")
    if suffix[1] != f"AURA-Glass-TV-{channel}-vc{latest['version_code']}.apk":
        raise ValueError("unexpected APK filename/version")
    if not isinstance(latest["notes"], str) or len(latest["notes"]) > 2000:
        raise ValueError("invalid release notes")
    if not isinstance(latest["published_at"], str) or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", latest["published_at"]):
        raise ValueError("invalid UTC timestamp")

def load_and_validate(path):
    path = Path(path)
    channel = path.stem
    with path.open("r", encoding="utf-8") as f:
        payload = json.load(f)
    validate(payload, channel)
    return payload

if __name__ == "__main__":
    paths = sys.argv[1:] or [f"updates/android/{channel}.json" for channel in CHANNELS]
    for path in paths:
        load_and_validate(path)
        print(f"VALID: {path}")
