ERRORMSG = "Invalid use of 'formatNum()'. Refer to '>>> help(formatNum)' if unsure how to use this function."

ABBREVIATIONS = {
    1: "K",
    2: "M",
    3: "B",
    4: "T"
}

def formatNum(number, method, amount=0):

    """
    Arguments:
    ----------

    number: The number to be formatted
            Accepted types: Integer (int), Floating point value (float)

    method: One of the following:
                'lz':   leading zero's
                        Add the specified amount of leading zero's to the beginning of the number.

                        'amount' needed
                        returns a string (str)

                'r':    round 
                        Round the number to the specified place after the comma.

                        'amount' needed
                        returns a floating point number (float)

                'abb':  abbreviate
                        Abbreviate and round a big number to make it more easily readable. 
                        Also adds apostrophe's between thousands.

                        'amount' not needed
                        returns a string (str)

            Accepted type: String (str)
    
    amount: The amount passed to the method if needed
            Accepted type: Integer (int)

    

    Examples:

    >>> formatNum(6, "lz", 2)
    '006'
    
    >>> formatNum(4.3528, "r", 3)
    4.353

    >>> formatNum(143_589, "abb")
    '144K'

    >>> formatNum(1_768_231_493_234_8520, "abb")
    "17'682T"
    """

    try:
        assert type(number) is int or float
        assert type(method) is str
        assert type(amount) is int

    except AssertionError:
        raise SyntaxError(ERRORMSG) from None # disables Exception chaining
    
    if method == "lz":
        return ("0" * amount) + str(number)

    elif method == "r":
        return round(number, amount)

    elif method == "abb":
        i = 0
        while number >= 1000 and i < 4:
            number = round(number / 1000)
            i += 1
        
        abbreviation = ABBREVIATIONS[i]
        
        number = str(number)
        segments = []

        while len(number) > 3:
            cutoff = number[-3:-1] + number[-1]
            segments.append(cutoff)
            number = number.replace(cutoff, "")

        segments.append(number)
        segments.reverse()
        return "'".join(segments) + abbreviation

if __name__ == "__main__":
    import doctest
    doctest.testmod()   