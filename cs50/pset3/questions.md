# Questions

## What's `stdint.h`?

Defines fixed width integer data types.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Eases working with data when a strict ordering of data is required. So location, storage, transportation and protocol management is possible.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

They are not the same on every system and program and can mean different things.
But in our case they are defined as follows:

BYTE = 8 bit = 1 byte
DWORD = 32 bit = 4 byte
WORD = 16 bit = 2 byte
LONG = 32 bit = 4 byte

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

Hex: 0x42 0x4D, Decimal: 66 77

## What's the difference between `bfSize` and `biSize`?

bfSize: To be found in the header and signals the size of the bitmap in bytes.
biSize: Size if BITMAPINFOHEADER in bytes.

## What does it mean if `biHeight` is negative?

It's a “top-down”-Bitmap and the image starts from top left, instead of bottom left.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in `copy.c`?

Could not open the file.

## Why is the third argument to `fread` always `1` in our code?

We read one byte at a time.

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

Zero (0).

## What does `fseek` do?

Change the pointer to the given offset

## What is `SEEK_CUR`?

Current pointer position.
