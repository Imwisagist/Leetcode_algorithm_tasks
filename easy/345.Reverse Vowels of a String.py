# https://leetcode.com/problems/reverse-vowels-of-a-string/

def reverseVowels(s: str) -> str:
    vowels, vowels_stack, sorted = "aeiouAEIOU", [], ""

    for char in s:
        if char in vowels:
            vowels_stack.append(char)

    for char in s:
        sorted += vowels_stack.pop() if char in vowels else char
            
    return sorted


assert reverseVowels("hello") == "holle"
assert reverseVowels("leetcode") == "leotcede"
