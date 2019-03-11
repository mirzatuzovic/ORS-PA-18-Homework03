"""
===================   TASK 1   ====================
* Name: Sum Number Digits
*
* Write a function `sum_digits` that will return
* sum of digits for given integer number.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def sum_digits(number):

    if not isinstance(number,int):
        return -1

    sum = 0

    for i in str(abs(number)):
        sum += int(i)
    return sum




def main():

    int_number = 1234
    digit_sum = sum_digits(int_number)
    print("Sum of digits for given numbers is: ", digit_sum)

main()