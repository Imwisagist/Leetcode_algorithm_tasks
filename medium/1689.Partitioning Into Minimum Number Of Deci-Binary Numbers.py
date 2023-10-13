# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/

def minPartitions(n: str) -> int:
    return int(max(n))


assert minPartitions("32") == 3
assert minPartitions("82734") == 8
assert minPartitions("27346209830709182346") == 9
