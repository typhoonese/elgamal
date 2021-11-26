# El Gamal Decryption Challenge

Here's a summary of the approach I took. 

### Step 1: Codify how El Gamal works 

Studied some lectures on how El Gamal encryption works and went through some examples. I codified one of the approaches in `elgamal.cpp`. This became somewhat a playground. 

### Step 2: Find the solution

Having studied more lectures and examples, I concluded the following solution steps and used an online calculator to find $M$ .

1. Let $t = c_1^x \mod p$

2. Calculate $t^{-1}$ , where $t * t^{-1} \equiv 1 \mod p$

3. $M = c_2 * t^{-1}$ 

4. $M = 157709172775299964495191$ 

### Step 3: Check encoding

Implemented the provided encoding algorithm to `checkEncoding.py`, which encodes a given $plainText$ accordingly and compares it to $M$ . If matched, $X = plainText$ . 

### decoder.py
- `decoder.py` implements a recursive binary search of an ascii code, `n`, to decode the encoded value. The search criteria is based on minimising the difference between the encoded value and a temp encoding, where the temp encoding encodes `.....n` with the provided `encode ` function. All letters before `n` is assumed to be white space (ascii code `32`) for encoding. 

### moduloDecoder.py 
- `moduloDecoder.py` implements an algorithm that decodes a message stored in ascii codes with 256 base

### guesser.py 
- `guesser.py` implements an algorithm that generates a random assortment of ascii characters from 32 to 126 of a given length and comprase its encoding to the target encoded value. If the encoding of the randomly generated string matches the target encoded value, the algorithm finds the correct phrase and translate the ascii codes to a readable form. 





