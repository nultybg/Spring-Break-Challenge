import pytest
from leap import new_phrase

def is_test_callable():
	assert callable(new_phrase)

	