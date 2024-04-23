# https://contest.yandex.ru/contest/60242/problems/B/

def check_user_input(target: str, user_input: str) -> bool:
    spec_sym, pointer, result, spec_flag = "", 0, [], False

    for c in user_input:
        if c == "<":
            spec_flag = True
            continue

        elif c == ">":
            if spec_sym == "left":
                if pointer != 0: pointer -= 1
            elif spec_sym == "right":
                if pointer < len(result): pointer += 1
            elif spec_sym == "delete":
                if result and (pointer < len(result)): result.pop(pointer)
            elif spec_sym == "bspace":
                if pointer > 0 and result[pointer-1]:
                    result.pop(pointer-1)
                    pointer -= 1

            spec_flag, spec_sym = False, ""
            continue

        if spec_flag: spec_sym += c
        else:
            result.insert(pointer, c)
            pointer += 1

    return target == "".join(result)


print("Yes" if check_user_input(input().strip(), input().strip()) else "No")
