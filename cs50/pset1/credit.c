#include <stdio.h>
#include <math.h>
#include <cs50.h>

int splitter(long cardnumber, int position)
{
    long num1 = pow(10, position+1);
    long num2 = pow(10, position);
    int digit = (cardnumber % num1 / num2);
    return digit;
}

int givelength(long number)
{
    if (number >= 1000000000000000)
    {
        return 16;
    }
    if (number >= 100000000000000)
    {
        return 15;
    }
    if (number >= 10000000000000)
    {
        return 14;
    }
    if (number >= 1000000000000)
    {
        return 13;
    }
    // du musst nen default wert zurückgeben, sonst zickt z.B. GCC herum
    return -1;
}

int main(void)
{
    long cardnumber = get_long("Number: ");


    if ( givelength(cardnumber) > 16 || givelength(cardnumber) < 13)
    {
        printf("INVALID\n");
        return 0;
    }
    else
    {
        int firstSum = 0;

        for (int x = 1; x < givelength(cardnumber); x += 2)
        {
            int d = splitter(cardnumber, x) * 2;
            if(d > 9)
            {
                int d1 = splitter(d, 1);
                firstSum += d1;
                int d2 = splitter(d, 0);
                firstSum += d2;
            }
            else
            {
                firstSum += d;
            }
        }

        for (int x = 0; x < (givelength(cardnumber) + 1); x += 2)
        {
            int d = splitter(cardnumber, x);
            firstSum += d;
        }

        if (firstSum % 10 == 0)
        {
            // Ein long hat 64 bit und ein int 32.
            // Wenn du einen long auf einen int assignst,
            // passieren krumme Dinge, idr. negative werte
            long numX = cardnumber;

            // Idee ist richtig, aber du kennst die Länge der Zahl nicht
            // Die kann 15, 16, etc Ziffern haben
            // bei der Amex ratterst du zum Beispiel über das Ziel hinaus
            while (numX >= 100)
            {
                numX /= 100;
            }

            printf("%li\n", numX);
            if (numX < 56 && numX > 50)
            {
                printf("MasterCard\n");
                return 0;
            }
            if (numX == 34 || numX == 37)
            {
                printf("American Express\n");
                return 0;
            }
            if (numX < 50 && numX > 39)
            {
                printf("VISA\n");
                return 0;
            }
        }
    }
}

