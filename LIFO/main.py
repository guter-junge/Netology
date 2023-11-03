class LIFO_Stack:

    def __init__(self):
        self.Stack = []

    def is_empty(self):
        if self.Stack == []:
            return True
        else:
            return False

    def push(self, new_element):
        self.Stack.insert(0, new_element)

    def pop(self):
        self.Stack.pop(0)
        return self.Stack[0]

    def peek(self):
        return self.Stack[0]

    def size(self):
        return len(self.Stack)

    def sequence_balance(self):
        print(self.Stack)
        stack = []
        bracket_pairs = {')': '(', ']': '[', '}': '{'}

        for element in self.Stack:
            if not isinstance(element, str):
                if element in '([{':
                    stack.append(element)
                elif element in ')]}':
                    if not stack:
                        return 'Unbalanced'
                    top = stack.pop()
                    if top != bracket_pairs[element]:
                        return 'Unbalanced'
            else:
                for el in element:
                    if el in '([{':
                        stack.append(el)
                    elif el in ')]}':
                        if not stack:
                            return 'Unbalanced'
                        top = stack.pop()
                        if top != bracket_pairs[el]:
                            return 'Unbalanced'

        if len(stack) == 0:
            return 'Balanced'



if __name__ == '__main__':
    stack = LIFO_Stack()

    # stack.push('(((([{}]))))')
    # stack.push('[([])((([[[]]])))]{()}')
    # stack.push('{{[()]}}')
    # stack.push('}{}')
    # stack.push('{{[(])]}}')
    stack.push('[[{())}]')

    result = stack.sequence_balance()
    print(result)
