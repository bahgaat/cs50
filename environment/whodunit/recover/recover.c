#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: write only the forensic image\n");
        return 1;
    }




    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s. \n",argv[1]);
        return 2;
    }
    unsigned char buffer[512];
    int counter=0;
    FILE *img;
    while (fread(&buffer,1,512,file)==512)
    {



         if(buffer[0]==0xff &&
         buffer[1]==0xd8 &&
         buffer[2]==0xff &&
         (buffer[3] & 0xf0) == 0xe0)
         {


              // char* newfile = malloc (x * sizeof(char)); i dont know i need it or know
              if (counter>0)
              {
                  fclose(img);
              }


              counter++;

              char filename[8];

              sprintf(filename,"%03i.jpg",counter-1);
              img = fopen(filename, "w");

              if (img==NULL)
              {
                  fclose(img);
                  fprintf(stderr,"could not create %s./n", filename);
                  return 3;
              }

              //fwrite(&buffer,sizeof(buffer),1,img);

          }

          if(counter>0)
          {
              fwrite(&buffer,sizeof(buffer), 1 , img);

          }

    }

    fclose(file);
    fclose(img);

    return 0;

}