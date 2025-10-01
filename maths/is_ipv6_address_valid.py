"""
Validate IPv6 addresses (full and compressed forms).

References:
- Wikipedia: https://en.wikipedia.org/wiki/IPv6_address
- RFC 4291: https://tools.ietf.org/html/rfc4291

Rules implemented (subset of RFC 4291):
- Hex groups are 1-4 hex digits (0-9, a-f, A-F).
- Exactly 8 groups in total. A single '::' may compress one or more groups of
  zeros. No more than one '::' is allowed.
- No leading/trailing single ':' (e.g., ':1:2::' is invalid).
- Does NOT support IPv4-mapped endings like '::ffff:192.0.2.128'.

Examples (doctests):

>>> is_ipv6_address_valid("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
True
>>> is_ipv6_address_valid("2001:db8:85a3:0:0:8A2E:0370:7334")
True
>>> is_ipv6_address_valid("2001:db8:85a3::8A2E:0370:7334")  # '::' compresses two groups
True
>>> is_ipv6_address_valid("::1")  # loopback, 7 groups compressed
True
>>> is_ipv6_address_valid("2001:db8::")  # trailing compression is OK
True
>>> is_ipv6_address_valid("::")  # all groups compressed
True

Invalids:

>>> is_ipv6_address_valid("")  # empty
False
>>> is_ipv6_address_valid("2001:db8:85a3:::8a2e:370:7334")  # multiple '::'
False
>>> is_ipv6_address_valid("2001:db8:85a3:0:0:8a2e:370:7334:abcd")  # 9 groups
False
>>> is_ipv6_address_valid("2001:db8:85a3:0:0:8a2e:0370:g334")  # non-hex char
False
>>> is_ipv6_address_valid("2001:db8:85a3:0:0:8a2e:0370:")  # trailing ':'
False
>>> is_ipv6_address_valid(":2001:db8::1")  # leading ':'
False
>>> is_ipv6_address_valid("a::b:c:d:e:f:g:h")  # '::' compresses zero groups (already 8)
False
>>> is_ipv6_address_valid("1::1:1:1:1:1:1:1")  # same idea; zero groups compressed
False
"""

_HEX_DIGITS = set("0123456789abcdefABCDEF")


def _is_valid_group(group: str) -> bool:
    """Return True iff group is 1-4 hex digits."""
    return 1 <= len(group) <= 4 and all(ch in _HEX_DIGITS for ch in group)


def is_ipv6_address_valid(address: str) -> bool:
    """
    Return True iff `address` is a valid IPv6 address in full or compressed form.

    See module docstring for rules and doctests.
    """
    # Early validation checks combined
    if not address:
        return False

    if (address.startswith(":") and not address.startswith("::")) or (
        address.endswith(":") and not address.endswith("::")
    ):
        return False

    # Check for invalid triple-colon or more
    if ":::" in address:
        return False

    double_colon_count = address.count("::")
    if double_colon_count > 1:
        return False

    if double_colon_count == 0:
        # No compression: must be exactly 8 non-empty groups.
        parts: list[str] = address.split(":")
        return (
            len(parts) == 8
            and all(part != "" for part in parts)
            and all(_is_valid_group(part) for part in parts)
        )

    # With compression: split once on '::' into left and right sides.
    left, right = address.split("::", 1)

    left_groups = [g for g in left.split(":") if g != ""] if left else []
    right_groups = [g for g in right.split(":") if g != ""] if right else []

    # Validate: valid hex groups, proper count, and actual compression
    total_groups = len(left_groups) + len(right_groups)
    return (
        total_groups < 8  # '::' must compress at least one group
        and all(_is_valid_group(g) for g in left_groups + right_groups)
    )


if __name__ == "__main__":
    ip = input().strip()
    valid_or_invalid = "valid" if is_ipv6_address_valid(ip) else "invalid"
    print(f"{ip} is a {valid_or_invalid} IPv6 address.")
