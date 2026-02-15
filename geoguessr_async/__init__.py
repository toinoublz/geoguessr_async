import os
import sys

from geoguessr_async.geoguessr import *

# Add the parent directory to the Python path
# This allows importing the geoguessr_async module in tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
