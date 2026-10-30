#!/usr/bin/env python3
"""Reject debuggable/test-only APK flags using actual aapt evidence. No private source or key."""
import re
import base64
import hashlib
from validate_manifest import EXPECTED_CERT
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

def certificate_sha256(output, expected=EXPECTED_CERT):
    """Hash verified signer's standard PEM DER; never depend on SDK-specific labels."""
    if not re.search(r'^Number of signers: 1\s*$', output, re.MULTILINE):
        raise ValueError('Expected exactly one verified signer')
    begin, end = '-----BEGIN CERTIFICATE-----', '-----END CERTIFICATE-----'
    if output.count(begin) != 1 or output.count(end) != 1:
        raise ValueError('Expected exactly one complete signing certificate')
    payload = output.split(begin, 1)[1].split(end, 1)[0]
    try:
        der = base64.b64decode(''.join(payload.split()), validate=True)
    except (ValueError, base64.binascii.Error) as exc:
        raise ValueError('Invalid certificate encoding') from exc
    digest = hashlib.sha256(der).hexdigest()
    if not der or digest != expected:
        raise ValueError('Original signing certificate mismatch')
    return digest

if __name__ == '__main__':
    verify(Path(sys.argv[1]).read_text(), Path(sys.argv[2]).read_text())
    print('Public distribution gate passed: non-debuggable, non-test-only, minSdk28')
    if len(sys.argv) > 3:
        digest = certificate_sha256(Path(sys.argv[3]).read_text())
        print('Original certificate verified (public SHA-256): ' + digest)
