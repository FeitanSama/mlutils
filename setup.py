import subprocess
import sys
from setuptools import setup

setup(name='mlutils',
      version='0.1.0',
      description='machine learning utilities',
      author='Charles Fisman - Guillaume Dupuy',
      packages=['mlutils'],
      zip_safe=False)
# subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])