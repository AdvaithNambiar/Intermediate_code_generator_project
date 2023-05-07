class BinOpNode:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} {self.op} {self.right})"


class IntNode:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class FloatNode:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, value):
        self.symbols[name] = value

    def get_symbol(self, name):
        return self.symbols.get(name)


class CodeGenerator:
    def __init__(self):
        self.code = []

    def emit(self, op, arg1=None, arg2=None, result=None):
        self.code.append((op, arg1, arg2, result))

    def new_temp(self):
        return f"t{len(self.code)}"

    def generate(self, node):
        if isinstance(node, BinOpNode):
            left = self.generate(node.left)
            right = self.generate(node.right)
            temp = self.new_temp()
            self.emit(node.op, left, right, temp)
            return temp
        elif isinstance(node, IntNode):
            return node.value
        elif isinstance(node, FloatNode):
            return node.value
        else:
            raise TypeError(f"Unsupported node type: {type(node)}")

    def __str__(self):
        return '\n'.join([str(instruction) for instruction in self.code])

if __name__ == '__main__':
    symtab = SymbolTable()
    codegen = CodeGenerator()

    x = IntNode(2)
    y = IntNode(3)
    z = FloatNode(3.14)

    a = BinOpNode('+', x, y)
    b = BinOpNode('-', BinOpNode('*', IntNode(4), IntNode(5)), IntNode(2))
    c = BinOpNode('/', z, x)

    codegen.generate(a)
    codegen.generate(b)
    codegen.generate(c)
    print(codegen)
