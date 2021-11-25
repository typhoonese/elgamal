from random import *


def encode(asciiCode, n):
    encodedVal = 0
    for i in range(n):
        encodedVal += (256 ** i) * asciiCode
    return encodedVal


def translateAscii(asciiChars):
    decodedPhrase = ""
    for code in asciiChars:
        decodedPhrase += str(chr(code))
    return decodedPhrase


def find(start, end, encodedVal):

    if (end > start):
        mid = (end-start) // 2 + start
        computedEn = encode(mid, 10)

        if(computedEn - encodedVal >= 0):
            return find(start, mid, encodedVal)

        if (encodedVal - computedEn >= 0):
            return mid, encodedVal - computedEn
    else:
        return -1


def main():

    print("In main: ", find(32, 127, 157709172775299964495191))


if (__name__ == "__main__"):
    main()
