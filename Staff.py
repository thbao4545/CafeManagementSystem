class Staff:
    def __init__(self, id, name, gender, birthday, address, startday, deparment):
        self.ID = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.address = address
        self.startingDay = startday
        self.deparment = deparment
    
    def get_ID(self):
        return self.ID
        
    def get_name(self):
        return self.name
        
    def get_gender(self):
        return self.gender
        
    def get_birthday(self):
        return self.birthday
        
    def get_address(self):
        return self.address
        
    def get_startingDay(self):
        return self.startingDay
        
    def get_department(self):
        return self.deparment
    def getInfo(self):
        info = dict(ID = self.ID, name = self.name, gender = self.gender, birthday = self.birthday, address = self.address, startingDay = self.startingDay, deparment = deepcopy(self.deparment))
        return info

# if __name__ == '__main__':
	# info = dict(ID = 1, name = "Khang", gender = 0, birthday = "28-05-2003", address = "TV", 
	# 	startingDay = "4-2", deparment = Deparment(1, "Moc boc"))

	# newInfo = dict(ID = 2, name = "Puken", gender = 0, birthday = "28-05-2003", address = "TV", 
	# 	startingDay = "4-2", deparment = Deparment(1, "Moc boc"))
	# newStaff = Staff(info)
	# anotherStaff = deepcopy(newStaff)
	# anotherStaff.updateInfo(newInfo)

	# print(newStaff.getInfo())
	# print(anotherStaff.getInfo())
