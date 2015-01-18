"""
Utility Functions for my crypto exercises.
"""

from itertools import izip_longest

def xor_strings(a, b, hex=False):
    """XOR two strings"""
    if hex:
        a = a.decode('hex')
        b = b.decode('hex')
    return ''.join(chr(ord(x) ^ ord(y))
                   for x, y in izip_longest(a, b, fillvalue="\x00"))


def get_random(size=16):
    """Get random bits with specified size"""
    return open("/dev/urandom").read(size)
