# https://leetcode.com/problems/truncate-sentence/description/

def truncateSentence(s: str, k: int) -> str:
    i = 0

    for _ in range(k): i = s.find(" ", i+1)

    return s[:i] if s[i] == " " else s


assert truncateSentence("Hello how are you Contestant",4) == "Hello how are you"
assert truncateSentence("What is the solution to this problem",4) == "What is the solution"
assert truncateSentence("chopper is not a tanuki",5) == "chopper is not a tanuki"
