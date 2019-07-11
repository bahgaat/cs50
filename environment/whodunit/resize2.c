// Copies a BMP file

#include <stdio.h>
#include <stdlib.h>

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
    int n = atoi(x);
    if ( n<1 || n>100 )
    {
        fprintf(stderr,"Enter n between 1 and 100/n");
        return 1;
    }
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


    int infwidth = bi.biWidth;
    int infheight = bi.biHeight;
    int padding =( 4-(infwidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    bi.biWidth *=n;
    bi.biHeight *=n;
    int newpadding =( 4-(bi.biWidth * sizeof(RGBTRIPLE)) % 4)% 4;
    bi.biSizeImage =((bi.biWidth * sizeof(RGBTRIPLE)) + padding)* abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);





    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // determine padding for scanlines


    // iterate over infile's scanlines

    for (int i = 0, biHeight = abs(infheight); i < biHeight; i++)
    {
        RGBTRIPLE row[bi.biWidth];

        // iterate over pixels in scanline
        for (int j = 0; j < infwidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;


            // read RGB triple from infile


             fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

             for (int k=0; k<n; k++)
             {


            // write RGB triple to outfile
                row[k+ (n*j)]= triple;

             }



        }


        for(int y=0;y<n;y++)
        {
            fwrite(row,sizeof(row),1,outptr);

            for(int p=0;p<newpadding;p++)
            {
                fputc(0x00,outptr);
            }



        }


        fseek(inptr,padding,SEEK_CUR);

   }






    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
