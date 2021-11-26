def encodeChar(asciiCode, n):  # encodes the value of a particular ascii code at position n
    return (256 ** n) * asciiCode


# encodes .....x (n chars) where asciiCode represents x and all chars before are " "
def encodePhrase(asciiCode, n):
    targetEncoding = 0
    for i in range(n-1):
        targetEncoding += (256 ** i) * (ord(" "))
    targetEncoding += (256 ** (n-1)) * (asciiCode)
    return targetEncoding
