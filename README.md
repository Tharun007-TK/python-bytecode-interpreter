# 🐍 Byterun-Py311 — A Python Interpreter Written in Python 3.11+

A small, educational implementation of a Python **bytecode interpreter** that runs Python code by interpreting its own **Python 3.11+ bytecode**. This project serves as a learning tool to understand how Python's virtual machine works internally.

Inspired by [Byterun (AOSA Book)](https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html) but **rebuilt for Python 3.11+**, which introduced new adaptive opcodes and inline caches.

## ✨ Features

✅ **Python 3.11+ Compatible** - Works with modern Python versions  
✅ **Safe Bytecode Reading** - Uses `dis.get_instructions()` for adaptive bytecode compatibility  
✅ **Stack-Based VM** - Mimics CPython's core execution model  
✅ **Extensible Design** - Easy to add new opcodes and features  
✅ **Educational Focus** - Well-documented code with clear examples  
✅ **Test Suite** - Comprehensive tests for core functionality

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

## 🚀 Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Install from Source

```bash
# Clone the repository
git clone https://github.com/Tharun007-TK/byterun-py311.git
cd byterun-py311

# Install in development mode
pip install -e .
```

### Install from PyPI (Future)

```bash
pip install byterun-py311
```

## ⚙️ Quick Start

### Basic Usage

```python
from src.byterun_vm import MiniVM

# Define a simple function
def add_numbers():
    a = 2
    b = 3
    return a + b

# Create and run the VM
vm = MiniVM()
result = vm.run_code(add_numbers.__code__, globals(), locals())
print(result)  # Output: 5
```

### Running the Demo

```bash
python examples/demo.py
```

This will execute several example functions and display their results.

## 🏗️ Architecture

### Core Components

#### MiniVM Class

The heart of the interpreter is the `MiniVM` class in `src/byterun_vm.py`:

- **`stack`**: List that simulates Python's evaluation stack
- **`globals`** & **`locals`**: Dictionaries for variable storage
- **`run_code()`**: Main execution method that processes bytecode instructions

#### Bytecode Execution Flow

1. **Instruction Fetching**: Uses `dis.get_instructions()` to safely read bytecode
2. **Opcode Dispatching**: Dynamic method dispatch based on opcode names (`op_LOAD_CONST`, `op_BINARY_OP`, etc.)
3. **Stack Operations**: Push/pop values as instructions execute
4. **Result Handling**: Return values are printed and can be captured

### Supported Opcodes

Currently implemented opcodes:

| Opcode         | Description                      | Status |
| -------------- | -------------------------------- | ------ |
| `RESUME`       | Function entry point             | ✅     |
| `LOAD_CONST`   | Load constant value              | ✅     |
| `LOAD_FAST`    | Load local variable              | ✅     |
| `STORE_FAST`   | Store local variable             | ✅     |
| `LOAD_GLOBAL`  | Load global variable             | ✅     |
| `LOAD_NAME`    | Load name (local/global/builtin) | ✅     |
| `POP_TOP`      | Pop top of stack                 | ✅     |
| `BINARY_OP`    | Binary operations (+, -, \*, /)  | ✅     |
| `CALL`         | Function calls                   | ✅     |
| `RETURN_VALUE` | Return from function             | ✅     |

## 📖 Usage Examples

### Example 1: Simple Arithmetic

```python
from src.byterun_vm import MiniVM

def calculate(x, y):
    result = x * 2 + y
    return result

vm = MiniVM()
vm.run_code(calculate.__code__, globals(), locals())
# Result: 7 (for calculate(2, 3): 2*2+3 = 7)
```

### Example 2: String Operations

```python
from src.byterun_vm import MiniVM

def greet(name):
    message = "Hello, " + name + "!"
    return message

vm = MiniVM()
vm.run_code(greet.__code__, globals(), locals())
# Result: Hello, World!
```

### Example 3: Multiple Operations

```python
from src.byterun_vm import MiniVM

def complex_calc(a, b, c):
    temp = a + b
    result = temp * c
    return result

vm = MiniVM()
vm.run_code(complex_calc.__code__, globals(), locals())
# Result: 15 (for complex_calc(2, 3, 3): (2+3)*3 = 15)
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_vm.py::test_add

# Run with verbose output
python -m pytest tests/ -v
```

### Current Test Coverage

- ✅ Basic arithmetic operations
- ✅ Constant loading
- ✅ Variable storage and retrieval
- ✅ Function calls with arguments

### Adding New Tests

Tests are located in the `tests/` directory. Add new test functions following the naming convention `test_*`:

```python
def test_new_feature():
    def my_function():
        # Your test code here
        pass

    vm = MiniVM()
    vm.run_code(my_function.__code__, globals(), locals())
    # Add assertions here
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

1. **Fork and Clone**

   ```bash
   git clone https://github.com/Tharun007-TK/byterun-py311.git
   cd byterun-py311
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .
   ```

3. **Run Tests**
   ```bash
   python -m pytest tests/
   ```

### Adding New Opcodes

1. **Identify the Opcode**: Use `dis.dis()` to see what opcodes your code generates
2. **Implement the Handler**: Add a method `op_OPCODE_NAME` to the `MiniVM` class
3. **Test Thoroughly**: Add tests and verify with existing examples

Example implementation:

```python
def op_NEW_OPCODE(self, instr):
    # Your implementation here
    pass
```

### Code Style

- Follow PEP 8 style guidelines
- Use descriptive variable names
- Add docstrings to new methods
- Keep methods focused and single-purpose

### Pull Request Process

1. Create a feature branch: `git checkout -b feature/new-opcode`
2. Make your changes and add tests
3. Ensure all tests pass: `python -m pytest tests/`
4. Update documentation if needed
5. Submit a pull request with a clear description

## 🗺️ Roadmap

### Phase 1: Core Operations ✅

- [x] Basic arithmetic operations
- [x] Variable loading/storing
- [x] Function calls
- [x] Constants and literals

### Phase 2: Control Flow (In Progress)

- [ ] Jump instructions (`JUMP_FORWARD`, `JUMP_IF_FALSE`)
- [ ] Comparison operations (`COMPARE_OP`)
- [ ] Conditional statements (if/else)
- [ ] Loops (while/for)

### Phase 3: Advanced Features

- [ ] Exception handling (`TRY/EXCEPT`)
- [ ] Function arguments and keyword arguments
- [ ] List/dict operations
- [ ] Import statements
- [ ] Class definitions

### Phase 4: Tools and Visualization

- [ ] Step-by-step bytecode visualization
- [ ] Performance benchmarking
- [ ] PyPI package publication
- [ ] Interactive debugger

### Phase 5: Optimization

- [ ] Inline caching
- [ ] Adaptive opcodes
- [ ] JIT compilation hints

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Original Byterun**: The [Architecture of Open Source Applications](https://aosabook.org/) book for the foundational concept
- **CPython Developers**: For the excellent `dis` module and bytecode documentation
- **Python Community**: For making Python's internals accessible and well-documented

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Tharun007-TK/byterun-py311/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Tharun007-TK/byterun-py311/discussions)
- **Documentation**: This README and inline code comments

---

## 🎉 Happy Interpreting

🐍✨
