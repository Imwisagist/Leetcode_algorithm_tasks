# https://leetcode.com/problems/decode-the-message/

def decodeMessage(key: str, message: str) -> str:
    hashmap, result = {" ": " "}, ""
    letters = iter("abcdefghijklmnopqrstuvwxyz")

    for k in key:
        if k not in hashmap:
            hashmap[k] = next(letters)

    for i in message: result += hashmap[i]

    return result


assert decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv") == "this is a secret"
assert decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly"
