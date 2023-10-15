
def shortestBeautifulSubstring(s: str, k: int) -> str:
    l,n,res = float("inf"),len(s),""

    for i in range(n):
        for j in range(i+1,n+1):
            if s[i:j].count('1') == k:
                if j-i <= l:
                    l = j-i

                    if not res: res = s[i:j].lstrip("0")
                    if s[i:j] < res: res = s[i:j].lstrip("0")

    return res


assert shortestBeautifulSubstring("110101000010110101",3) == "1011"
assert shortestBeautifulSubstring("001110101101101111",10) == "10101101101111"
assert shortestBeautifulSubstring("100011001",3) == "11001"
            
        