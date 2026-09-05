class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized_str = ''.join(c for c in s if c.isalnum()).lower()
        half_len = int(len(sanitized_str)/2)
        chars = list(sanitized_str)

        first_half = chars[0:half_len+(len(sanitized_str)%2)];
        second_half = chars[half_len:len(sanitized_str)][::-1]
        

        print(first_half)
        print(second_half)

        return bool(first_half == second_half)