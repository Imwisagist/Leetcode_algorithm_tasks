# https://leetcode.com/problems/restore-ip-addresses/
from typing import List


def restoreIpAddresses(s: str) -> List[str]:
    ans, n = [], len(s)

    if n > 12: return ans

    def valid_ip(s):
        if s and s[0] == '0': return False
        return int(s) < 256

    def dfs(i, curr, dots):
        if i == n or dots == 4:
            if i == n and dots == 4: ans.append(curr[:len(curr) - 1])
            return

        dfs(i + 1, curr + s[i] + '.', dots + 1)

        if i + 1 < n and valid_ip(s[i:i + 2]):
            dfs(i + 2, curr + s[i:i + 2] + '.', dots + 1)

        if i + 2 < n and valid_ip(s[i:i + 3]):
            dfs(i + 3, curr + s[i:i + 3] + '.', dots + 1)

    dfs(0, '', 0)

    return ans


assert restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"]
assert restoreIpAddresses("0000") == ["0.0.0.0"]
assert restoreIpAddresses("101023") == ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
