#!/usr/bin/env python3
"""Reject debuggable/test-only APK flags using actual aapt evidence. No private source or key."""
import re
import sys
from pathlib import Path

def verify(badging, manifest):
    if 'application-debuggable' in badging:
        raise ValueError('Public APK must not be debuggable')
    for field in ('debuggable', 'testOnly'):
        for line in manifest.splitlines():
            if re.search(r'\bandroid:' + field + r'\b', line):
                value = line.split('=', 1)[-1].strip()
                if value not in ('(type 0x12)0x0', 'false', '0x0'):
                    raise ValueError('Unsafe or ambiguous manifest flag: ' + field)
    if not re.search(r"sdkVersion:'28'", badging):
        raise ValueError('Unexpected minimum Android version')

if __name__ == '__main__':
    verify(Path(sys.argv[1]).read_text(), Path(sys.argv[2]).read_text())
    print('Public distribution gate passed: non-debuggable, non-test-only, minSdk28')
