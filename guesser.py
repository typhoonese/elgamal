from random import *
import utils.plainText


def guess(targetEncodedVal, guessLength):

    encodedGuess = 0
    while (encodedGuess != targetEncodedVal):
        encodedGuess = 0
        asciiChars = []
        for i in range(guessLength):
            guessAscii = randint(ord(" "), ord("~"))
            encodedGuess += (256 ** i) * guessAscii
            asciiChars.append(guessAscii)

        print(asciiChars)

    if (targetEncodedVal == encodedGuess):
        return asciiChars


def main():
    targetEncodedVal = int(input("Input the encoded value to be decoded: "))
    guessLength = utils.plainText.guessLength(targetEncodedVal)
    print("Correct plain text found: ", utils.plainText.translateFromAscii(
        guess(targetEncodedVal, guessLength)))


if (__name__ == "__main__"):
    main()
