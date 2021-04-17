class Employee:
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last):
		self.first = first
		self.last = last

# getter sample
	@property
	def email(self):
		return '{}-{}@email.com'.format(self.first, self.last)
	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)


# setter sample
	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

# deleter sample
	@fullname.deleter
	def fullname(self):
		print('Delete Name!')
		self.first = None
		self.last = None


emp_1 = Employee('Bob', 'King')
emp_1.fullname = 'Jane Bird'
print(emp_1.email)	
print(emp_1.fullname)	

del emp_1.fullname