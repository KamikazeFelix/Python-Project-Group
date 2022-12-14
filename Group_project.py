class Doctor:
    listdoctors =[]

    def __init__(self,ID='',Name='',Speciality='',Timing='',Qualification='',roomNb=''):
        self.ID = ID
        self.Name = Name
        self.Speciality = Speciality
        self.Timing = Timing
        self.Qualification = Qualification
        self.roomNb = roomNb

    def formatDrInfo(self):
        return '{:<5} {:<12} {:<12} {:<10} {:<15} {:<10}'.format(self.ID,self.Name,self.Speciality,self.Timing,self.Qualification,self.roomNb)
    
    def __str__(self):
        format=self.formatDrInfo()
        return format

    def firstLineDisplay(self):
        print("{:<6} {:<12} {:<12} {:<10} {:<15} {:<12}".format(
            'Id',
            'Name',
            'Speciality',
            'Timing',
            'Qualification',
            'Room Number\n'
        ))

    def enterDrInfo(self):
        self.ID = input('Enter the doctor\'s ID:\n')
        self.Name = input('Enter the doctor\'s name:\n')
        self.Speciality = input('Enter the doctor\'s speciality:\n')
        self.Timing = input('Enter the doctor\'s timing (e.g, 7am-10pm):\n')
        self.Qualification = input('Enter the doctor\'s qualification:\n')
        self.roomNb = input('Enter the doctor\'s room number:\n')
        self.listdoctors.append(Doctor(self.ID,self.Name,self.Speciality,self.Timing,self.Qualification,self.roomNb))
        return self.listdoctors
    
    def readDoctorsFile(self):
        f = open('doctors.txt','r')
        lines = f.readlines()
        for line in lines:
            splitline = line.strip().split('_')
            id =  splitline[0]
            Name = splitline[1]
            Speciality =  splitline[2]
            Timing =  splitline[3]
            Qualification =  splitline[4]
            roomNb =  splitline[5]
            doctor = Doctor(id,Name,Speciality,Timing,Qualification,roomNb)
            self.listdoctors.append(doctor)
        return self.listdoctors    
        

    def displayDoctorInfo(self):
        for doctor in self.listdoctors:
            print(doctor,'\n')

    def searchDoctorByID(self):
        i = input('Enter the doctor Id:\n')
        for n in self.listdoctors:
            if i == n.ID:
                Doctor().firstLineDisplay()
                print(n,'\n')
                return
        print('Can\'t find the doctor with the same ID on the system')

    def searchDoctorByName(self):
        i = input('Enter the doctor Name:\n')
        for n in self.listdoctors:
            if i == n.Name:
                Doctor().firstLineDisplay()
                print(n,'\n')
                return
        print('Can\'t find the doctor with the same Name on the system')

    def editDoctorInfo(self):
        i = input('Enter the  ID of  the doctor to change their information:\n')
        name = input('Enter new name:\n')
        spec = input('Enter new specialist in:\n')
        timi = input('Enter new timing:\n')
        qual = input('Enter new qualification:\n')
        room = input('Enter new room number:\n')
        for new in self.listdoctors:
            if i == new.ID:
                new.Name = name 
                new.Specialist = spec
                new.Timing = timi
                new.Qualification = qual
                new.RoomNb  = room
        return self.listdoctors

    def writeListOfDoctorsToFile(self):
        f = open('doctors.txt','w')
        for i in self.listdoctors:
            f.write(i.ID + '_' + i.Name + '_' + i.Speciality + '_' + i.Timing + '_' + i.Qualification + '_' + i.roomNb+"\n")

    def addDrToFile(self):
        f = open('doctors.txt','a')
        i = self.listdoctors[-1]
        f.write('\n' + i.ID + '_' + i.Name + '_' + i.Speciality + '_' + i.Timing + '_' + i.Qualification + '_' + i.roomNb)



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

