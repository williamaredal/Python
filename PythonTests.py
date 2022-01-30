import pytest

# Functions
def AdditionFunction(a, b):
    return a + b

def MultiplicationFunction(a, b):
    return a * b


# Tests
def test_addition_1():
    assert AdditionFunction(3, 2) == 6

def test_addition_2():
    assert AdditionFunction(3, 2) == 5

def test_multiplication_1():
    assert MultiplicationFunction(4, 2) == 4

def test_multiplication_2():
    assert MultiplicationFunction(2, 2) == 4
