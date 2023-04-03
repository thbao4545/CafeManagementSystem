from Staff import Staff
from Deparment import Deparment
from copy import deepcopy

class StaffList:
	def __init__(self, staffNumber = 0, sList = []):
		self.list = sList.copy()
		self.staffNumber = staffNumber

	def print(self):
		for staff in self.list:
			print(staff.getInfo())
	def  getStaffNumber(self): #Get number of staff in list
		return self.staffNumber

	def addStaff(self, staff): #Add a new staff to list
		self.list.append(staff)
		self.staffNumber += 1


	def getByName(self, name): #Get a StaffList with staff with same name with input
		tempList = [staff for staff in self.list if staff.name == name]
		tempNumber = len(tempList)
		return StaffList(tempNumber, tempList)

	def getByID(self, ID):
		findStaff = None
		for staff in self.list:
			if staff.ID == ID:
				findStaff = staff
		return "None" if findStaff == None else deepcopy(findStaff)


if __name__ == '__main__':
	info = dict(ID = 1, name = "Khang", gender = 0, birthday = "28-05-2003", address = "TV", 
				startingDay = "4-2", deparment = Deparment(1, "Moc boc"))
	newInfo = dict(ID = 2, name = "Puken", gender = 0, birthday = "28-05-2003", address = "TV", 
				startingDay = "4-2", deparment = Deparment(1, "Moc boc"))
	newStaff = Staff(info)
	anotherStaff = deepcopy(newStaff)
	anotherStaff.updateInfo(newInfo)

	staffList = StaffList()
	print(staffList.list)
	staffList.addStaff(newStaff)
	staffList.addStaff(anotherStaff)
	print(staffList.list)
	staff = staffList.getByID(1)
	staff.ID = 3
	print(staffList.print())