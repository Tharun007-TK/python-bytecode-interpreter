import dis

# 1️⃣ Sample function we want to run via our mini interpreter
def sample():
    a = 2
    b = 2
    return a + b

# 2️⃣ A super simple virtual machine
class MiniVM:
    def __init__(self):
        self.stack = []  # stack to hold values
        self.vars = {}   # dictionary for variable storage

    def run(self, code_obj):
        instructions = list(dis.get_instructions(code_obj))
        for instr in instructions:
            name = instr.opname
            arg = instr.argval

            if name == 'LOAD_CONST':
                self.stack.append(arg)
            elif name == 'STORE_FAST':
                self.vars[arg] = self.stack.pop()
            elif name == 'LOAD_FAST':
                self.stack.append(self.vars[arg])
            elif name == 'BINARY_ADD':
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif name == 'BINARY_OP':
                b = self.stack.pop()
                a = self.stack.pop()
                if arg == 0:  # 0 is the arg for addition in BINARY_OP
                    self.stack.append(a + b)
                else:
                    print(f"Operation {arg} not implemented for BINARY_OP")
            elif name == 'RESUME':
                # Just continue execution for RESUME opcode
                pass
            elif name == 'RETURN_VALUE':
                return self.stack.pop()
            else:
                print(f"Opcode {name} not implemented yet!")

# 3️⃣ Run our mini interpreter
vm = MiniVM()
result = vm.run(sample.__code__)
print("Result from MiniVM:", result)