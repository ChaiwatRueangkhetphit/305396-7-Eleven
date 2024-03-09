"""Test case for 7-Eleven Kata"""

import pytest

from sevenEleven.seven_Eleven import sevenEleven

    
@pytest.mark.parametrize(
    "number, expected",
    [
        (1, ""),
        (5, ""),
        (7, "seven"),
        (9, ""),
        (11, "eleven"),
        (12, ""),
        (14, "seven"),
        (16, ""),
        (21, "seven"),
        (22, "eleven"),
        (77, "7-eleven"),
        (88, "eleven"),
        (84, "seven"),
        (91, "seven"),
        (154, "7-eleven"),
    ]
)
def test_seven_Eleven(number, expected):
    """Seven-Eleven check."""
    # Arrage
    
    # Act
    result = sevenEleven(number)
    
    # Assert
    assert result == expected