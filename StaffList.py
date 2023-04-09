from Staff import Staff
from copy import deepcopy

class StaffList:
	def __init__(self, staffNumber = 0, sList = []):
		self.list = sList.copy()
		self.staffNumber = staffNumber

	#Method for testing
	
	def addStaff(self, id, name, gender, birthday, address, startday, deparment): #Add a new staff to list
		a = Staff(id, name, gender, birthday, address, startday, deparment)
		self.list.append(a)
		self.staffNumber += 1
	def remove_nhanvien(self,id):
		for i in self.list :
			if i.get_ID() == id :
				self.list.remove(i)

	def  getStaffNumber(self): #Get number of staff in list
		return self.staffNumber

	def getByName(self, name): #Get a StaffList with staff with same name with input
		a = []
		for i in self.list :
			if str(name) in i.get_name() :
				a.append(i)
		return StaffList(0,a)

	def  getByBirthday(self,birthday):
		a = []
		for i in self.list :
			if str(birthday) in i.get_birthday():
				a.append(i)
		return StaffList(0,a)

	def	getByAddress(self,address):
		a = []
		for i in self.list :
			if str(address) in i.get_address():
				a.append(i)
		return StaffList(0,a)

	def getByID(self, ID):
		a = []
		for i in self.list :
			if ID == i.get_ID():
				a.append(i)
		return StaffList(0,a)

	def sort_id(self) :
		for i in range(0,len(self.list)) :
			x = self.list[i].get_ID()
			for j in range (i + 1, len(self.list)) :
				y = self.list[j].get_ID()
				if x > y :
					s = self.list[i]
					self.list[i] = self.list[j]
					self.list[j] = s


