# https://leetcode.com/problems/count-binary-substrings/description/

def countBinarySubstrings(s: str) -> int:
    total = count = last_count = 0; last_chr = '-1' 

    for chr in s:
        if chr != last_chr: 
            total += min(count, last_count) 
            last_count = count; count = 1; last_chr = chr
        else: count += 1

    total += min(count, last_count)

    return total


assert countBinarySubstrings("00110011") == 6
assert countBinarySubstrings("10101") == 4
