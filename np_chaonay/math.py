# Name: NP-chaonay/Math Python module
# Description: Module contains object for mathematics usage
# Author: NP-chaonay (Nuttapong Punpipat)
# Version: V.1.1.0_dev
# Version Note: 
#       - Major version: indicates of very significant changes or changes that break compatibility on some system/platforms.
#       - Minor version: indicates of significant changes or features adding.
#       - Micro version: indicates of small changes or bug patches, or even typo revising.
# Revised Date: 2020-07-17 06:39 (UTC)
# License: MIT License
# Programming Language: Python
# CUI/GUI Language: English

__version__='1.1.0.dev'
__doc__="""
Module contains object for mathematics usage

Module Contents (excluding _*) :
- prime_generator (function)
- polymonial_long_division (function)
- Vector (class)
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

def polymonial_long_division(num_ce,den_ce):
	'''Long division a polymonial coefficient
	
	Arguments:
	- num_ce,den_ce (non-empty iterable object, length of 'num_ce' should be higher or equal to 'den_ce'): coefficient of each degrees from the numerator and denominator respectively.
	
	Return value:
	Tuple, contains:
	- result coefficient array
	- remainder array
	
	Example:
	- array with [1,-2,3] means x^2-2x+3
	
	Notes:
	- For the shape of returned arrays, depends on maximum possible amount of coefficient which depends on inputted arrays. See the source for how this function calulates.
	'''
	try: import numpy as np
	except: raise ImportError('Cannot import necessary \'numpy\' package. Origin exception should be shown above.')
	try:
		if len(num_ce)==0 or len(den_ce)==0: raise ValueError('\'num_ce\' and \'den_ce\' should not be empty.')	
		if len(num_ce)<len(den_ce): raise ValueError('Amount of number in \'num_ce\' must be equal or more than its of \'den_ce\'')	
	except: raise ValueError('Cannot find the length of both \'num_ce\' and \'den_ce\', both of them should be iterable.')
	try:
		num_ce=np.array(num_ce)
		den_ce=np.array(den_ce)
	except:
		raise ValueError('Cannot convert inputted iterable objects to numpy array. Make sure that \'num_ce\' and \'den_ce\' are iterable. Origin exception should be shown above.')
	num_highest_deg=len(num_ce)-1
	den_highest_deg=len(den_ce)-1
	round_num=num_highest_deg-den_highest_deg+1
	result_ce=np.zeros(round_num)
	rmd_ce=num_ce[0:len(den_ce)]
	for i in range(round_num):
		tmp=rmd_ce[0]/den_ce[0]
		result_ce[i]=tmp
		sub_ce=(tmp)*den_ce
		rmd_ce=rmd_ce-sub_ce
		if i+1==round_num: break
		else: rmd_ce=np.concatenate((rmd_ce[1:],(num_ce[i+len(rmd_ce)],)))
	return result_ce,rmd_ce[1:]

class Vector():
	# QualityCheckTags:
	# [/] CODE
	# [/] INPUTCHECK
	# [/] DOCS
	# [/] TEST
	''' Vector implementation
	
	# Object Creation
	    Vector(*dimensions)
	  Optional Arguments:
	  - *dimensions (int-alike,float-alike): Value of each dimensions
	
	# Object Representation
	  >>> Vector(-1,0,1)
	  Vector((-1,0,1)
	  
	# Object Iteration
	  >>> list(Vector(-1,0,1)
	  [-1,0,1]
	
	# Negative Unary
	  >>> -Vector(-1,0,1)
	  Vector(1,0,-1)
	
	# Adding/Subtracting
	  ## With same type
	    >>> Vector(-1,0,1)+Vector(-1,0,1)
	    Vector(-2,0,2)
	    >>> Vector(-1,0,1)-Vector(-1,0,1)
	    Vector(0,0,0)
	  ## With int-alike/float-alike
	    >>> Vector(-1,0,1)+1
	    Vector(0,1,2)
	    >>> Vector(-1,0,1)-1
	    Vector(-2,-1,0)
	
	# Multiplying
	  ## With int-alike/float-alike
	    >>> Vector(-1,0,1)*10
	    Vector(-10,0,10)
	
	# Methods
	  - magnitude()
	    Returns: Magnitude of vector
	
	# Variables
	  - dimensions (iterable) : consists of dimensions' values
	'''
	dimensions=[]
	def __init__(self,*dimensions):
		# Type Checking
		for dimension in dimensions: npc_m.alternative_isinstance('*dimensions',(int,float),dimension)
		self.dimensions=list(dimensions)
	def __repr__(self):
		return 'Vector('+repr(self.dimensions)[1:-1]+')'
	def __iter__(self):
		return (dimension for dimension in self.dimensions)
	def __neg__(self):
		new_dimensions=[]
		for i in range(len(self.dimensions)):
			new_dimensions+=[-self.dimensions[i]]
		return type(self)(*new_dimensions)
	def __add__(self,another):
		if type(self)==type(another):
			if len(self.dimensions)==len(another.dimensions):
				new_dimensions=[]
				for i in range(len(self.dimensions)):
					new_dimensions+=[self.dimensions[i]+another.dimensions[i]]
				return type(self)(*new_dimensions)
			else:
				raise ValueError('Adding vectors with different dimensions.')
		else:
			# Type Checking (Adding type(self) for exception displaying
			npc_m.alternative_isinstance('adding value',(int,float,type(self)),another)
			new_dimensions=[]
			for i in range(len(self.dimensions)):
				new_dimensions+=[self.dimensions[i]+another]
			return type(self)(*new_dimensions)
	def __sub__(self,another):
		if type(self)==type(another):
			if len(self.dimensions)==len(another.dimensions):
				new_dimensions=[]
				for i in range(len(self.dimensions)):
					new_dimensions+=[self.dimensions[i]-another.dimensions[i]]
				return type(self)(*new_dimensions)
			else:
				raise ValueError('Subtracting vectors with different dimensions.')
		else:
			# Type Checking (Adding type(self) for exception displaying
			npc_m.alternative_isinstance('adding value',(int,float,type(self)),another)
			new_dimensions=[]
			for i in range(len(self.dimensions)):
				new_dimensions+=[self.dimensions[i]-another]
			return type(self)(*new_dimensions)
	def __mul__(self,another):
		if type(self)==type(another):
			raise ValueError('Muliplying vectors is not implemented yet.')
		else:
			# Type Checking
			npc_m.alternative_isinstance('adding value',(int,float),another)
			new_dimensions=[]
			for i in range(len(self.dimensions)):
				new_dimensions+=[self.dimensions[i]*another]
			return type(self)(*new_dimensions)
	def magnitude(self):
		return (sum(tuple(map(lambda x: x**2,self.dimensions))))**0.5
