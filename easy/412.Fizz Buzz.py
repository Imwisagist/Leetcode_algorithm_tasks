# https://leetcode.com/problems/fizz-buzz/

from typing import List

def fizzBuzz(n: int) -> List[str]:
        array: list = []
        for i in range(1, n + 1):
            if (i % 3 == 0) and (i % 5 == 0):
                array.append("FizzBuzz")
            elif i % 3 == 0:
                array.append("Fizz")
            elif i % 5 == 0:
                array.append("Buzz")
            else:
                array.append(str(i))

        return array


assert fizzBuzz(3) == ["1", "2", "Fizz"]
assert fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
assert fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
