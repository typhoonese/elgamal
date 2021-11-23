#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
namespace mp = boost::multiprecision;

int modInverse(mp::cpp_int a, mp::cpp_int m)
{
    mp::cpp_int m0 = m;
    mp::cpp_int y = 0, x = 1;

    if (m == 1)
        return 0;

    while (a > 1)
    {
        // q is quotient
        mp::cpp_int q = a / m;
        mp::cpp_int t = m;

        // m is remainder now, process same as
        // Euclid's algo
        m = a % m, a = t;
        t = y;

        // Update y and x
        y = x - q * y;
        x = t;
    }

    // Make x positive
    if (x < 0)
        x += m0;

    return int(x);
}

int main()
{
    int plainMessage = 35; //plain text
    int publicBase = 5;    //public base known to all
    int N = 89;            // modulo
    int prvKey_BOB = 8;    // number Bob chooses
    int prvKey_ALICE = 13; // number Alice chooses

    //Bob to send Alice the encrypted message

    //ALice can create a public key to share with Bob
    //Alice gives Bob her pubKey_ALICE, public base and N
    mp::cpp_int pubKey_ALICE = mp::pow(mp::cpp_int(publicBase), prvKey_ALICE) % N;

    //Bob can create a public key with what Alice provided
    //it's also referred as the ephemeral key
    mp::cpp_int pubKey_BOB = mp::pow(mp::cpp_int(publicBase), prvKey_BOB) % N;

    //Bob creates encryption key from what Alice sent him, the pubKey_ALICE
    //it's also referred as the masking key/session key
    mp::cpp_int encryptionKey = mp::pow(mp::cpp_int(pubKey_ALICE), prvKey_BOB) % N;

    //Bob encrypts the msg and sends it to Alice along with the ephemeral key (pubKey_BOB)
    //This is where El Gamal differs from Diffi-Helman:
    // Encrpted message and the ephemeral key are shared with ALice at the same time.
    mp::cpp_int encryptedMsg = (encryptionKey * plainMessage) % N;

    //Alice now has the encrypted message and Bob's public key
    //ALice first needs to figure out the encryption key Bob used
    mp::cpp_int aliceFindsOutKey = mp::pow(mp::cpp_int(pubKey_BOB), prvKey_ALICE) % N;

    //Alice then needs to calculate the inverse the key
    mp::cpp_int aliceInversesKey = modInverse(aliceFindsOutKey, mp::cpp_int(N));

    //Alice can decrypt the message
    mp::cpp_int aliceDecryptsMsg = (encryptedMsg * aliceInversesKey) % N;

    cout << "pubKey_BOB" << endl
         << pubKey_BOB << endl
         << "pubKey_ALICE" << endl
         << pubKey_ALICE << endl
         << "encryptionKey" << endl
         << encryptionKey << endl
         << "encryptedMsg" << endl
         << encryptedMsg << endl
         << "aliceFindsOutKey" << endl
         << aliceFindsOutKey << endl
         << "aliceInversesKey" << endl
         << aliceInversesKey << endl
         << "aliceDecryptsMsg" << endl
         << aliceDecryptsMsg << endl
         << "encryption is decrypted: " << endl
         << (plainMessage ==
             aliceDecryptsMsg)
         << endl;

    //alternative decryption without inversing the masking key from Bob
    mp::cpp_int alternativeDecryptionOutput = (mp::pow(mp::cpp_int(pubKey_BOB), int(N - 1 - mp::cpp_int(prvKey_ALICE)))) * encryptedMsg % N;
    cout << "alternative decryption output: " << endl
         << alternativeDecryptionOutput << endl
         << "encryption is decrypted: " << endl
         << (plainMessage ==
             alternativeDecryptionOutput)
         << endl;

    return 0;
}

/*
El Gamal Encryption Notes:
1. Compations are equivalent between DF and El Gamal 
2. Alice sticks to her public key in El Gamal. 
3. N and P are chosen by Alice. 
4. The ephemeral key must be different for every plain text
5. Bob is required to used a different private key every time he encryptes 
so that the ephemeral key and masking key will be different. Even though the same value
is encrypted, the cipher text would be different. 
6. El Gamal is a probabilistic encryption scheme as Bob choosing is private key plays 
the role of randomiser. This key should be between 2 and N-2

Computational Aspects: 
Square and multiplication algorithm can be used to calculate:  
    pubKey_ALICE
    pubKey_BOB
    encryptionKey
    aliceFindsOutKey
Extended Euclidean algo to compute the inverse
    aliceInversesKey

Fermat's little theorem = x^p-1 = 1 mod p, where p is prime
    plainText = aliceInversesKey * encryptedMsg = pubKey_BOB^(N-1-prvKey_ALICE) *encryptedMsg mod P


*/