import pytest
import os
from src.functions import log
from src.functions import LOGS_PATH, SNAPSHOTS, FILES, DOCS, IMGS 

class TestFunctions():

	def test_log(self):
		assert type(log()) == str , "log() must return a str"
		print("log() works")

	def test_directories(self):
		assert os.path.exists(LOGS_PATH) , "Function doesn't create LOGS_PATH"
		assert os.path.exists(SNAPSHOTS) , "Function doesn't create SNAPSHOTS"
		assert os.path.exists(FILES) , "Function doesn't create FILES"
		assert os.path.exists(DOCS) , "Function doesn't create DOCS"
		assert os.path.exists(IMGS) , "Function doesn't create IMGS"
		print("All dirs was created")
