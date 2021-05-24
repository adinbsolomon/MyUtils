
import os
import json
import subprocess

# Locate this file
CustomCodePath = __file__.replace("setup\\setup.py", "")

# Read in config file
config_file = open(CustomCodePath + "setup\\config.json")
config = json.load(config_file)



'''
    Setting up the Python package

    This requires setting an environment variable on windows. This 
    environment variable is PYTHONPATH and shows Python's import
    utility where it should look for packages.
'''
PythonPath = "PYTHONPATH"
if os.getenv(PythonPath):
    print("PYTHONPATH environment variable is already set!")
else:
    subprocess.call(f"setx {PythonPath} {CustomCodePath}")
print(os.getenv(PythonPath))



'''
    Setting up ____ package
'''