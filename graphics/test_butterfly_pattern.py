from graphics.butterfly_pattern import butterfly_pattern


def test_butterfly_pattern():
    expected_output = (
        "*        *\n" "**      **\n" "***    ***\n" "**      **\n" "*        *"
    )
    assert butterfly_pattern(3) == expected_output
