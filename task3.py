"""
===================   TASK 3   ====================
* Name:  Euclidean algorithm
*
* Write a function `gcd` that will calculate
* greatest common divisor for two integer values.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

def gcd(a,b):

    r = a % b

    while(r != 0):

        a = b

        b = r

        q = int(a/b)

        r = a - (b * q)

    return b

def main():

    a = abs(int(input("First number: ")))

    b = abs(int(input("Second number: ")))

    print(gcd(a,b))

main()