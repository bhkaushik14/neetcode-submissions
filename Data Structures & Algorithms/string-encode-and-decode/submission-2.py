class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + "#" + word
        
        # print(encoded_str)

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        word = ""
        length = 0

        count = 0

        while len(s) > 0:
            c = s[count]
            if c == "#":
                index = s.index(c)
                length = int(s[:index])
                word = s[(index + 1):(length + index + 1)]

                decoded_list.append(word)

                s = s[(length + index + 1):]
                count = 0
            
            count += 1


        return decoded_list


