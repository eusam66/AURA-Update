import json
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_manifest import load_and_validate, validate, EXPECTED_CERT, EXPECTED_PACKAGE

class ManifestTests(unittest.TestCase):
    def test_feeds_stay_disabled_until_release(self):
        for channel in ("stable", "lite"):
            p = load_and_validate(f"updates/android/{channel}.json")
            self.assertEqual(p["status"], "unreleased")
            self.assertIsNone(p["latest"])

    def test_rejects_fake_active_without_valid_payload(self):
        data = {"schema_version": 1, "platform": "android-tv", "channel": "stable",
                "status": "released", "latest": None}
        with self.assertRaises(ValueError):
            validate(data, "stable")

    def test_valid_published_and_bad_host(self):
        data = {"schema_version": 1, "platform": "android-tv", "channel": "stable",
                "status": "released", "latest": {
                    "version_code": 27, "version_name": "0.9.5-aura-premium",
                    "package_name": EXPECTED_PACKAGE, "min_sdk": 28,
                    "apk_url": "https://github.com/eusam66/AURA-Update/releases/download/android-stable-vc27/AURA-Glass-TV-stable-vc27.apk",
                    "apk_sha256": "a" * 64, "apk_size_bytes": 42_000_000,
                    "signing_cert_sha256": EXPECTED_CERT, "notes": "Test",
                    "published_at": "2026-10-29T18:00:00Z"
                }}
        validate(data, "stable")
        data["latest"]["apk_url"] = "https://example.com/fake.apk"
        with self.assertRaises(ValueError):
            validate(data, "stable")

if __name__ == "__main__":
    unittest.main()
