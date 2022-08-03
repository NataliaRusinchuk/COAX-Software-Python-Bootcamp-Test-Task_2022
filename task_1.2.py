"""
Hash the string using hashlib.md5 method
"""

import hashlib

s = "Python Bootcamp"
print(hashlib.md5(s.encode()).hexdigest())
