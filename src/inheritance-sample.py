class Employee: # parent class
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
	raise_amt = 1.10
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		# Employee.__init__(self, first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())

dev_1 = Developer('Bob', 'King', 50000, 'python')
dev_2 = Developer('Jane', 'Bird', 60000, 'c++')


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.add_emp(dev_2)

mgr_1.print_emps()


# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))

# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Developer))


# print(mgr_1.email)
# print(dev_2.prog_lang)
# print(help(Developer))
