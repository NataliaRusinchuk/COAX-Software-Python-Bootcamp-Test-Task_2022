"""Prime numbers generator"""
import math

def prime_numbers_generator(start: int = 2, end: int = None) -> int:
    """
    Prime numbers generator

        Parameters:
            start (int): Default value is 2. A decimal integer, should be at least 2. Define the lowest number, which can be yielded by the generator;
            end (int): Default value is None, unlimited generator. Another decimal integer, should be higher than start. Define the highest number, which can be yielded by the generator;
        
        Returns:
            number (int): Decimal number.
    """
    
    # Check if the inputs are correct
    if (
        not isinstance(start, int) 
        or (end != None and not isinstance(end, int))
        or start < 2
        or (end and end<start)
    ):
        raise ValueError("Not valid end and start numbers. Start should be at least 2, end should be higher than start, both should be integers")
    number = start
    while True:
        # Break of the generator if reach the stop point
        if end is not None and number == end + 1:
            break
        else:
            # Look for divisor in the range of numbers up to the square root of the current number
            for i in range(2, math.floor(number**1/2) + 1):
                if (number % i) == 0:
                    break
            else:
                yield number
        number += 1

if __name__ == "__main__":
    print("Default generator\nFirst five prime numbers")
    a = prime_numbers_generator()
    for _ in  range(5):
        print(next(a))


    print("\nChange start value\nFirst five prime numbers starting from 4")
    a = prime_numbers_generator(4)
    for _ in  range(5):
        print(next(a))


    print("\nChange end value\nPrime numbers up to 15")
    a = prime_numbers_generator(end=15)
    for x in  a:
        print(x)


    print("\nChange both start and end values\nPrime numbers from 7 to 31")
    a = prime_numbers_generator(7, 31)
    for x in  a:
        print(x)


    print("\nString as input")
    try:
        a = prime_numbers_generator("cat")
        print(next(a))
    except Exception as e:
        print(str(e))


    print("\nFloat as input")
    try:
        a = prime_numbers_generator(3.0)
        print(next(a))
    except Exception as e:
        print(str(e))

    
    print("\nStart is higher than end")
    try:
        a = prime_numbers_generator(18, 3)
        for _ in  range(5):
            print(next(a))
    except Exception as e:
        print(str(e))
