import pytest
from .passgen import generatePasscode

def generatePasscode_test():
    assert generatePasscode(3) == "acd"