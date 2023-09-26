# https://leetcode.com/problems/reverse-only-letters/description/

def reverseOnlyLetters(s: str) -> str:
    l, r, res = 0, len(s) - 1, list(s)

    while l < r:
        is_left_alpha, is_right_alpha = res[l].isalpha(), res[r].isalpha()

        if not is_left_alpha: l += 1

        if not is_right_alpha: r -= 1

        if is_left_alpha and is_right_alpha:
            res[l], res[r] = res[r], res[l]; l += 1; r -= 1

    return "".join(res)


assert reverseOnlyLetters("ab-cd") == "dc-ba"
assert reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
assert reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
