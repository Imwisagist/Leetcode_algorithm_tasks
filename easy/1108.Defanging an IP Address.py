# https://leetcode.com/problems/defanging-an-ip-address/description/

def defangIPaddr(address: str) -> str:
    return address.replace(".", "[.]")


assert defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
assert defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
