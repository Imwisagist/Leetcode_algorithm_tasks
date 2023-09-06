# https://leetcode.com/problems/unique-email-addresses/

from typing import List

def numUniqueEmails(emails: List[str]) -> int:
    def parse(email: str) -> str:
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        
        return f"{local}@{domain}"

    return len(set(map(parse, emails)))


assert numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]) == 2
assert numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]) == 3
assert numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]) == 2
