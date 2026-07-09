class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for j in range(len(temperatures)):
            found = False
            index = j + 1
            while index < len(temperatures):
                if temperatures[j] < temperatures[index]:
                    result.append(index - j)
                    found = True
                    break
                else:
                    index += 1
            if not found:
                result.append(0)
        
        print(result)
        return result
            
