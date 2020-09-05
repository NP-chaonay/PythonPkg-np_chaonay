# Name: NP-chaonay/Humour/Main Python module
# Description: Main module for humour-related objects
# Author: NP-chaonay (Nuttapong Punpipat)
# Version: V.1.0.3_stable
# Version Note:
#       - Major version: indicates of very significant changes or changes that break compatibility on some system/platforms.
#       - Minor version: indicates of significant changes or features adding.
#       - Micro version: indicates of small changes or bug patches, or even typo revising.
# Revised Date: 2020-08-09 13:21 (UTC)
# License: MIT License
# Programming Language: Python
# CUI/GUI Language: English

__version__='1.0.3'
__doc__ = """
Main module for humour-related objects

HAVING FUN!!!
"""

import time as _time

# Class look like function, however you wouldn't run this right?"""
class run_python():
	msg="You're already running Python intepreter!"
	def __repr__(self):
		return self.msg
# We also alert you if you want to run python2 inside python3.
class run_python2():
	msg="Use 'subprocess.run('python2')' to run python2 inside python3."
	def __repr__(self):
		return self.msg
run_python3=run_python

# Class-->Object like many objects that have implemented repr-noticing (such as exit, help), so when you accidentially run python in shell, you will know what're you running now!
python=run_python()
python3=python
python2=run_python2()

# Yeah, UNIX Epoch time is the example of time in the past.
past=_time.localtime(0)

# Implement zen string.
zen="You're the Zen!"

# Parent class of Python, Snake!
class Snake():
	pass
