import os
import shutil

def prepare(PROJECT_DIR, KICKOFF_DIR):
  MAIN_SOURCE = os.path.join(KICKOFF_DIR, "assets/executable/main.cpp")
  MAIN_TARGET = os.path.join(PROJECT_DIR, "source/src/main.cpp")
  shutil.copy(MAIN_SOURCE, MAIN_TARGET)
