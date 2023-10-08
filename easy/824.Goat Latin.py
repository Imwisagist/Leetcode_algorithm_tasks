# https://leetcode.com/problems/goat-latin/description/

def toGoatLatin(sentence: str) -> str:
    vowels,res = {"a","e","i","o","u","A","E","I","O","U"},[]

    for i,word in enumerate(sentence.split(),1):
        if word[0] in vowels: res.append(word+"ma"+"a"*i)
        else: res.append(word[1:]+word[0]+"ma"+"a"*i)

    return " ".join(res)


assert toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
assert toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
