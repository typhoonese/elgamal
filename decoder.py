from random import *


def encode(asciiCode, n):  # encodes x.....x (n times) where asciiCode represents x
    targetEncoding = 0
    for i in range(n):
        targetEncoding += (256 ** i) * asciiCode
    return targetEncoding


def encodeChar(asciiCode, n):  # encodes the value of a particular ascii code at particular position n
    return (256 ** n) * asciiCode


def translateAscii(asciiCodes):  # translates ascii codes to readable form
    decodedPhrase = ""
    for code in asciiCodes:
        decodedPhrase += str(chr(code))
    return decodedPhrase


# returns true if target encoding is bigger than temp encoding
def isDiffBigger(asciiCode, guessLength, targetEncoding):
    tempEncoding = encode(asciiCode, guessLength)
    if (targetEncoding - tempEncoding >= 0):
        return 1
    else:
        return 0


# finds the ascii code that minimises the encoding difference start : min ascii code, end: max ascii code, guessLength: length of encoded phrase
def find(start, end, targetEncoding, guessLength, asciiChars):

    if (end >= start and guessLength > 0):
        mid = (end+start) // 2
        tempEncoding = encode(mid, guessLength)

        print("targetEncoding  : ", targetEncoding)
        print("tempEncoding    : ", tempEncoding)
        print("diff            : ", targetEncoding - tempEncoding)
        print("start: ", start)
        print("end  : ", end)
        print("mid  : ", mid)
        print("*******************************")

        # diff needs to get smaller
        if(not isDiffBigger(mid, guessLength, targetEncoding)):
            return find(start, mid-1, targetEncoding, guessLength, asciiChars)

        # should find the first ascii char that makes targetEncoding-tempEncoding positive
        if (isDiffBigger(mid, guessLength, targetEncoding)):
            # need to check if mid is the first positive diff
            if(isDiffBigger(mid+1, guessLength, targetEncoding)):
                # diff needs to get bigger
                return find(mid+1, end, targetEncoding, guessLength, asciiChars)
            else:
                asciiChars.append(mid)
                return mid, targetEncoding - encodeChar(mid, guessLength-1), guessLength-1, asciiChars
    else:
        return -1


def main():

    start = 32  # ascii code
    end = 127  # ascii code
    # targetEncoding = 391565397484887
    # guessLength = 6  # number of letters encoded
    targetEncoding = 157709172775299964495191
    guessLength = 10
    asciiChars = []  # store the decoded asci codes

    print("In main: ", find(start, end, targetEncoding,
          guessLength, asciiChars))


if (__name__ == "__main__"):
    main()
