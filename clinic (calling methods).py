class Clinic(object):
    
    max_patients = 3
    
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.waiting_list = []
    
    def add_patient(self, patient):
        if len(self.patients) &gt;= Clinic.max_patients:
            self.waiting_list.append(patient)
        else:
            self.patients.append(patient)
            
# Create your instance of Clinic and call the method addPatient below this line

my_clinic = Clinic("Clinic911")

my_clinic.add_patient("Danny")
