class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            for ch in s:
                encoded += str(ord(ch)) + ","
            encoded += "|"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        if not s:
            return []

        encoded_words = s.split("|")[:-1]

        for word in encoded_words:
            decoded_word = ""
            ords = word.split(",")[:-1]

            for o in ords:
                decoded_word += chr(int(o))
            
            decoded.append(decoded_word)
        
        return decoded