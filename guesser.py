from random import *


def guessAscii(targetEncodedVal, guessLength):

    encodedGuess = 0
    while (encodedGuess != targetEncodedVal):
        encodedGuess = 0
        asciiChars = []
        for i in range(guessLength):
            guessAscii = randint(32, 127)
            encodedGuess += (256 ** i) * guessAscii
            asciiChars.append(guessAscii)

        print(asciiChars)

    if (targetEncodedVal == encodedGuess):
        return asciiChars


def translateAscii(asciiChars):
    decodedPhrase = ""
    for code in asciiChars:
        decodedPhrase += str(chr(code))
    return decodedPhrase


def main():
    targetEncodedVal = int(input("Input the encoded value to be decoded: "))
    guessLength = int(input("Guess the length of decoded pharase: "))

    print("Correct plain text found: ", translateAscii(
        guessAscii(targetEncodedVal, guessLength)))


if (__name__ == "__main__"):
    main()
