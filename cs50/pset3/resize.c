// Resize a BMP file

#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: copy scale infile outfile\n");
        return 1;
    }

    // Remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // Remember scale
    int scale = atoi(argv[1]);

    // Open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // Open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // Read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // Read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // Ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // Copy old headers
    BITMAPFILEHEADER bf_out = bf;
    BITMAPINFOHEADER bi_out = bi;

    // Update headers so match the new resolution
    bi_out.biWidth *= scale;
    bi_out.biHeight *= scale;

    // Determine padding for scanlines for both the in and out file
    int padding_in = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int padding_out = (4 - (bi_out.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // Change biSizeImage
    bi_out.biSizeImage = ((sizeof(RGBTRIPLE) * bi_out.biWidth) + padding_out) * abs(bi_out.biHeight);

    // Change bfSize
    bf_out.bfSize = bi_out.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // Write outfile's BITMAPFILEHEADER
    fwrite(&bf_out, sizeof(BITMAPFILEHEADER), 1, outptr);

    // Write outfile's BITMAPINFOHEADER
    fwrite(&bi_out, sizeof(BITMAPINFOHEADER), 1, outptr);

    // Iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        // Iterate over each line n times (scale vertically)
        for (int p = 0; p < scale; p++)
        {
            // Iterate over pixels in scanline
            for (int j = 0; j < bi.biWidth; j++)
            {
                // Temporary storage
                RGBTRIPLE triple;

                // Read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                // Write RGB triple to outfile ( scale horizontally )
                for (int k = 0; k < scale; k++)
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);

            }
            // Write outfiles padding
            for (int k = 0; k < padding_out; k++)
                fputc(0x00, outptr);

            // Reset the cursor, otherwise the the wrong line will be copied
            if (p < (scale - 1))
                fseek(inptr, -(bi.biWidth * sizeof(RGBTRIPLE)), SEEK_CUR);
        }
        // Skip over infiles padding
        fseek(inptr, padding_in, SEEK_CUR);
    }

    // Close infile
    fclose(inptr);

    // Close outfile
    fclose(outptr);

    // Success
    return 0;
}