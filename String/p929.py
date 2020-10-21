class Solution:
    """
    Runtime: 48 ms, faster than 84.29% of Python3 online submissions for Unique Email Addresses.
    Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Unique Email Addresses.
    """
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i, e in enumerate(emails):
            l, d = e.split('@')
            l = l.replace('.', '')
            l = l.split('+')[0]
            emails[i] = l + '@' + d
        return len(set(emails))
    """
    Runtime: 36 ms, faster than 99.78% of Python3 online submissions for Unique Email Addresses.
    Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Unique Email Addresses.
    """
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i, e in enumerate(emails):
            l, d = e.split('@')
            l = l.split('+')[0].replace('.', '')
            emails[i] = l + '@' + d
        return len(set(emails))