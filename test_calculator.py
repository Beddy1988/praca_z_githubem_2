import pytest
from calculator import add, substract, multiply, divide

def test_add():
  assert add(10,20) == 30
