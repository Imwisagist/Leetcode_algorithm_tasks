# https://leetcode.com/problems/increasing-decreasing-string/description/

def sortString(s: str) -> str:
    chars, counter, result = sorted(set(s)), {}, ""
    
    for char in s:
        counter[char] = counter.get(char, 0) + 1

    def sorting_string(arr: list) -> None:
        nonlocal result
        
        for char in arr:
            if char in counter:
                result += char
                counter[char] -= 1

                if counter[char] == 0:
                    del counter[char]

    while(counter):
        sorting_string(chars)
        sorting_string(reversed(chars))
                    
    return result


assert sortString("aaaabbbbcccc") == "abccbaabccba"
assert sortString("rat") == "art"