class Lab:
    lab_list = []
    def __init__(self, lab="", cost="" ):
        self.lab = lab
        self.cost = cost

    def readLaboratoriesFile(self): 
        f = open('laboratories.txt', 'r')
        lines = f.readlines()
        for line in lines:
            splitline = line.split('_')
            Object = Lab(splitline[0], splitline[1])
            self.lab_list.append(Object)
        f.close()


    def writeListOfLabsToFile(self): 
            f = open('laboratories.txt', 'r')
            data = f.read()
            data = data.replace('Facility','Lab')
            f.close()
            f = open('laboratories.txt', 'w')
            f.write(data)
            f.close()

    def displayLabsList(self): 
        for i in range(len(self.lab_list)):
            print("{:<12} {:<12}".format(self.lab_list[i].lab, self.lab_list[i].cost,'\n'))
        print('Back to the prevoius Menu')
        
    def enterLaboratoryInfo(self): 
        add_lab = input('Enter Laboratory facility:\n')
        add_cost = input('Enter Laboratory cost:\n')
        addObject = Lab(add_lab, add_cost)
        self.lab_list.append(addObject)
        return add_lab, add_cost

    def formatDrInfo(self): 
        add = Lab().enterLaboratoryInfo()
        format = ['\n', add[0] ,'_', add[1]]
        return format 

    def addLabToFile(self): 
        f = open('laboratories.txt', 'a')            
        lab_cost =  Lab().formatDrInfo()
        f.write(''.join(lab_cost))
        f.close()
        print('Back to the prevoius Menu')
            
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
          
    def firstLineDisplay2(self):
        print("{:<5} {:<20} {:<15} {:<15} {:<7}".format(
            'id',
            'Name',
            'Disease',
            'Gender',
            'Age\n'
        ))

    def searchPatientById(self):
        patient_id=input("Enter the Patient Id:\n")
        for i in self.patientlist:
            if patient_id == i.pid:
                Patient().firstLineDisplay2()
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

back = "Back to the prevoius Menu \n"
active = True
while active:
    print('Welcome to Alberta Hospital  (AH) Managment system! ')
    choose = input('''Please select from the following options, or select 0 to stop:
                    1 - 	Doctors
                    2 - 	Facilities
                    3 - 	Laboratories
                    4 - 	Patients
                    \n''')
    Doctor().readDoctorsFile()
    if choose == '1':
        
        while True:
            choose1 = input('''Doctors Menu:
                            1 - Display Doctors list
                            2 - Search for doctor by ID
                            3 - Search for doctor by name
                            4 - Add doctor
                            5 - Edit doctor info
                            6 - Back to the Main Menu
                            \n''')
            if choose1 =='1':
                Doctor().displayDoctorInfo()
                print(back)
            elif choose1 == '2':
                Doctor().searchDoctorByID()
                print(back)
            elif choose1 == '3':
                Doctor().searchDoctorByName()
                print(back)
            elif choose1 == '4':
                Doctor().enterDrInfo()
                Doctor().addDrToFile()
                print(back)
            elif choose1 == '5':
                Doctor().editDoctorInfo()
                Doctor().writeListOfDoctorsToFile()
                print(back)
            elif choose1 == '6':
                break
            else:
                print('Please enter a valid number!')
                
            
    elif choose == '2':
        while True:
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
                break
            else:
                print('Please enter a valid number!')
    elif choose == '3':
        Lab().writeListOfLabsToFile()
        Lab().readLaboratoriesFile()
        while True:
            choose3 = input('''Laboratories Menu:
                            1- Display laboratories list
                            2- Add laboratory
                            3- Back to the Main Menu
                            \n''')
            if choose3 == '1':
                Lab().displayLabsList()
            elif choose3 == '2':
                Lab().addLabToFile()
            elif choose3 == '3':
                break
            else:
                print('Please enter a valid number!')
            
    elif choose == '4':
        Patient().readPatientsFile()
        while True:
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
                break
            else:
                print('Please enter a valid number!')

    elif choose == '0':
        active = False
        break

    else:
        print("Enter a valid entry")
        continue
