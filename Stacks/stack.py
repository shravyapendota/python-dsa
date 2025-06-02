class Postfix:
    def _init_(self, expression):
        self.expression = expression
        self.stack = []

    def evaluate(self):
        for ch in self.expression:
            if ch.isdigit():
                self.stack.append(int(ch))
            elif ch in '+-*/':
                b = self.stack.pop()
                a = self.stack.pop()

                if ch == '+':
                    result = a + b
                elif ch == '-':
                    result = a - b
                elif ch == '*':
                    result = a * b
                elif ch == '/':
                    result = a // b  

                self.stack.append(result)
            else:
                print(f"Invalid character: {ch}")
                return None

        return self.stack.pop()


expr = input("Enter postfix expression: ")
evaluator = Postfix(expr)
result = evaluator.evaluate()

if result is not None:
    print("Result:", result)