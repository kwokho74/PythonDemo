import sys
import fractal

def demo():
    # filedemo.WriteTextFileDemo()
    # filedemo.ReadTextFileDemo()

    pixels = fractal.mandelbrot(448, 256)
    write_grayscale("mandel.bmp", pixels)


def ReadTextFileDemo():
    # open file using with-block, close will be done automatically
    with open("demo.txt", mode="rt", encoding="utf-8") as f:
        for line in f:
            sys.stdout.write(line)


def WriteTextFileDemo():
    # open file without using with-block, have to close manually
    try:
        f = open("demo.txt", mode="at", encoding="utf-8")
        f.writelines(
            ["This is line 1\n", "This is line 2\n", "This is line 3\n"])
    finally:
        f.close()


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.

    Args:
        filename: The name of the BMP file to me created.

        pixels: A rectangular image stored as a sequence of rows.
            Each row must be an iterable series of integers in the
            range 0-255.

    Raises:
        ValueError: If any of the integer values are out of range.
        OSError: If the file couldn't be written.
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        # BMP Header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()     # The next four bytes hold the filesize as a 32-bit
        # little-endian integer. Zero placeholder for now.
        bmp.write(b'\x00\x00\x00\x00')

        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero

        # The next four bytes hold the integer offset to the
        pixel_offset_bookmark = bmp.tell()
        # pixel data. Zero placeholder for now.
        bmp.write(b'\x00\x00\x00\x00')

        # Image Header
        # Image header size in bytes - 40 decimal
        bmp.write(b'\x28\x00\x00\x00')
        bmp.write(_int32_to_bytes(width))  # Image width in pixels
        bmp.write(_int32_to_bytes(height))  # Image height in pixels
        bmp.write(b'\x01\x00')         # Number of image planes
        bmp.write(b'\x08\x00')         # Bits per pixel 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00')  # No compression
        bmp.write(b'\x00\x00\x00\x00')  # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Use whole color table
        bmp.write(b'\x00\x00\x00\x00')  # All colors are important

        # Color palette - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))  # Blue, Green, Red, Zero

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):  # BMP files are bottom to top
            row_data = bytes(row)
            bmp.write(row_data)
            # Pad row to multiple of four bytes
            padding = b'\x00' * ((4 - (len(row) % 4)) % 4)
            bmp.write(padding)

        # End of file
        eof_bookmark = bmp.tell()

        # Fill in file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    # &:  Bitwise-and
    # >>: Right-shift
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))
