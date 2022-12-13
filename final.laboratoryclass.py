class Laboratories:
    lab_list = []
    def __init__(self, name="", cost=""):
        self.name = name
        self.cost = cost

    def readLabsList(self):
        self.lab_list.clear()
        with open ('laboratories.txt','r') as file:
            while True:    
                line = file.readline()
                if not line:
                    break
                x = line.strip().split('_')
                name = x[0]
                cost = x[1]
                laboratoryObject = Laboratories(name,cost)
                self.lab_list.append(laboratoryObject)
                
        return(self.lab_list)

    def displayLabsList(self):
        for i in range(len(self.lab_list)):
            line ='{:<12}{:<12}'.format (self.lab_list[i].name , self.lab_list[i].cost )
            print(line)

    def formatDrInfo(self):
        object = f'{self.name}_{self.cost} \n'
        return object

    def addLabToFile(self):
        self.enterLaboratoryInfo()
        file = open ("laboratories.txt","w")
        for object in self.lab_list:
            file.write(object.formatDrInfo())

    def writeListOfLabsToFile(self):
        with open("laboratories.txt","w") as file:
            for i in self.lab_list:
                file.write((i).formatDrInfo())

    def enterLaboratoryInfo(self):
        lab_name = input('enter the lab name\n')
        lab_cost = input('enter the lab cost \n')
        object = Laboratories(lab_name, lab_cost)
        self.lab_list.append(object)


while True :
    print("Welcome to Alberta Hospital (AH) Managment system \n Select from the following options, or select 0 to stop: \n 1 - 	Doctors\n 2 - 	Facilities\n 3 - 	Laboratories \n 4 - 	Patients")
    selection = input("")
    active = True
    Laboratories().readLabsList()
    
    while active:
        if selection == '3':
            lab_menu = input("Laboratories Menu:\n 1 - Display laboratories list\n 2 - Add laboratory\n 3 - Back to the Main Menu ")
            if lab_menu == '1':
                Laboratories().displayLabsList()
                print('Back to the prevoius Menu')
            if lab_menu == '2':
                Laboratories().enterLaboratoryInfo()
                Laboratories().writeListOfLabsToFile()
                print('Back to the prevoius Menu')
            elif lab_menu == '3':
                active = False