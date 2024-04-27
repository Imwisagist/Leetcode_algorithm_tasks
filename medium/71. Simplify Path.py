# https://leetcode.com/problems/simplify-path/


def simplifyPath(path: str) -> str:
    words, stack = path.split('/'), []

    for word in words:
        if word == '' or word == '.': continue
        elif word == '..':
            if stack: stack.pop()
        else: stack.append(word)

    return '/' + '/'.join(stack)


assert simplifyPath("/home/") == "/home"
assert simplifyPath("/../") == "/"
assert simplifyPath("/home//foo/") == "/home/foo"
