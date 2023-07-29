"""
Implements an is valid email address algorithm

@ https://en.wikipedia.org/wiki/Email_address
"""


email_tests: tuple[tuple[str, bool], ...] = (
    ("simple@example.com", True),
    ("very.common@example.com", True),
    ("disposable.style.email.with+symbol@example.com", True),
    ("other-email-with-hyphen@and.subdomains.example.com", True),
    ("fully-qualified-domain@example.com", True),
    ("user.name+tag+sorting@example.com", True),
    ("x@example.com", True),
    ("example-indeed@strange-example.com", True),
    ("test/test@test.com", True),
    (
        "1234567890123456789012345678901234567890123456789012345678901234567890@example.com",
        True,
    ),
    ("admin@mailserver1", True),
    ("example@s.example", True),
    ("Abc.example.com", False),
    ("A@b@c@example.com", False),
    ("a(c)d,e:f;g<h>i[j\\k]l@example.com", False),
    (
        "12345678901234567890123456789012345678901234567890123456789012345678901@example.com",
        False,
    ),
    ("i.like.underscores@but_its_not_allowed_in_this_part", False),
)

# The maximum octets (one character as a standard unicode character is one byte)
# that the local part and the domain part can have
MAX_LOCAL_PART_OCTETS = 64
MAX_DOMAIN_OCTETS = 255


def is_valid_email_address(email: str) -> bool:
    """
    Returns True if the passed email address is valid.

    The local part of the email precedes the singular @ symbol and
    is associated with a display-name. For example, "john.smith"
    The domain is stricter than the local part and follows the @ symbol.

    >>> for email, valid in email_tests:
    ...     assert is_valid_email_address(email) is valid
    """

    # Make sure that there is only one @ symbol in the email address
    if email.count("@") != 1:
        return False

    local_part, domain = email.split("@")
    # Check octet length of the local part and domain
    if len(local_part) > MAX_LOCAL_PART_OCTETS or len(domain) > MAX_DOMAIN_OCTETS:
        return False

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    for email, _ in email_tests:
        is_valid = is_valid_email_address(email)
        print(f"Email address {email} is {'not' if is_valid is False else ''} valid")
