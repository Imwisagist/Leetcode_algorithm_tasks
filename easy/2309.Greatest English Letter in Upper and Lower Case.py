# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

def greatestLetter(s: str) -> str:
    chars, s = "ZYXWVUTSRQPONMLKJIHGFEDCBA", set(s)

    for c in chars:
        if c in s and (c.lower() in s): return c

    return ""  


assert greatestLetter("lEeTcOdE") == "E"
assert greatestLetter("arRAzFif") == "R"
assert greatestLetter("AbCdEfGhIjK") == ""
