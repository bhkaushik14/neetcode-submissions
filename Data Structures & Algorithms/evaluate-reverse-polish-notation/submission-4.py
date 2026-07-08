class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+" | "-" | "*" | "/":
                    b = stack.pop()
                    a = stack.pop()

                    match token:
                        case "+":
                            stack.append(a+b)
                        case "-":
                            stack.append(a-b)
                        case "*":
                            stack.append(a * b)
                        case "/":
                            stack.append(int(a/b))
                case _: 
                    stack.append(int(token))

        return stack[0]         
