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

class Doctor:
    Doctors_list = []
    
    def __init__(self, id='', name='', specialization='', workingTime='', qualification='', roomNumber=''):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.workingTime = workingTime
        self.qualification = qualification
        self.roomNumber = roomNumber

    def read_doctors_list(self):
        f = open("doctors.txt","r")
        lines = f.readlines()
        for line in lines:
            x = line.strip().split('_')
            id = x[0]
            name = x[1]
            specialization = x[2]
            workingTime = x[3]
            qualification = x[4]
            roomNumber = x[5]
            doctorObject = Doctor( id, name , specialization , workingTime, qualification, roomNumber )
            self.Doctors_list.append(doctorObject)
        return self.Doctors_list

    def firstLineDisplay(self):
        print("{:<6} {:<12} {:<12} {:<10} {:<15} {:<12}".format(
            'Id',
            'Name',
            'Speciality',
            'Timing',
            'Qualification',
            'Room Number'
        ))

    def displaydoctorInfo(self):
        # for i in range(len(self.Doctors_list)):
        #     line = '{:<15} {:<15} {:<15} {:<20} {:<15} {:<15}'.format(self.Doctors_list[i].id , self.Doctors_list[i].name , self.Doctors_list[i].specialization , self.Doctors_list[i].workingTime, self.Doctors_list[i].qualification , self.Doctors_list[i].roomNumber)
        #     print(line)
        for doctor in self.Doctors_list:
            print(doctor)

    def formatDoctorInfo(self):
        return '{:<6} {:<12} {:<12} {:<10} {:<15} {:<12}'.format (self.id , self.name, self.specialization , self.workingTime , self.qualification, self.roomNumber)

    def __str__(self):
        format = self.formatDoctorInfo()
        return format
    def searchDoctorById(self):
        doctor_id = input("enter the Id to search for the doctor \n")
        # id: 23 but self.Doctors_list[0] => Doctor().id != 23
        Doctor().firstLineDisplay()
        for doctor in self.Doctors_list:
            #print(doctor.id + doctor.name)
            # check if doctor.id equal to given id or not
                #if yes we found
            # if not just continue until found or not found
            if doctor_id != doctor.id:
                None
            else:
                # object ='{:<6} {:<12} {:<12} {:<10} {:<15} {:<12}'.format (doctor.id , doctor.name, doctor.specialization , doctor.workingTime , doctor.qualification, doctor.roomNumber)
                print(doctor)
    
    def searchDoctorByName(self):
        doctor_name = input('enter the name to search for the doctor \n')
        Doctor().firstLineDisplay()
        for doctor in self.Doctors_list:
            if doctor.name != doctor_name:
                object = None
            else:
                object = '{:<6} {:<12} {:<12} {:<10} {:<15} {:<12}'.format(doctor.id ,doctor.name, doctor.specialization , doctor.workingTime , doctor.qualification , doctor.roomNumber)
                print(object)

        if object == None :
            print('Dr. name does not exist, make sure there is no space in doctors name')

    def enterDrInfo(self):
        id = input('Enter the doctor’s ID:\n')
        name = input('Enter the doctor’s name: \n')
        specialization = input('Enter the doctor’s specility:\n ')
        workingTime = input('Enter the doctor’s timing (e.g., 7am-10pm): \n')
        qualification = input("Enter the doctor’s qualification:\n")
        roomNumber = input('Enter the doctor’s room number:\n')
        doctorObject = Doctor(id, name,specialization, workingTime, qualification, roomNumber)
        self.Doctors_list.append(doctorObject)
    
    def addDrToFile(self):
        pass

    def formatDrInfo(self):
        for doctor in self.Doctors_list:
            line_object = f'\n{doctor.id}_{doctor.name}_{doctor.specialization}_{doctor.workingTime}_{doctor.qualification}_{doctor.roomNumber}\n'
            return line_object


    def writeListOfDoctorsToFile(self):
        with open ("doctors.txt","w") as file:
            for doctor in self.Doctors_list:
                file.write(f'{doctor.id}_{doctor.name}_{doctor.specialization}_{doctor.workingTime}_{doctor.qualification}_{doctor.roomNumber}\n')      

    def editDoctorInfo(self):
        id = input("Please enter the id of the doctor that you want to edit their information:\n")   
        for doctor in self.Doctors_list:
            if id != doctor.id:
                line = None

            else:
                new_name = input('please enter new name\n')
                new_spec = input('Enter the doctor’s specility:\n ')
                new_workTime = input('Enter the doctor’s timing (e.g., 7am-10pm): \n')
                new_qualifcation = input("Enter the doctor’s qualification:\n")
                new_roomNumber = input("Enter the doctor’s room number:\n")
                doctor.name = new_name
                doctor.specialization = new_spec
                doctor.workingTime = new_workTime
                doctor.qualification = new_qualifcation
                doctor.roomNumber = new_roomNumber
        return ( doctor.id, doctor.name , doctor.specialization , doctor.workingTime , doctor.qualification, doctor.roomNumber)
                           
class Facilities:
    facilitylist = []
    def __init__(self, facilities=""):
        self.facilities = facilities
    
    def displayFacilities(self):
        f = open('facilities.txt','r')
        lines = f.readlines()
        for line in lines:
            print(line)
        f.close()
        print('\nBack to the previous menu')

    def addFacility(self):
        add_facility = input('Enter facility name:\n') 
        self.facilitylist.append(add_facility) 
          
    def writeListOffacilitiesToFile(self):
        f = open('facilities.txt','a')
        for facilityadd in self.facilitylist:
            f.write('\n'+facilityadd)
        f.close()
        print('Back to the previous menu')

