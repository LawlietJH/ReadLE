
import json
import os

class RLE:
	
	def __init__(self, coms=[], x=0, y=0, rule='', rle='', indent=4):
		self.coms = coms
		self.x    = x
		self.y    = y
		self.rule = rule
		self.rle  = rle
		self.fname = ''
		self.fcont = ''
		self.indent = indent
	
	@property
	def data(self):
		return {
			'#':    self.coms,
			'x':    self.x,
			'y':    self.y,
			'rule': self.rule,
			'rle':  self.rle,
		}
	
	@property
	def json(self):
		return json.dumps(self.data, indent=self.indent)
	
	def __str__(self):
		return self.json
	
	def __repr__(self):
		return self.json
	
	def __getitem__(self, args):
		if args.__class__ == tuple:
			out = []
			for arg in args:
				val = self.data[arg]
				out.append(val)
		else:
			out = self.data[args]
		return out

def readRLE(data):
	rle = RLE()
	if data.endswith('.rle'):
		with open(data, 'r') as f:
			rle.fname = data
			rle.fcont = f.read()
	else:
		rle.fcont = data
	content = rle.fcont.split('\n')
	for row in content:
		row = row.strip()
		if len(row) == 0:
			continue
		if row[0] == '#':
			rle.coms.append(row)
		elif row[0] == 'x':
			row = row.split(',')
			for col in row:
				col = col.strip()
				val = col.split(' = ')
				if val[0] == 'x':
					rle.x = int(val[1])
				if val[0] == 'y':
					rle.y = int(val[1])
				else:
					rle.rule = val[1]
		else:
			rle.rle += row
	return rle

def getXY(rle):
	rle = rle.split('$')
	digits = ''
	num = 0
	x = 0
	for row in rle:
		for col in row:
			if col in 'bo1234567890':
				if col.isdigit():
					digits += col
				else:
					if digits:
						num += int(digits)
						digits = ''
					else:
						num += 1
					if num > x:
						x = num
		digits = ''
		num = 0
	return x, len(rle)

def getPattern(rle):
	
	if rle.__class__ == RLE:
		rle, x = rle['rle','x']
	elif rle.__class__ == dict:
		rle = rle['rle']
		x = getXY(rle)[0]
	else:
		x = getXY(rle)[0]
	
	pac = 1
	pdc = 0
	ac = 'o'	# Alive Cell
	dc = 'b'	# Dead Cell
	
	pos = 0
	out = []
	
	while True:
		
		row = []
		
		while not rle[pos] == '$':
			
			let = rle[pos]
			
			if let in [' ','\n','\t','\r']:
				pos += 1
				continue
			
			if let == ac: row.append(pac)
			if let == dc: row.append(pdc)
			
			if let.isdigit():
				
				if rle[pos:pos+4].isdigit():
					num = int(rle[pos:pos+4])
					pos += 4
				elif rle[pos:pos+3].isdigit():
					num = int(rle[pos:pos+3])
					pos += 3
				elif rle[pos:pos+2].isdigit():
					num = int(rle[pos:pos+2])
					pos += 2
				elif rle[pos:pos+1].isdigit():
					num = int(rle[pos:pos+1])
					pos += 1
				else:
					num = int(let)
					pos += 1
				
				let = rle[pos]
				
				for i in range(num):
					if let == ac: row.append(pac)
					if let == dc: row.append(pdc)
			
			if rle[pos+1] == '!':
				break
			pos += 1
		
		if len(row) < x:
			row += [pdc for _ in range(x-len(row))]
		
		out.append(row)
		pos += 1
		
		if rle[pos] == '!':
			break
	
	return out

def setChars(values):
	
	# ~ pac = '[█]'
	pac = '[■]'
	pdc = ' · '
	cac = '[+]'
	cdc = ' + '
	
	out = []
	ly = len(values)
	lx = len(values[0])
	
	for j, row in enumerate(values):
		out.append([])
		for i, col in enumerate(row):
			if j == ly//2 and i == lx//2:
				if col == 1: out[-1].append(cac)
				if col == 0: out[-1].append(cdc)
			else:
				if col == 1: out[-1].append(pac)
				if col == 0: out[-1].append(pdc)
	
	return out

