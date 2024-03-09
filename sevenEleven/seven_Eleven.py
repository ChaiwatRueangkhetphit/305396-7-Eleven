"""The 7-Eleven module."""

def sevenEleven(number):
    """Seven-Eleven check."""
    if(number % 7 == 0 and number % 11 == 0):
        result = "7-eleven"
    elif(number % 7 == 0):
        result = "seven"
    elif(number % 11 == 0):
        result = "eleven"
    else:
        result = ""
    return result

