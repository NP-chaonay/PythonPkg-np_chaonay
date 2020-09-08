#!/usr/bin/env python3
# Name: Python module "pymusicnote" on Python package "np_chaonay"
# Description: Module contains object for musical notation
# Author: NP-chaonay (Nuttapong Punpipat)
# Type: Module
# Version: (See on Python metadata below)
# Version Note: 
#       - Major version: indicates of very significant changes or changes that break compatibility on some system/platforms.
#       - Minor version: indicates of significant changes or features adding.
#       - Micro version: indicates of small changes or bug patches, or even typo revising.
# Revised Date: 2020-09-08 11:59 (UTC)
# License: MIT License
# Programming Language: Python
# CUI/GUI Language: English
# Development Status : In progress
# Development Stage :
#	[] Reviewing of Code
#	[] Reviewing of Type and Value Checking & Error Handling
#	[] Reviewing of Documentations
#	[] Testing

__version__='0.0.0.dev'
__doc__="""
Musical Notation implementation on Python.

Constant :
- a4_freq=400 : Standard frequency of note A4.
- a4_mnote : Musical note object in A4 pitch.
"""

# Import required modules
from math import log2 as _log2

# Define module constant
a4_freq=440

### Functions defination ###
def note_letter_to_number(notename):
	"""
	Read the string of musical notename and return correspond identification integer (From C to B as 0-11).

	Acceptable musical notename :
	- Uppercase and lowercase are supported. (Ex. 'Cb' = 'cb' -> 11)
	- Flat accidental must be always lowercase. (Ex. 'Cb' -> 11, but 'CB' -> Error raises.)
	- Poly-accidental is supported. (Ex. 'Cbbb' = 'A' -> 9)

	For example, inputting 'C','c','B#','b#' gives 0, inputting 'C#','c#','Db,'db' gives 1, inputting 'B','b','Cb','cb' gives 11.

	Required keyword arguments:
	- notename (str) : Musical notename as string.

	Error:
	- ValueError('Typed musical notename isn\'t supported.') : Input string isn't in acceptable musical notename.
	- TypeError('...') : Wrong type of input data.
	"""
	Err=ValueError('Typed musical notename isn\'t supported.')
	if type(notename)!=str: raise TypeError('notename should be str.')
	if notename=='': raise Err
	if notename[0] in ['c','C']: val=0
	elif notename[0] in ['d','D']: val=2
	elif notename[0] in ['e','E']: val=4
	elif notename[0] in ['f','F']: val=5
	elif notename[0] in ['g','G']: val=7
	elif notename[0] in ['a','A']: val=9
	elif notename[0] in ['b','B']: val=11
	else: raise Err
	if notename.__len__()==1: pass
	else:
		acc=notename[1]
		for c in range(0,notename.__len__()-1):
			tmp=notename[c+1]
			if tmp!=acc: raise Err
			if tmp=='#': val+=1
			elif tmp=='b': val-=1
			else: raise Err
	return val%12
def number_to_note_letter(number,accidental='#',Uppercase=True):
	"""
	Read the identification integer of musical notename and return correspond string of musical notename (From 0-11 as C to B).

	Required keyword arguments:
	- number (int) : Identification integer of musical notename.
	- accidental (str) : Select accidental to apply when in need. 'b', '#' are available.
	- Uppercase (bool) : Uppercase the output string.

	Error:
	- ValueError('Typed number is out of range (0-11).') : Inputted integer 'number' is out of range of 0-11.
	- TypeError('...') : Wrong type of input data.
	"""
	if type(number)!=int: raise TypeError('number should be int.')
	if type(Uppercase)!=bool: raise TypeError('Uppercase should be bool.')
	if accidental not in ['b','#']: raise TypeError('accidental should be str of \'b\' or \'#\'.')
	if number==0: letter=['C','C']
	elif number==1: letter=['Db','C#']
	elif number==2: letter=['D','D']
	elif number==3: letter=['Eb','D#']
	elif number==4: letter=['E','E']
	elif number==5: letter=['F','F']
	elif number==6: letter=['Gb','F#']
	elif number==7: letter=['G','G']
	elif number==8: letter=['Ab','G#']
	elif number==9: letter=['A','A']
	elif number==10: letter=['Bb','A#']
	elif number==11: letter=['B','B']
	else: raise ValueError('Typed number is out of range (0-11).')
	if accidental=='b': letter=letter[0]
	elif accidental=='#': letter=letter[1]
	if Uppercase: return letter
	else: return letter.lower()
### End of section

### In progress parts ###
def frequency_to_musical_note(freq):
	if type(freq)!=int and type(freq)!=float: raise TypeError('Frequency should be int or float.')
	if freq<=0: raise ValueError('Frequency should more than 0.')
	d=round(_log2((freq/a4_freq)**12))
	return a4_mnote+d
class MusicalNote():
	@property
	def pitch_letter(self):
		return self._pitch_letter
	@pitch_letter.setter
	def pitch_letter(self,val):
		if type(val)!=str: raise TypeError('Pitch letter should be str.')
		new_pitch_letter=val[0].upper()+val[1:]
		if new_pitch_letter in ['C','D','E','F','G','A','B','Cb','Db','Eb','Fb','Gb','Ab','Bb','C#','D#','E#','F#','G#','A#','B#'] :
			self._pitch_letter=new_pitch_letter
		else: raise ValueError('Typed musical notename isn\'t supported.')
	@property
	def octave_level(self):
		return self._octave_level
	@octave_level.setter
	def octave_level(self,val):
		if type(val)!=int: raise TypeError('Octave level should be int.')
		self._octave_level=val
	def __init__(self,pitch_letter='A',octave_level=4):
		if type(pitch_letter)!=str: raise TypeError('Pitch letter should be str.')
		if type(octave_level)!=int: raise TypeError('Octave level should be int.')
		#
		pitch_letter=pitch_letter[0].upper()+pitch_letter[1:]
		if pitch_letter in ['C','D','E','F','G','A','B','Cb','Db','Eb','Fb','Gb','Ab','Bb','C#','D#','E#','F#','G#','A#','B#'] :
			self._pitch_letter=pitch_letter
		else: raise ValueError('Typed musical notename isn\'t supported.')
		self._octave_level=octave_level
	def __repr__(self):
		return 'MusicalNote(\''+self._pitch_letter+'\','+str(self.octave_level)+')'
	def __str__(self):
		if self.octave_level>=0: return self._pitch_letter+str(self.octave_level)
		else: return self._pitch_letter+'('+str(self.octave_level)+')'
	def __add__(self,another):
		if type(another)!=int: raise TypeError('MusicalNote object can be added/subtracted by only int.')
		pitch_letter=number_to_note_letter((note_letter_to_number(self._pitch_letter)+another)%12)
		octave_level=self._octave_level+((note_letter_to_number(self._pitch_letter)+another)//12)
		return MusicalNote(pitch_letter,octave_level)
	def __sub__(self,another):
		Type=type(another)
		if Type==int: return self.__add__(-another)
		elif Type==MusicalNote:
			octave_level_diff=self.octave_level-another.octave_level
			semitone_diff=note_letter_to_number(self._pitch_letter)-note_letter_to_number(another._pitch_letter)
			return octave_level_diff*12+semitone_diff
		else: raise TypeError('MusicalNote object can be added/subtracted by only int and MusicalNote object.')
	def copy(self):
		return MusicalNote(self._pitch_letter,self._octave_level)
### End of section

# Initialize A4 musical note object
a4_mnote=MusicalNote('A',4)
