# Name: NP-chaonay/Main Python module
# Description: Module contains object for general usage
# Author: NP-chaonay (Nuttapong Punpipat)
# Version: V.2.2.3_stable
# Version Note: 
#       - Major version: indicates of very significant changes or changes that break compatibility on some system/platforms.
#       - Minor version: indicates of significant changes or features adding.
#       - Micro version: indicates of small changes or bug patches, or even typo revising.
# Revised Date: 2020-07-01 06:15 (UTC)
# License: MIT License
# Programming Language: Python
# CUI/GUI Language: English

__version__='2.2.3'
__doc__="""
Module contains object for general usage

Module Contents (excluding _*) :
- ValueWarning (class)
- display_datetime (function)
- alternative_type_checking (function)
- alternative_isinstance (function)
- alternative_issubclass (function)
- arg_value_error (function)
- print_categorical_bracket (function)
+ Documentation isn't fully implemented :
    - Namespace (class)
+ Type-checking is not fully implemented :
    - add_lead_zero (function)
"""

######## Pre-Initialization ########

import warnings as _warnings
import time as _time
from types import SimpleNamespace as _Namespace

######## Completed (Required for module initialization) ########

class ValueWarning(Warning):
	"""Warning related value content issue"""
	pass

######## Post-Initialization ########

_warnings.filterwarnings('always','',ValueWarning,'^'+__name__+'$')
_warnings.filterwarnings('default','',DeprecationWarning,'^'+__name__+'$')

######## Completed ########

def display_datetime(epoch_time=None):
	"""Display datetime from specific timestamp from epoch (or using current time).
		
	Optional arguments:
	- epoch_time (None, int-alike, or float-alike) : Set timestamp from epoch to be displayed. Set as None to get the current time instead.
	"""
	if epoch_time is not None and not isinstance(epoch_time,(int,float)):
		raise TypeError('Inputted value for \'epoch_time\' should be None, integer-like, or float-like, not \''+epoch_time.__class__.__name__+'\'.'+'\nAt: function:display_datetime, module:'+__name__)
	if epoch_time is None:
		epoch_time=_time.time()
	epoch_time=list(map(lambda x:add_lead_zero(x,2,True),_time.localtime(epoch_time)))
	return ':'.join(epoch_time[3:6])+' on '+'-'.join(epoch_time[0:3])

def alternative_type_checking(obj_name,types,value):
	'''Alternative of regular-method of type checking. Check if value is the given type, else will raise the exception.
	
	Arguments:
	- obj_name (not-empty str): Reported variable name when type checking is not pass.
	- types (not-empty tuple consists of types): Tuple of types that the given object should be matched one of these.
	- value: Any object to check its type.
	'''
	if type(obj_name)!=str : raise TypeError('Inputted value for this function arugment \'obj_name\' must be str.')
	if type(types)!=tuple : raise TypeError('Inputted value for this function arugment \'types\' must be tuple.')
	if not obj_name: raise ValueError('Inputted value for this function arugment \'obj_name\' must not be empty string.')
	if not types: raise ValueError('Inputted value for this function arugment \'types\' must not be empty tuple.')
	for type_ in types:
		if type(type_)!=type: raise TypeError('Inputted tuple for this function arugment \'types\' must only consists of types only.')
	if not type(value) in types:
		msg=[]
		for type_ in types:
			msg+=[type_.__name__]
		if len(msg)==1:
			msg=msg[0]
		elif len(msg)==2:
			msg=msg[0]+' or '+msg[1]
		else:
			msg=', '.join(msg[:-1])+', or '+msg[-1]
		raise TypeError('Inputted value for \''+obj_name+'\' should be '+msg+'.')

def alternative_isinstance(obj_name,types,value):
	'''Alternative usage of Python isinstance builtin-function for type checking. Check if value is the given type, else will raise the exception.
	
	Arguments:
	- obj_name (not-empty str): Reported variable name when type checking is not pass.
	- types (not-empty tuple consists of types): Tuple of types that the given object should be matched or inherited from one of these.
	- value: Any object to check its type.
	'''
	if type(obj_name)!=str : raise TypeError('Inputted value for this function arugment \'obj_name\' must be str.')
	if type(types)!=tuple : raise TypeError('Inputted value for this function arugment \'types\' must be tuple.')
	if not obj_name: raise ValueError('Inputted value for this function arugment \'obj_name\' must not be empty string.')
	if not types: raise ValueError('Inputted value for this function arugment \'types\' must not be empty tuple.')
	for type_ in types:
		if type(type_)!=type: raise TypeError('Inputted tuple for this function arugment \'types\' must only consists of types only.')
	if not isinstance(value,types):
		msg=[]
		for type_ in types:
			msg+=[type_.__name__+'-alike']
		if len(msg)==1:
			msg=msg[0]
		elif len(msg)==2:
			msg=msg[0]+' or '+msg[1]
		else:
			msg=', '.join(msg[:-1])+', or '+msg[-1]
		raise TypeError('Inputted value for \''+obj_name+'\' should be '+msg+'.')

