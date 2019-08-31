/* Recover JPEG's from memory.
 *
 * SUMMARY
 * JPEG'sd begin with 3 bytes (0xff 0xd8 0xff), followed by 4 bits containing 1110.
 *
 * Slack space is that space between photos, that is not used.
 *
 * n blocks = ceil(size_in_bytes / BLOCK_SIZE)
 *
 *  Pseudocode:
 *
 *  ITERATE over memory:
 *      CHECK for JPEG signature
 *      IF signature:
 *          OPEN a new file f
 *          DO UNTIL we reach another signature:
 *              COPY bytes (in blocks of 512 bytes) from memory to f
 * */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

// Constants and definitions
const int BLOCK_SIZE = 512;
const int JPEG_HEADER = 0xffd8ff;
const int INPUT_FILE_ERROR = 1;
const int OUTPUT_FILE_ERROR = 2;

int main(int argc, char *argv[])
{
    char *infile;
    uint8_t block[BLOCK_SIZE];
    int count = 0;
    int header[1];
    char outfile[8];
    int write = 0;
    FILE *outptr;

    if (argc != 2)
    {
        printf("Usage: recover infile \n");
        return INPUT_FILE_ERROR;
    }

    // Open input file
    infile = argv[1];
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return INPUT_FILE_ERROR;
    }

    while (fread(&block, BLOCK_SIZE, 1, inptr) == 1)
    {
        // Copy first 3 bytes
        memcpy(header, &block, 3);

        // Check for JPEG signature
        if ((*header == JPEG_HEADER) && (block[3] >= 0xe0))
        {
            // Close old file
            if (write)
            {
                fclose(outptr);
            }

            // Open new file
            sprintf(outfile, "%03i.jpg", count++);
            outptr = fopen(outfile, "w");
            write = 1;
            if (outptr == NULL)
            {
                fclose(inptr);
                printf("Could not create %s.\n", outfile);
                return OUTPUT_FILE_ERROR;
            }
        }
        if (write)
        {
            fwrite(block, BLOCK_SIZE, 1, outptr);
        }

    }
    // Cleanup
    fclose(inptr);
    fclose(outptr);
    return 0;
}