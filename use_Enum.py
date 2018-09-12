from enum import Enum,unique
class Gender(Enum):
	Male=0
	Female=1
class Student(object):
	def __init__(self,name,gender):
		self.name=name
		self.gender=gender
		
bart=Student('Bart',Gender.Male)
if bart.gender==Gender.Male:
	print('pass_over')
else:
	print('failure')