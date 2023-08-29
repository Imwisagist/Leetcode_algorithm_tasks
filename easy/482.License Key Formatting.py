# https://leetcode.com/problems/license-key-formatting/

def licenseKeyFormatting(s: str, k: int) -> str:
    s, result = s.upper().replace("-", "")[::-1], ""

    for i in range(0, len(s), k):
        result += s[i:i+k] + "-"

    return result[::-1][1:]


assert licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"
assert licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J"
