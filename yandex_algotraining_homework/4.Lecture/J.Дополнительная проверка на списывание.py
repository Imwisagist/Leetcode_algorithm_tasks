# https://contest.yandex.ru/contest/27665/enter/

import sys

def preproc_str(s, case_sen):
    cleaned = "".join((c if c.isalnum() or c == "_" else " " for c in s))
    
    if case_sen: return cleaned
    else: return cleaned.lower()

def is_correct(word, keywords, st_digit):
    if word in keywords: return False

    f_digit = word[0].isdigit()

    if f_digit:
        if len(word) == 1 or not st_digit: return False

    return True

def solve(keywords, case_sen, st_digit):
    cnt, w2pos, w_pos = {}, {}, 0

    for line in sys.stdin:
        line = preproc_str(line.strip(), case_sen)

        for word in line.split():
            if is_correct(word, keywords, st_digit):
                if word in cnt: cnt[word] += 1
                else: cnt[word] = 1; w2pos[word] = w_pos
                
                w_pos += 1

    popular, max_count = None, -1

    for w, count in cnt.items():
        if popular is None or (count > max_count):
            popular = w; max_count = count
        elif count == max_count and w2pos[w] < w2pos[popular]:
            popular = w

    return popular


n, case_sen, st_digit = sys.stdin.readline().strip().split()
case_sen, n = case_sen == "yes", int(n)
st_digit = st_digit == "yes"; keywords = set()

for _ in range(n):
    keyword = sys.stdin.readline().strip()

    if case_sen: keywords.add(keyword)
    else: keywords.add(keyword.lower())

print(solve(keywords, case_sen, st_digit))
