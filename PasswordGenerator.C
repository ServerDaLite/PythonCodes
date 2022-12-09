#include <stdio.h>
#include <stdlib.h> // Random Library

// Still a work in Progress

// Setting password length
#define PASSWORD_LENGTH 32

int generateNumber(int maximum) {
    time_t t;
    srand((unsigned) time(&t));
    return rand() % maximum;
};

char* generatePassword(char* characters[]) {
    int character_length = sizeof(characters) / sizeof(char) - 1;
    char password[PASSWORD_LENGTH];
    
    for (int i = 0; i < PASSWORD_LENGTH; i++) {
        printf("- %d\n", generateNumber(5));
        password[i] = characters[generateNumber(character_length)];
    };
    
    return &password;
};

int main() {
    
    // Setting the possible characters
    char characters[] = "abc123XYZ!@#";
    
    char* password = generatePassword(characters);
    for (int i = 0; i < PASSWORD_LENGTH; i++) {
        printf("%d \n", &password[i]);
    };
    
    // Getting the length of characters
    //int character_length = sizeof(characters) / sizeof(char) - 1;
    
    // Initializing the password array
    //char password[PASSWORD_LENGTH];
    
    // Setting a number to clock
    //time_t t;
    
    // Setting random SEED to the time from t
    //srand((unsigned) time(&t));

    // Getting a random number
    // Finding the character with that random number
    // Appending that chacter to password array
    //for (int i = 0; i < PASSWORD_LENGTH; i++) {
    //    password[i] = characters[rand()%character_length];
    //};
    
    // Printing out the password together.
    //for (int i = 0; i < PASSWORD_LENGTH; i++) {
    //    printf("%c", password[i]);
    //};

    return 0;
}
