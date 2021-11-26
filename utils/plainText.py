import utils.encode


def translateFromAscii(asciiCodes):  # translates ascii codes (arr) to readable form
    decodedPhrase = ""
    for code in asciiCodes:
        decodedPhrase += str(chr(code))
    return decodedPhrase


def guessLength(targetEncoding):  # guesses the length of the decoded phrase
    i = 0
    guessEncoding = 0
    while (targetEncoding >= guessEncoding):
        i += 1
        guessEncoding = utils.encode.encodePhrase(ord(" "), i)
    return i-1
