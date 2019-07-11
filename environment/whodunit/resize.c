// Copies a BMP file

#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include "bmp.h"

int main(int argc, char *argv[])
{


    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: copy infile outfile\n");
        return 1;
    }

    // remember filenames
    char *x = argv[1];
    int n= atoi(x);
    char *infile = argv[2];
    char *outfile = argv[3];


    // open input file

    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }


    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // determine padding for scanlines



    // iterate over infile's scanlines

    int*heap_array=malloc(x*sizeof(int));
    int padding=(4-(bi.biWidth*n*sizeof(RGBTRIPLE))%4) % 4;

    for (int c=0, biHeight2=abs(bi.biHeight*n); c<biHeight2;c++)
    {

         for(int d=0; d<bi.biWidth*n; d++)
         {
             RGBTRIPLE word;

             fwrite(&word,sizeof(RGBTRIPLE),1,outptr);
         }

        // skip over padding, if any


        // then add it back (to demonstrate how)
        for (int k = 0; k < padding2; k++)
        {
            fputc(0x00, outptr);
        }
        fseek(inptr, padding2, SEEK_CUR);
    }



    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
