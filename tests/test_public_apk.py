import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from verify_public_apk import verify

class ApkGateTests(unittest.TestCase):
    def test_safe_absent_flags(self):
        verify("sdkVersion:'28'", 'E: manifest\n E: application')
    def test_safe_explicit_false(self):
        verify("sdkVersion:'28'", 'A: android:debuggable(0x0101000f)=(type 0x12)0x0\nA: android:testOnly(0x01010272)=(type 0x12)0x0')
    def test_reject_flags_or_ambiguous_values(self):
        for flag in ['debuggable', 'testOnly']:
            for value in ['(type 0x12)0xffffffff', 'true', '(type 0x12)0x1', '@bool/unknown']:
                with self.subTest(flag=flag,value=value), self.assertRaises(ValueError):
                    verify("sdkVersion:'28'", f'A: android:{flag}(0x01)={value}')
    def test_badging_and_sdk(self):
        for text in ["application-debuggable\nsdkVersion:'28'", "sdkVersion:'27'", '']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                verify(text, '')

class SigningCertificateGateTests(unittest.TestCase):
    def fixture(self, label='Signer #1', data=b'synthetic certificate parser fixture', signers=1):
        import base64
        return (f'Number of signers: {signers}\n{label} certificate PEM:\n'
                '-----BEGIN CERTIFICATE-----\n' + base64.b64encode(data).decode() +
                '\n-----END CERTIFICATE-----\n')

    def test_sdk35_and_sdk37_labels_do_not_change_certificate_digest(self):
        import hashlib
        from verify_public_apk import certificate_sha256
        wanted = hashlib.sha256(b'synthetic certificate parser fixture').hexdigest()
        for label in ['Signer #1', 'V2 Signer:', 'V3 Signer:']:
            self.assertEqual(wanted, certificate_sha256(self.fixture(label), expected=wanted))

    def test_default_pin_rejects_other_certificate_and_tampering(self):
        import hashlib
        from verify_public_apk import certificate_sha256
        with self.assertRaises(ValueError):
            certificate_sha256(self.fixture())
        wanted = hashlib.sha256(b'synthetic certificate parser fixture').hexdigest()
        with self.assertRaises(ValueError):
            certificate_sha256(self.fixture(data=b'tampered'), expected=wanted)

    def test_missing_multiple_or_truncated_signers_are_rejected(self):
        import hashlib
        from verify_public_apk import certificate_sha256
        wanted = hashlib.sha256(b'synthetic certificate parser fixture').hexdigest()
        for text in ['', self.fixture(signers=2), self.fixture() + self.fixture(),
                     self.fixture().replace('-----END CERTIFICATE-----', '')]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                certificate_sha256(text, expected=wanted)

    def test_invalid_base64_and_empty_certificate_are_rejected(self):
        from verify_public_apk import certificate_sha256
        for text in ['Number of signers: 1\n-----BEGIN CERTIFICATE-----\n!\n-----END CERTIFICATE-----',
                     'Number of signers: 1\n-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                certificate_sha256(text)
