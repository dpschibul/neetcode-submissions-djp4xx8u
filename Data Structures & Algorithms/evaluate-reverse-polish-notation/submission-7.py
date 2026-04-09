class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.calculate(a, b, token))
            else:
                stack.append(int(token))
        return stack[-1]
        

        
                    
    def calculate(self, a: int, b: int, operator: str) -> int:
        if operator == "+":
            return a + b
        if operator == "*":
            return a * b
        if operator == "-":
            return b - a
        if operator == "/":
            return int(b / a)



        