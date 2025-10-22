from src.byterun_vm import MiniVM

def greet():
    name = "World"
    return f"Hello, {name}!"

def multiply():
    a = 3
    b = 4
    return a * b

def calculate():
    x = 2
    y = 3
    result = x * 2 + y
    return result

if __name__ == "__main__":
    vm = MiniVM()

    print("Testing greet function:")
    result = vm.run_code(greet.__code__, globals(), locals())
    print(f"Result: {result}")

    print("\nTesting multiply function:")
    result = vm.run_code(multiply.__code__, globals(), locals())
    print(f"Result: {result}")

    print("\nTesting calculate function:")
    result = vm.run_code(calculate.__code__, globals(), locals())
    print(f"Result: {result}")
