# Name: NP-chaonay/Math Python module
# Description: Module contains object for mathematics usage
# Author: NP-chaonay (Nuttapong Punpipat)
# Version: V.1.0.3_stable
# Version Note: 
#       - Major version: indicates of very significant changes or changes that break compatibility on some system/platforms.
#       - Minor version: indicates of significant changes or features adding.
#       - Micro version: indicates of small changes or bug patches, or even typo revising.
# Revised Date: 2020-07-13 10:12 (UTC)
# License: MIT License
# Programming Language: Python
# CUI/GUI Language: English

__version__='1.0.3'
__doc__="""
Module contains object for mathematics usage

Module Contents (excluding _*) :
- prime_generator (function)
"""

######## Initialization ########

from . import main as _npc_m

######## Objects ########
	
def prime_generator(amount=None):
	"""Prime Generator
	
	Optional arguments:
	- amount (None or int): Set how many output amount, set to None for endless output.
	"""
	_npc_m.alternative_isinstance('amount',(int,type(None)),amount)
	if amount is not None:
		if amount==0: return 123
		elif amount<0: _npc_m.arg_value_error('amount','not be less than zero')
	c=3
	primes=[2]
	yield 2
	while True:
		if amount is not None:
			if len(primes)>=amount: break
		for prime in primes:
			if c%prime==0: break
		else:
			primes+=[c]
			yield c
		c+=1
