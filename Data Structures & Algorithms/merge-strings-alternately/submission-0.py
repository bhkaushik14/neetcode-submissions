class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenWord1 = len(word1)
        lenWord2 = len(word2)

        output = ""
        index = 0

        while lenWord1 > 0 and lenWord2 > 0:
            output += word1[index] + word2[index]

            print(output)

            lenWord1 -= 1
            lenWord2 -= 1
            index += 1

        if lenWord1 == 0:
            output += word2[index:]
        else:
            output += word1[index:]

        return output