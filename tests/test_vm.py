from src.byterun_vm import MiniVM

def test_add():
    def add():
        a = 2
        b = 3
        return a + b
    vm = MiniVM()
    result = vm.run_code(add.__code__, globals(), locals())
    assert result == 5, f"Expected 5, got {result}"

def test_const():
    def f():
        return 42
    vm = MiniVM()
    result = vm.run_code(f.__code__, globals(), locals())
    assert result == 42, f"Expected 42, got {result}"

def test_multiply():
    def multiply():
        x = 6
        y = 7
        return x * y
    vm = MiniVM()
    result = vm.run_code(multiply.__code__, globals(), locals())
    assert result == 42, f"Expected 42, got {result}"

def test_string_formatting():
    def greet():
        name = "World"
        return f"Hello, {name}!"
    vm = MiniVM()
    result = vm.run_code(greet.__code__, globals(), locals())
    assert result == "Hello, World!", f"Expected 'Hello, World!', got {result}"

if __name__ == "__main__":
    test_add()
    test_const()
    test_multiply()
    test_string_formatting()
    print("All tests passed!")
