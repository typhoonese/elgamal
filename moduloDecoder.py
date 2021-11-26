# decodes ascii codes, encodedVal = encoded ascii code, asciiCodes = arr of chars decoded
def moduloDecoder(encodedVal, decodedPhrase):
    while (encodedVal > 0):
        decodedPhrase += str(chr(encodedVal % 256))
        encodedVal = encodedVal // 256
        moduloDecoder(encodedVal, decodedPhrase)
    return decodedPhrase


def main():
    # encodedVal = 157709172775299964495191
    targetEncodedVal = int(input("Input the encoded value to be decoded: "))
    decodedPhrase = ""
    print("Decoded phrase: ", (moduloDecoder(targetEncodedVal, decodedPhrase)))


if (__name__ == "__main__"):
    main()
