import pytest
import os
from src.functions import log
from src.functions import LOGS_PATH, SNAPSHOTS, FILES, DOCS, IMGS, WORKSPACE

class TestFunctions():

	def test_log(self):
		assert type(log()) == str , "log() must return a str"
		print("log() works")

	def test_directories(self):
		assert os.path.exists(LOGS_PATH) , "Function doesn't create LOGS_PATH"
		print("Function creates LOGS_PATH")