class Patient:
    patientlist=[]
    def __init__(self='', pid='', name='',disease='',gender='',age=''):
        self.pid=pid
        self.name=name
        self.disease=disease
        self.gender=gender
        self.age=age
        
    def formatPatientInfo(self):
        return "{:<5} {:<20} {:<15} {:<15} {:<7}".format(self.pid,self.name,self.disease,self.gender,self.age)
    
    def __str__(self):
        format=self.formatPatientInfo()
        return format  
              
    
    def readPatientsFile(self):
        f=open("patients.txt", "r")
        for x in f:
            self.patient_info = x.strip().split("_")
            self.patientlist.append(Patient(
                self.patient_info[0],
                self.patient_info[1],
                self.patient_info[2],
                self.patient_info[3],
                self.patient_info[4]))
        return self.patientlist

    def displayPatientsList(self):
        for i in self.patientlist:
            print(f"{i}\n")

    def searchPatientById(self):
        patient_id=input("Enter the Patient Id:\n")
        for i in self.patientlist:
            if patient_id == i.pid:
                return print(f"{i}\n")
        return print("Can't find the Patient with the same id on the system\n")  

    def enterPatientInfo(self):
        pid=input("Enter Patient id: ")
        name=input("Enter Patient name: ")
        disease =input("Enter Patient disease: ")
        gender=input("Enter Patient gender: ")
        age =input("Enter Patient age: ")
        self.patientlist.append(Patient(pid,name,disease,gender,age))
        return self.patientlist
        

    def editPatientInfo(self):
        patient_id=input("Please enter the id of the Patient that you want to edit their information: ")
        name_new=input("Enter new Patient name: ")
        disease_new =input("Enter new Patient disease: ")
        gender_new=input("Enter new Patient gender: ")
        age_new =input("Enter new Patient age: ")
        for i in self.patientlist:
            if i.pid==patient_id:
                i.name=name_new
                i.disease=disease_new
                i.gender=gender_new
                i.age=age_new
        return self.patientlist

    def writeListOfPatientsToFile(self):
        f=open("patients.txt","w")
        for i in self.patientlist:
            f.write(i.pid+"_"+i.name+"_"+i.disease+"_"+i.gender+"_"+i.age+"\n" )
        f=open("patients.txt","r")

    def addPatientToFile(self):
        f=open("patients.txt","a")
        i=self.patientlist[-1]
        f.write(i.pid+"_"+i.name+"_"+i.disease+"_"+i.gender+"_"+i.age+"\n" )


while True :
    print("Welcome to Alberta Hospital (AH) Managment system \n Select from the following options, or select 0 to stop: \n 1 - 	Doctors\n 2 - 	Facilities\n 3 - 	Laboratories \n 4 - 	Patients")
    selection = input("")
    active = True
    Laboratories().readLabsList()
    Doctor().read_doctors_list()
    Patient().readPatientsFile()
    while active:
        if selection == '1':
            doctors_menu = input("Doctors Menu:\n 1 - Display Doctors list \n 2 - Search for doctor by ID \n 3 - Search for doctor by name \n 4 - Add doctor \n 5 - Edit doctor info \n 6 - Back to the Main Menu\n")
            if doctors_menu == '1':

                Doctor().displaydoctorInfo()
                print('Back to previous menu')
                continue
            elif doctors_menu == '2':

                Doctor().searchDoctorById()
                print('Back to previous menu')
            elif doctors_menu == '3':
                Doctor().searchDoctorByName()
                print('Back to previous menu')
            elif doctors_menu =='4':
                Doctor().enterDrInfo()
                Doctor().writeListOfDoctorsToFile()
            elif doctors_menu == '5':
        
                Doctor().editDoctorInfo()
                Doctor().writeListOfDoctorsToFile()
            elif doctors_menu == '6':
                # active = False
                break
            else:
                print("Please enter a valid option")
                continue

        if selection == '2':
            while active:
                choose2 = input('''Facilities Menu:
                                    1 - Display Facilities list
                                    2 - Add Facility
                                    3 - Back to the Main Menu
                                    \n''')
                if choose2 == '1':
                    Facilities().displayFacilities()
                elif choose2 == '2':
                    Facilities().addFacility() 
                    Facilities().writeListOffacilitiesToFile()
                elif choose2 == '3':
                    active = False
                    break
                else:
                    print("Please enter a valid option")
                    continue

        if selection == '3':
            while active:
                lab_menu = input("Laboratories Menu:\n 1 - Display laboratories list\n 2 - Add laboratory\n 3 - Back to the Main Menu \n")
                if lab_menu == '1':
                    Laboratories().displayLabsList()
                    print('Back to the prevoius Menu')
                if lab_menu == '2':
                    Laboratories().enterLaboratoryInfo()
                    Laboratories().writeListOfLabsToFile()
                    print('Back to the prevoius Menu')
                elif lab_menu == '3':
                    active = False
                    break
                else:
                    print("Please enter a valid option")
                    continue

        if selection == '4':
            while active:
                choose4 = input('''Patients Menu:
                                    1 - Display patients list
                                    2 - Search for patient by ID
                                    3 - Add patient
                                    4 - Edit patient info
                                    5 - Back to the Main Menu
                                    \n''')
                if choose4 == '1':
                    Patient().displayPatientsList()
                    print("Back to the prevoius Menu")
                elif choose4 == "2":
                    Patient().searchPatientById()
                    print("Back to the prevoius Menu")
                elif choose4 == "3":
                    Patient().enterPatientInfo()
                    Patient().addPatientToFile()
                    print("Back to the prevoius Menu")
                elif choose4 == "4":
                    Patient().editPatientInfo()
                    Patient().writeListOfPatientsToFile()
                    print("Back to the prevoius Menu")
                elif choose4 == '5':
                    active = False
                    break
                else:
                    print('Please enter a valid number!')
                    continue