def alternative_issubclass(obj_name,parent_classes,sub_class):
	'''Alternative usage of Python issubclass builtin-function for class inheritance checking. Check if sub_class is inherited from given classes, else will raise the exception.
	
	Arguments:
	- obj_name (not-empty str): Reported variable name when class inheritance checking is not pass.
	- parent_classes (not-empty tuple consists of classes): Tuple of classes that the given class should be inherited from one of these.
	- sub_class (class) : Any class to check its class inheritance.
	'''
	if type(obj_name)!=str : raise TypeError('Inputted value for this function arugment \'obj_name\' must be str.')
	if type(parent_classes)!=tuple : raise TypeError('Inputted value for this function arugment \'parent_classes\' must be tuple.')
	if not obj_name: raise ValueError('Inputted value for this function arugment \'obj_name\' must not be empty string.')
	if not parent_classes: raise ValueError('Inputted value for this function arugment \'parent_classes\' must not be empty tuple.')
	if type(sub_class)!=type: raise TypeError('Inputted value for this function arugment \'sub_class\' must be class.')
	for parent_class in parent_classes:
		if type(parent_class)!=type: raise TypeError('Inputted tuple for this function arugment \'types\' must only consists of classes only.')
	if not issubclass(sub_class,parent_classes):
		msg=[]
		for parent_class in parent_classes:
			msg+=[parent_class.__name__]
		if len(msg)==1:
			msg=msg[0]
		elif len(msg)==2:
			msg=msg[0]+' or '+msg[1]
		else:
			msg=', '.join(msg[:-1])+', or '+msg[-1]
		raise TypeError('Inputted class for \''+obj_name+'\' should be inherited from '+msg+'.')

def arg_value_error(name,statement,err_type=ValueError):
	"""My implementation for raising custom exception relates to arugument's value.

	Arguments:
	- name (str-alike): Reported variable name when type checking is not pass.
	- statement (str-alike): Statement to report
	Optional arguments:
	- err_type (class inherited from Exception): Exception to use
	"""
	alternative_isinstance('name',(str,),name)
	alternative_isinstance('statement',(str,),statement)
	alternative_isinstance('err_type',(type,),err_type)
	alternative_issubclass('err_type',(Exception,),err_type)
	raise err_type('Inputted value for \''+name+'\' should '+statement+'.')

def print_categorical_bracket(category,text,**kwargs):
	"""Implementation of print: Print message in format "[CATEGORY] Example text.".

	Arguments:
	- category (str-alike): Text to be displayed in square brackets.
	- text (str-alike): Passage to be displayed.
	Optional arguments:
	- **kwargs: Parameters to pass on print function.
	"""
	alternative_isinstance('category',(str,),category)
	alternative_isinstance('text',(str,),text)
	print('['+category+'] '+text,**kwargs)

######## Documentation isn't fully implemented ########

class Namespace(_Namespace):
	def __init__(self,name=None):
		_warnings.warn('1 year after this release published, this class will be removed from module. Use \'types.SimpleNamespace\' instead.',DeprecationWarning)
		if name!=None:
			if isinstance(name,str):
				self.__name__=str(name)
			else:
				raise TypeError('\'name\' should be string-alike.')
	def __repr__(self):
		_warnings.warn('1 year after this release published, this class will be removed from module. Use \'types.SimpleNamespace\' instead.',DeprecationWarning)
		if '__name__' in dir(self):
			return '<np_chaonay.main.Namespace \''+self.__name__+'\'>'
		else:
			return '<np_chaonay.main.Namespace (no name)>'

######## Type-checking is not fully implemented ########

def add_lead_zero(num,digit,IgnoreDataManipulation=False,RaiseDataManipulationError=False,DigitMustAtLeastTwo=False):
	"""Add leading the letters '0' to inputted integer 'num' according to defined 'digit' and return as string.
		
	Required keyword arguments:
	- num (int) : Integer (can be positive, zero, or negative)
	- digit (int) : How much digits of number should be in returned string.

	Optional keyword arguments:
	- IgnoreDataManipulation (bool) : Avoid raising acceptable data manipulation warning.
	- RaiseDataManipulationError (bool) : Raise every data manipulation warning as error exception. (IgnoreDataManipulation must be False.)
	- DigitMustAtLeastTwo (bool) : Raise warning or error if defined digit is less than 2.

	Data manipulation error:
	- Digit should be at least 2. (Ignore by default)
	- Amount of defined digits is less than digits of number in inputted integer.
	"""
	if type(num) is not int or type(digit) is not int: raise TypeError('parameters \'num\', \'digit\' should be integer.'+'\nAt: function:display_datetime, module:'+__name__)
	if type(IgnoreDataManipulation) is not bool or type(RaiseDataManipulationError) is not bool or type(DigitMustAtLeastTwo) is not bool: raise TypeError('parameters \'IgnoreDataManipulation\', \'RaiseDataManipulationError\', and \'DigitMustAtLeastTwo\' should be boolean.'+'\nAt: function:display_datetime, module:'+__name__)
	if IgnoreDataManipulation: RaiseDataManipulationError=False
	if digit<1: raise ValueError('Digit should be at least one.'+'\nAt: function:display_datetime, module:'+__name__)
	if digit<2 and DigitMustAtLeastTwo:
		msg='Amount of digits should be at least 2.'+'\nAt: function:display_datetime, module:'+__name__
		if not IgnoreDataManipulation and not RaiseDataManipulationError: _warnings.warn(msg,ValueWarning)
		if RaiseDataManipulationError: raise ValueError(msg)
	# Reuse variable 'digit'
	if num>=0:
		num=str(num)
		IsNegative=False
	else:
		num=str(abs(num))
		IsNegative=True
	digit=digit-len(num)
	if digit>0:
		for x in range(0,digit):
			# Reuse variable 'num'
			num='0'+num
		if not IsNegative: return num
		else: return '-'+num
	elif digit==0:
		if not IsNegative: return num
		else: return '-'+num
	else:
		msg='Defined digits amount is less than digits of number in inputted integer. It possibly means that some of used data has been manipulated incorrectly.'+'\nAt: function:display_datetime, module:'+__name__
		if not IgnoreDataManipulation and not RaiseDataManipulationError: _warnings.warn(msg,ValueWarning)
		if RaiseDataManipulationError: raise ValueError(msg)
		if not IsNegative: return num
		else: return '-'+num
