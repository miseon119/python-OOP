import datetime
class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


my_date = datetime.date(2016, 7, 12)
print(Employee.is_workday(my_date))
