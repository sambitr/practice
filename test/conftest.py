import os
import sys

# Ensure the project root is on sys.path so tests can import the top-level `src` package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
