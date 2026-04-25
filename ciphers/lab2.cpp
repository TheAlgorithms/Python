#include<iostream>
#include<vector>
#include<string>

using namespace std;

int modInverse(int n)
{
    n %= 26;
    for(int i = 0; i < 26; i++)
    {
        if((n * i) % 26 == 1)
            return i;
    }
    return -1;
}

string encrypt(string text, int key[2][2])
{
    string cipher = "";
    for(int i = 0; i < text.length(); i += 2)
    {
        int p1 = text[i] - 'A';
        int p2 = text[i+1] - 'A';

        cipher += char((key[0][0]*p1 + key[0][1]*p2) % 26 + 'A');
        cipher += char((key[1][0]*p1 + key[1][1]*p2) % 26 + 'A');
    }
    return cipher;
}

string decrypt(string cipher, int key[2][2])
{
    int det = (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 26;
    if(det < 0) det += 26;

    int invdet = modInverse(det);
    if(invdet == -1) return "Key is not invertible";

    int invKey[2][2];

    invKey[0][0] = ( key[1][1] * invdet ) % 26;
    invKey[0][1] = (-key[0][1] * invdet ) % 26;
    invKey[1][0] = (-key[1][0] * invdet ) % 26;
    invKey[1][1] = ( key[0][0] * invdet ) % 26;

    for(int i = 0; i < 2; i++)
        for(int j = 0; j < 2; j++)
            if(invKey[i][j] < 0)
                invKey[i][j] += 26;

    string plain = "";

    for(int i = 0; i < cipher.length(); i += 2)
    {
        int c1 = cipher[i] - 'A';
        int c2 = cipher[i+1] - 'A';

        plain += char((invKey[0][0]*c1 + invKey[0][1]*c2) % 26 + 'A');
        plain += char((invKey[1][0]*c1 + invKey[1][1]*c2) % 26 + 'A');
    }

    return plain;
}

int main()
{
    int key[2][2];
    string message;

    cout << "Enter 4 integers for the key matrix (2x2): ";
    for(int i = 0; i < 2; i++)
        for(int j = 0; j < 2; j++)
            cin >> key[i][j];

    cout << "Enter message (uppercase letters only): ";
    cin >> message;

    // Ensure even length
    if(message.length() % 2 != 0)
        message += 'X';

    string cipher = encrypt(message, key);
    cout << "Encrypted message: " << cipher << endl;

    string decrypted = decrypt(cipher, key);
    cout << "Decrypted message: " << decrypted << endl;

    return 0;
}