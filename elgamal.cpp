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

    //Bob can create a public key to share with Alice
    mp::cpp_int pubKey_BOB = mp::pow(mp::cpp_int(publicBase), prvKey_BOB) % N;

    //Alice can create a public key to share with Bob
    mp::cpp_int pubKey_ALICE = mp::pow(mp::cpp_int(publicBase), prvKey_ALICE) % N;

    //Bob creates encryption key from what Alice sent him
    mp::cpp_int encryptionKey = mp::pow(mp::cpp_int(pubKey_ALICE), prvKey_BOB) % N;

    //Bob encrypts the msg and sends it to Alice
    mp::cpp_int encryptedMsg = (encryptionKey * plainMessage) % N;

    //Alice first needs to figure out the encryption key Bob used
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

    return 0;
}