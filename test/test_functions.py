import pytest
import os
from functions import log
from functions import LOGS_PATH, SNAPSHOTS, FILES, DOCS, IMGS, WORKSPACE

class TestFunctions():

	def test_log():
		assert type(log()) == str , "log() must return a str"
		print("log() works")

	def test_directories():
		assert os.path.exists(LOGS_PATH) , "Function doesn't create LOGS_PATH"
		print("Function creates LOGS_PATH")
