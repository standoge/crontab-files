import pytest
from functions import log

class TestFunctions():

	def test_log():
		assert type(log()) == str , "log() must return a str"
		print("log() works")
