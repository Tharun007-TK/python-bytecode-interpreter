import dis
import operator

class MiniVM:
    """A tiny Python bytecode interpreter for Python 3.11+."""

    def __init__(self):
        self.stack = []
        self.globals = {}
        self.locals = {}

    def run_code(self, code, globals=None, locals=None):
        self.stack = []
        self.globals = globals or {}
        self.locals = locals or {}

        for instr in dis.get_instructions(code):
            opname = instr.opname
            if hasattr(self, f"op_{opname}"):
                result = getattr(self, f"op_{opname}")(instr)
                if result is not None:  # If an opcode returns a value, it's the final result
                    return result
            else:
                raise NotImplementedError(f"Opcode {opname} not implemented")

    def op_RESUME(self, instr):
        pass

    def op_LOAD_CONST(self, instr):
        self.stack.append(instr.argval)

    def op_LOAD_FAST(self, instr):
        self.stack.append(self.locals[instr.argval])

    def op_STORE_FAST(self, instr):
        self.locals[instr.argval] = self.stack.pop()

    def op_LOAD_GLOBAL(self, instr):
        name = instr.argval
        self.stack.append(self.globals.get(name, __builtins__[name]))

    def op_LOAD_NAME(self, instr):
        name = instr.argval
        if name in self.locals:
            self.stack.append(self.locals[name])
        elif name in self.globals:
            self.stack.append(self.globals[name])
        else:
            self.stack.append(__builtins__[name])

    def op_POP_TOP(self, instr):
        self.stack.pop()

    def op_BINARY_OP(self, instr):
        right = self.stack.pop()
        left = self.stack.pop()
        symbol = instr.argrepr
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if symbol in ops:
            self.stack.append(ops[symbol](left, right))
        else:
            raise NotImplementedError(f"Unsupported operator {symbol}")

    def op_FORMAT_VALUE(self, instr):
        # For f-string formatting
        value = self.stack.pop()
        if instr.arg == 0:  # No format specifier
            self.stack.append(str(value))
        else:
            # For now, just convert to string
            self.stack.append(str(value))

    def op_BUILD_STRING(self, instr):
        # Build string from multiple parts (for f-strings)
        count = instr.arg
        parts = []
        for _ in range(count):
            parts.append(self.stack.pop())
        parts.reverse()  # Stack is LIFO
        self.stack.append(''.join(parts))

    def op_CALL(self, instr):
        argc = instr.arg
        args = [self.stack.pop() for _ in range(argc)][::-1]
        func = self.stack.pop()
        self.stack.append(func(*args))

    def op_RETURN_VALUE(self, instr):
        result = self.stack.pop()
        return result

    def op_RETURN_CONST(self, instr):
        # Return a constant value directly (Python 3.12+)
        return instr.argval

if __name__ == "__main__":
    def add(a, b):
        return a + b
    vm = MiniVM()
    vm.run_code(add.__code__, globals(), locals())
