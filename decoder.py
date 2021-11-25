from random import *

# encodes x.....x (n times) where asciiCode represents x


def encode(asciiCode, n):
    targetEncoding = 0
    for i in range(n):
        targetEncoding += (256 ** i) * asciiCode
    return targetEncoding

# encodes the value of a particular ascii code at particular position n


def encodeChar(asciiCode, n):
    return (256 ** n) * asciiCode

# translates ascii to readable form


def translateAscii(asciiChars):
    decodedPhrase = ""
    for code in asciiChars:
        decodedPhrase += str(chr(code))
    return decodedPhrase


def find(start, end, targetEncoding, guessLength, asciiChars):

    if (end > start and guessLength > 0):
        mid = (end-start) // 2 + start
        tempEncoding = encode(mid, guessLength)

        print("targetEncoding  : ", targetEncoding)
        print("tempEncoding    : ", tempEncoding)
        print("diff            : ", targetEncoding - tempEncoding)
        print("start: ", start)
        print("end  : ", end)
        print("mid  : ", mid)
        print("*******************************")

        if(tempEncoding - targetEncoding >= 0):
            return find(start, mid, targetEncoding, guessLength, asciiChars)

        if (targetEncoding - tempEncoding >= 0):
            asciiChars.append(mid)
            return mid, targetEncoding - encodeChar(mid, guessLength-1), guessLength-1, asciiChars
    else:
        return -1


def main():

    guessLength = 9
    start = 32
    end = 127
    targetEncoding = 1871078840601672443223
    asciiChars = []

    (x, y, z, t) = find(start, end, targetEncoding, guessLength, asciiChars)
    print("In main: ", x, y, z, t)

    print("Char: ", translateAscii(t))


if (__name__ == "__main__"):
    main()
