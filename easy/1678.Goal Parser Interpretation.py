# https://leetcode.com/problems/goal-parser-interpretation/description/

def interpret(command: str) -> str:
    return command.replace("()", "o").replace("(al)","al")


assert interpret("G()(al)") == "Goal"
assert interpret("G()()()()(al)") == "Gooooal"
assert interpret("(al)G(al)()()G") == "alGalooG"
