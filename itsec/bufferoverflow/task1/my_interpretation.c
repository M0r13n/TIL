//
// Created by Leon Morten Richter on 13.09.19.
//
int main(int argc,char *argv)

{
    int iVar1;
    size_t input_length;
    char buffer [20]; // create a buffer with 20 bytes
    int correct; // placeholder for correct password
    char *argv_cpy;
    int local_10;
    uint local_c; // das ist der exit code

    local_c = 0;
    // Check for correct usage
    if (argc == 3) {
        correct = 0; // password is false initially
        argv_cpy = argv; // argv in function (ignore)
        local_10 = argc; // argc in function (ignore)
        input_length = strlen((char *)puParm2[1]); // get length of users input
        if (input_length == 8) { // if it equals 8 continue
            iVar1 = strncmp((char *)argv[1],"password", 8); // does the first user arg equal the string password ?
            if (iVar1 == 0) { // if so, the password is correct
                correct = 1;
            }
        }
        strcpy(buffer,(char *)argv[2]);  // copy username (second argument by user) into buffer, which has only 20 bytes [ATTACK VECTOR]
        if (correct == 0) { // if the password that was checked previously is not correct
            printf("Your password is not valid.\n"); // say invalid
        }
        else { // else if it is correct
            printf("Hello %s. Your password is correct.\n",buffer);  // say correct and append the username
        }
        local_c = 0; // exit code 0 -> success
    }
    // This program requires exactly two arguments and if not called with exactly two  two, it will exit and print a usage message
    else {
        local_10 = argc;
        printf("Usage: %s <password> <name>\n",*puParm2);
        local_c = 1; // exit code 1 --> error
    }
    return (ulong)local_c;
}
