import pytest
from challenge import new_phrase

def test_if_it_is_callable():
	assert callable(new_phrase)

def test_to_get_rid_of_punctuation_and_spaces():
	assert new_phrase('he llo.wor ld') == new_phrase('helloworld')
	assert new_phrase('ha ppy. bir th.day') == new_phrase('happybirthday')

def test_to_get_rid_of_capital_letters():
	assert new_phrase('HEllOWorLd') == new_phrase('helloworld')

#def test_to_put_string_into_an_array():
	#assert new_phrase('helloworldimzach') == new_phrase('h e l l o w')
