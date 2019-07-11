# Questions

## What'sdint.h' ?
it shall declares width of integers.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?
to specify the width of each integter.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

1, 4, 4, 2.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."



## What's the difference between `bfSize` and `biSize`?
bisize is the total size of image in bytes including pixels and padding
while bfsize is the sum of bisize image plus sizeof(bitmap file header)
plus sizeof(bitmap info header).

## What does it mean if `biHeight` is negative?

it is not opssible.
## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

bi.bibitcount.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

if the input cannot be opened for reading and the output cannotbe opened for writing
## Why is the third argument to `fread` always `1` in our code?

it must be 3.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3.

## What does `fseek` do?

indicator that keeps track where we are.

## What is `SEEK_CUR`?

current position in the file.

## Whodunit?

it was the professour plum with the 
candlessstick in the library.
