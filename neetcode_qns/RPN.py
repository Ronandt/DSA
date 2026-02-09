class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #[1,4,3]
        #[*+]
        #  
        number_stack = []
        for x in tokens:
            if x.lstrip("-").isdigit():
                number_stack.append(int(x))
            else:
                number2 = number_stack.pop() #[1,2]
                number1 = number_stack.pop()

                if x == "+":
                    number_stack.append(number1 + number2)
                elif x =="*":
                     number_stack.append(number1 * number2)
                elif x== "-":
                     number_stack.append(number1 - number2)
                elif x == "/":
                     number_stack.append(int(number1/number2))
        return number_stack[0]