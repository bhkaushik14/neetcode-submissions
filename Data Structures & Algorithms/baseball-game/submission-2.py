class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        scores_total = []

        for c in operations:
            match c:
                case val if val.lstrip("-").isdigit():
                    score = int(val)
                    scores_total.append(score)
                case "+":
                    score = scores_total[-1] + scores_total[-2]
                    scores_total.append(score)
                case "D":
                    score = scores_total[-1] * 2
                    scores_total.append(score)
                case "C":
                    scores_total.pop(-1)
        
        return sum(scores_total)


            