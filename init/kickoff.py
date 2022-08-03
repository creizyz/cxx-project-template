import os
import shutil
import glob
import argparse
import stat
import importlib.util

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
PROJECT_NAME_PATTERN = "{{CXX_PROJECT}}"
TARGET_NAME_PATTERN = "{{cxx_target}}"
TEST_TARGET_NAME_PATTERN = "{{cxx_test}}"

KICKOFF_DIR = os.path.join(PROJECT_DIR, "init")
GIT_HISTORY_DIR = os.path.join(PROJECT_DIR, ".git")

README_TARGET = os.path.join(PROJECT_DIR, "readme.md")
CMAKE_TARGET = os.path.join(PROJECT_DIR, "source/CMakeLists.txt")

# ================================================================== #
# ================================================== # Project setup

def importMethodFromPythonFile(file, method):
  spec = importlib.util.spec_from_file_location(method, file)
  module = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  return module

# Replaces the all occurences of a word in a file
def replaceAllInFile(filename, replacements):
  print("  . processing '{0}'...".format(filename))
  # read input file
  with open(filename, 'r') as file :
    data = file.read()
  # replace all occurences
  for before, after in replacements:
    data = data.replace(before, after)
  # write output file
  with open(filename, 'w') as file:
    file.write(data)

def replaceAllInAllFiles(directory, replacements):
  for file in glob.glob(os.path.join(directory, "**/*"), recursive=True):
    if os.path.isfile(file) and not os.path.samefile(file, __file__):
      replaceAllInFile(file, replacements)

def on_rm_error(func, path, exc_info):
    #from: https://stackoverflow.com/questions/4829043/how-to-remove-read-only-attrib-directory-with-python-in-windows
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def kickoffProject(targetType, name):
  PROJECT_NAME = name.upper()
  TARGET_NAME = name.lower()
  TEST_TARGET_NAME = "test_{0}".format(TARGET_NAME)

  README_SOURCE  = os.path.join(KICKOFF_DIR, "configurations", "readme.{0}.md".format(targetType))
  CMAKE_SOURCE   = os.path.join(KICKOFF_DIR, "configurations", "CMakeLists.{0}.txt".format(targetType))
  PREPARE_SCRIPT = os.path.join(KICKOFF_DIR, "configurations", "prepare.{0}.py".format(targetType))

  print("[x] Setting up project '{0}'".format(PROJECT_NAME))
  print("  . Setting project name and targets...")
  replaceAllInAllFiles(PROJECT_DIR, [
    [ PROJECT_NAME_PATTERN, PROJECT_NAME ],
    [ TARGET_NAME_PATTERN, TARGET_NAME ],
    [ TEST_TARGET_NAME_PATTERN, TEST_TARGET_NAME ]
  ])

  print("  . Replacing project README...")
  shutil.copy(README_SOURCE, README_TARGET)

  print("  . Setting up project cmake...")
  shutil.copy(CMAKE_SOURCE, CMAKE_TARGET)

  print("  . Running project prepare script...")
  if os.path.isfile(PREPARE_SCRIPT):
    script = importMethodFromPythonFile(PREPARE_SCRIPT, "prepare")
    script.prepare(PROJECT_DIR, KICKOFF_DIR)

  print("  . Removing kickoff data...")
  shutil.rmtree(KICKOFF_DIR)

  print("  . Resetting up git history...")
  shutil.rmtree(GIT_HISTORY_DIR, onerror=on_rm_error)
  tmpDir = os.getcwd()
  os.chdir(PROJECT_DIR)
  os.system("git init")
  os.system("git add .")
  os.system("git commit -m \"initial commit\"")
  os.chdir(tmpDir)

  print("  . Done.\n")
  print("This project has been initialized using the kickoff script. Make sure to update the readme to add a summary of your project, and a list of dependencies.")

  return True

# ================================================================== #
# ================================================== # Command Line Interface

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' [Y] / N : ')).lower().strip() or "y"
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

CMAKE_FILES = glob.glob(os.path.join(KICKOFF_DIR, "configurations/CMakeLists.*.txt"))
AVAILABLE_CONFIGURATIONS = [ os.path.basename(path)[11:-4] for path in CMAKE_FILES ]
AVAILABLE_CONFIGURATIONS_STR = ", ".join(AVAILABLE_CONFIGURATIONS)

parser = argparse.ArgumentParser(description="An easy way to initialize a C++ project.")
parser.add_argument("configuration", help="the cmake configuration to use for the project (available: {})".format(AVAILABLE_CONFIGURATIONS_STR))
parser.add_argument("name", help="name of the project to kickoff")
parser.add_argument("--confirm", help="auto confirm", action=argparse.BooleanOptionalAction)
args = parser.parse_args()

# check configuration is valid
if args.configuration not in AVAILABLE_CONFIGURATIONS:
  print("error - configuration not recognized : {}".format(args.configuration))
  print("available configurations : {}".format(AVAILABLE_CONFIGURATIONS_STR))
  exit(1)

# ask user to confirm
print("[X] CXX project kickoff tool")
print("  . Project name : '{}'".format(args.name))
print("  . Project configuration : '{}'".format(args.configuration))

if (args.confirm):
  print("  . auto confirmed !")
elif yes_or_no("do you confirm project kickoff"):
  print("  . confirmed...")
else:
  print("  . canceled...")
  exit(0)

# Launch project kickoff
kickoffProject(args.configuration, args.name)