def prettyPat(pattern, clean=False):
	
	pat = setChars(pattern)
	
	print()
	
	for i, row in enumerate(pat):
		
		if not clean:
			print(str(i).rjust(2)+': ', end='')
		
		for j, col in enumerate(row):
			
			print(col, end='')
			
			if not clean:
				if j == len(row)-1:
					i = i - len(pat)//2
					i = str(i)
					if int(i) > 0:
						i = '+'+i
					print(i.rjust(3),end='')
		
		print()
	
	print('    ', end='')
	
	if not clean:
		for i in range(len(row)):
			
			i = i - len(row)//2
			i = str(i)
			if int(i) > 0:
				i = '+'+i
			
			print(i.center(3), end='')
	
	print(f'\n\n x = {len(pat[0])}, y = {len(pat)}')

#=======================================================================
#=======================================================================
#=======================================================================
# Ejecuciones de prueba:
#---------------------------------------

if __name__ == '__main__':
	
	rle = '''
		2o$bo$bobo13b3o$2b2o3bo8bo3bo$6bob2o6bo4bo$5bo4bo6b2obo$
		6bo3bo8bo3b2o$7b3o13bobo$25bo$25b2o!
	'''
	pattern = getPattern(rle)
	prettyPat(pattern)
	
	#---------------------------------------
	
	rle = readRLE('patterns/36p22.rle')
	pattern = getPattern(rle)
	prettyPat(pattern)
	
	#---------------------------------------
	
	rle = readRLE('patterns/36p22.rle')
	pattern = getPattern(rle)
	prettyPat(pattern, clean=True)
	
	#---------------------------------------
	
	rle = readRLE('patterns/36p22.rle')
	pattern = getPattern(rle)
	for p in pattern:
		print(p)
	xy = getXY(rle['rle'])
	print(f'\n x = {xy[0]}, y = {xy[1]}')

#=======================================================================
#=======================================================================
#=======================================================================

desc = '''
https://www.conwaylife.com/wiki/Run_Length_Encoded

Run Length Encoded

The Run Length Encoded (or RLE for short) file format is commonly-used
for storing large patterns. It is more cryptic than some other file
formats such as plaintext and Life 1.06, but is still quite readable.
Many features of the RLE file format are incorporated in the MCell file
format. RLE files are saved with a .rle file extension.

Description of format

The first line is a header line, which has the form

x = m, y = n

where m and n are the width and height of the pattern, respectively.
The pattern itself begins on the next line and is encoded as a sequence
of items of the form <run_count><tag>, where <run_count> is the number
of occurrences of <tag> and <tag> is one of the following three
characters:

<tag>	description
  b		dead cell
  o		alive cell
  $		end of line
  !		end

Examples

The following is a glider in RLE format:

	#C This is a glider.
	x = 3, y = 3
	bo$2bo$3o!
	
How to read:
	
	RLE: bo$2bo$3o! --> bo$, 2bo$, 3o!
	
	bo$  -->  [b, o]    $  --> break ($)
	2bo$ -->  [b, b, o] $  --> break ($)
	3o!  -->  [o, o, o] !  --> End (!)
	
	Visual: x = 3, y = 3
	
	1  ·  ■  ·
	2  ·  ·  ■
	3  ■  ■  ■
	   1  2  3
	

The following is the Gosper glider gun in RLE format:

	#N Gosper glider gun
	#C This was the first gun discovered.
	#C As its name suggests, it was discovered by Bill Gosper.
	x = 36, y = 9, rule = B3/S23
	24bo$22bobo$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o$
	2o8bo3bob2o4bobo$10bo5bo7bo$11bo3bo$12b2o!

'''

#===================================#
# ┌───┬───┐   ╔═══╦═══╗   ▄▄▄▄▄▄▄▄▄ #
# │   │   │   ║   ║   ║   █   █   █ #
# ├───┼───┤   ╠═══╬═══╣   █■■■█■■■█ #
# │   │   │   ║   ║   ║   █   █   █ #
# └───┴───┘   ╚═══╩═══╝   ▀▀▀▀▀▀▀▀▀ #
#===================================#

