'''
This program prints stdin to the screen.
'''
import sys

def cat(file):
    # Read in fixed-size chunks to maintain O(1) memory usage
    # regardless of input size
    while chunk := file.read(8192):
        sys.stdout.buffer.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
