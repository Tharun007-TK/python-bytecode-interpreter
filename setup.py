from setuptools import setup, find_packages

setup(
    name="byterun-py311",
    version="0.1.0",
    author="Tharun Kumar",
    description="A simple Python interpreter implemented in Python 3.11+ for learning bytecode internals.",
    packages=find_packages(),
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Software Development :: Interpreters",
    ],
    keywords="python interpreter bytecode vm educational",
    project_urls={
        "Homepage": "https://github.com/yourusername/byterun-py311",
        "Bug Reports": "https://github.com/yourusername/byterun-py311/issues",
        "Source": "https://github.com/yourusername/byterun-py311",
    },
)
