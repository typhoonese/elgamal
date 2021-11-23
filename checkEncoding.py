#checkEncoding checks whether plainText can be encoded into the targetEncodedVal
#when encoded with the encoding algorithm
def checkEncoding (plainText, targetEncodedVal):
  #encodedPlainText: to store the value of encoded plainText
  encodedPlainText = 0
  #number: index to loop through plainText
  number = 0
  
  #Encode the plain text 
  while number < len(plainText) :
  #Convert each index of plainText to ASCII and encode with respect to the algorithm provided
   encodedPlainText  += (256 ** number) * ord(plainText[number])
   number += 1 

  print ("Encoded Plain Text   : ", targetEncodedVal)
  print ("Target Encoded Value : ", encodedPlainText)
  print ("Target Encoded Value - Encoded Plain Text: ", targetEncodedVal - encodedPlainText)

  if (encodedPlainText == targetEncodedVal):
   return plainText

#Enter plain text here
plainText = "Well done!"
#Enter the encoded phrase here
targetEncodedVal = 157709172775299964495191
#Check if plainText encodes to the targetEncodedVal. Returns the value of plain text if successful. Returns none otherwise
print("Correct plain text found: ", checkEncoding (plainText, targetEncodedVal))