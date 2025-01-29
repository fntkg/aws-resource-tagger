import os
import importlib

# Gets all files in the taggers folder
for module in os.listdir(os.path.dirname(__file__)):
    if module.endswith(".py") and module != "__init__.py":
        importlib.import_module(f"taggers.{module[:-3]}")