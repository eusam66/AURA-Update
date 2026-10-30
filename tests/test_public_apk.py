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
