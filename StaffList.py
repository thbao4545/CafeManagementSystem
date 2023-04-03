from Staff import Staff
from Deparment import Deparment
from copy import deepcopy

class StaffList:
	def __init__(self, staffNumber = 0, sList = []):
		self.list = sList.copy()
		self.staffNumber = staffNumber

	#Method for testing
	
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

	def  getByBirthday(self,birthday):
		tempList = [staff for staff in self.list if staff.birthday == birthday]
		tempNumber = len(tempList)
		return StaffList(tempNumber, tempList)

	def	getByAddress(self,address):
		addresstempList = [staff for staff in self.list if staff.address == address]
		tempNumber = len(tempList)
		return StaffList(tempNumber, tempList)

	def getByID(self, ID):
		findStaff = None
		for staff in self.list:
			if staff.ID == ID:
				findStaff = staff
				break

		return "None" if findStaff == None else findStaff

	def updateStaffInfo(self, ID, info):
		#Return Success neu co staff, nguoc lai return Fail
		staff = self.getByID(ID)
		if (staff == "None"):
			return "Fail"
		staff.updateInfo(info)
		return "Success"

# if __name__ == '__main__':
# 	info = dict(ID = 1, name = "Khang", gender = 0, birthday = "28-05-2003", address = "TV", 
# 				startingDay = "4-2", deparment = Deparment(1, "Moc boc"))
# 	newInfo = dict(ID = 2, name = "Puken", gender = 0, birthday = "28-05-2003", address = "TV", 
# 				startingDay = "4-2", deparment = Deparment(1, "Moc boc"))
# 	newStaff = Staff(info)
# 	anotherStaff = deepcopy(newStaff)
# 	anotherStaff.updateInfo(newInfo)

# 	staffList = StaffList()
# 	print(staffList.print())
# 	# staffList.addStaff(newStaff)
# 	# print(staffList.print())
# 	# staffList.updateStaffInfo(1, newInfo)
# 	# print(staffList.print())
# 	