from distutils.core import setup
import py2exe
import os
import re
from pathlib import Path
from time import sleep
from random import randrange
import sqlite3
import re

setup(console=["MyScript.py"])
