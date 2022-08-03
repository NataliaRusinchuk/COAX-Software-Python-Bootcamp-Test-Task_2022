"""
Simple own hash function for strings
"""

def hash_simple(smth: str):
    """
    Simple hash function for hashing the string
    Hash codes may be from 0 to 1,000,000
    """
    n = len(smth)
    code = 0
    for i in range(n):
        code += (i+1)**2 * ord(smth[i])
    return int(code % 1e6)

s = "Python Bootcamp"
print(hash_simple(s))
