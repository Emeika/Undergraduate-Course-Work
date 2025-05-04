#include <MD5.h>

struct users
{
    char *name;
    char *hash_pw;
};

void setup()
{
    Serial.begin(9600);
    delay(1000);

    users User1 = {"hafsah", "81dc9bdb52d04dc20036dbd8313ed055"}; // pw: 1234
    users User2 = {"daim", "674f3c2c1a8a6f90461e8a66fb5550ba"};   // pw: 5678

    Serial.println("Enter username:");
    while (Serial.available() == 0)
    {
    }

    String username = Serial.readString();
    username.trim();
    Serial.println(username);

    users *loggedInUser = nullptr;

    if (strcmp(username.c_str(), User1.name) == 0)
    {
        loggedInUser = &User1;
    }
    else if (strcmp(username.c_str(), User2.name) == 0)
    {
        loggedInUser = &User2;
    }
    else
    {
        Serial.println("Username not found");
        return;
    }

    Serial.println("Enter password: ");
    while (Serial.available() == 0)
    {
    }

    String password = Serial.readString();
    password.trim();

    // Generate the MD5 hash for the entered password
    unsigned char *hash = MD5::make_hash(password.c_str());
    char *md5str = MD5::make_digest(hash, 16);
    free(hash);

    if (strcmp(md5str, loggedInUser->hash_pw) != 0)
    {
        Serial.println("Incorrect password");
    }
    else
    {
        Serial.println("Logged in successfully");
    }

    // Free memory used by md5str
    free(md5str);

    return;
}

void loop()
{
}
