# https://leetcode.com/problems/sorting-the-sentence/description/

def sortSentence(s: str) -> str:
    words = s.split(); res = [None] * len(words)

    for word in words: res[int(word[-1])-1] = word[:-1]

    return " ".join(res)


assert sortSentence("is2 sentence4 This1 a3") == "This is a sentence"
assert sortSentence("Myself2 Me1 I4 and3") == "Me Myself and I"
