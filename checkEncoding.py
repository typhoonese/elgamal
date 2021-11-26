# checkEncoding checks whether plainText can be encoded into the targetEncoding
# when encoded with the encoding algorithm
def checkEncoding(plainText, targetEncoding):
    # encodedPlainText: to store the value of encoded plainText
    encodedPlainText = 0
    # number: index to loop through plainText
    number = 0

    # Encode the plain text
    while number < len(plainText):
        # Convert each index of plainText to ASCII and encode with respect to the algorithm provided
        encodedPlainText += (256 ** number) * ord(plainText[number])
        number += 1

    # print("Encoded Plain Text   : ", targetEncoding)
    # print("Target Encoded Value : ", encodedPlainText)
    # print("Target Encoded Value - Encoded Plain Text: ",
    #       targetEncoding - encodedPlainText)

    if (encodedPlainText == targetEncoding):
        return plainText


# Enter plain text here
plainText = input("Input plain text: ")
# encoded value - 157709172775299964495191
targetEncoding = int(input("Input the encoded value to be decoded: "))

# Check if plainText encodes to the targetEncoding. Returns the value of plain text if successful. Returns none otherwise
print("Correct plain text found: ", checkEncoding(plainText, targetEncoding))
