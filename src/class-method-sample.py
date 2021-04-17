class Employee:
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'

		Employee.num_of_emps += 1

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

emp_str_1 = 'Bob-King-40000'
emp_str_2 = 'Jane-Bird-50000'
emp_str_3 = 'Johnson-Magic-60000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)


