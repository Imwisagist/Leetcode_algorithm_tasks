# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guessNumber(n: int) -> int:
    lower_bound, upper_bound = 1, n
    my_guess = (lower_bound+upper_bound) >> 1

    while (res := guess(my_guess)) != 0:
        if res == 1:
            lower_bound = my_guess + 1
        else:
            upper_bound = my_guess - 1
        my_guess = (lower_bound+upper_bound) >> 1

    return my_guess
