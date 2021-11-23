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

Implemented the encoding algorithm in `checkEncoding.py`, which encodes a given $plainText$  and compares it to $M$ . If matched, $X = plainText$ . 





