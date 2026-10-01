# we have to create a special file __int__.py which turns a directory into a 
# package
'''
Python looks for __init__.py to know that a folder is a package.
Without it, older Python versions (pre‑3.3) cannot import the folder.
Modern Python allows “namespace packages” without this file, but regular 
packages still commonly include it for clarity. 

2. Runs initialization code when the package is imported
Anything inside __init__.py executes once, the first time the package is imported.
You can use it to:
set up package‑level variables
import submodules
configure logging

'''