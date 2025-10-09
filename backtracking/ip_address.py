"""
    Restore IP Addresses
    -> IP Address consists of exactly four integers seperated by single dots.
    -> Each integer is between 0 and 255.
    -> Exempli Gratia - 192.168.1.1 is valid ip address but 192.168@1.1 is an invalid ip address.

    We are given with a string containing only digits , return all possible valid IP Addresses that 
    can be formed by inserting dots in the string.
    --> Not allowed to reorder or remove any digits in the string.
    --> Return valid IP addresses in any order.
    
    Topics covered: Backtracking
    
    Example:
    Input: s = "25525511135"
    Output: ["255.255.11.135","255.255.111.35"]

"""


class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, path):
            # Base case: if we have 4 parts and used all digits
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            # Try segments of length 1 to 3
            for l in range(1, 4):
                if start + l > len(s):
                    break
                segment = s[start:start + l]

                # Skip invalid parts (leading zeros or > 255)
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue

                backtrack(start + l, path + [segment])

        backtrack(0, [])
        return res
