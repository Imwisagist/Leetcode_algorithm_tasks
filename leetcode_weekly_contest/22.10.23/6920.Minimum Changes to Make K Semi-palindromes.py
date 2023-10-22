def minimumChanges(s: str, k: int) -> int:
    substrings = []; min_changes = 0

    for i in range(k):
        substring_len = len(s) // k

        if len(s) % k != 0: substring_len += 1
        
        substrings.append(s[:substring_len])
        s = s[substring_len:]

    for substring in substrings:
        changes = 0

        for i in range(len(substring) // 2):
            j = len(substring) - i - 1

            if substring[i] != substring[j]: changes += 1

        min_changes += changes

    return min_changes

assert minimumChanges("abcac",2) == 1
assert minimumChanges("abcdef",2) == 2
assert minimumChanges("aabbaa",3) == 0
#WA
