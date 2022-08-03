import os
import shutil

def prepare(PROJECT_DIR, KICKOFF_DIR):
  TEST_SOURCE = os.path.join(KICKOFF_DIR, "assets/library/test")
  TEST_TARGET = os.path.join(PROJECT_DIR, "test")
  shutil.copytree(TEST_SOURCE, TEST_TARGET)
