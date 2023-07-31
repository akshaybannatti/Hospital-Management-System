class Patient:
    def __init__(self, patient_id, name, age, gender, contact):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.appointments = []

class Doctor:
    def __init__(self, doctor_id, name, specialization, contact):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.contact = contact

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.next_patient_id = 1
        self.next_doctor_id = 1
        self.next_appointment_id = 1

    def add_patient(self, name, age, gender, contact):
        patient_id = self.next_patient_id
        patient = Patient(patient_id, name, age, gender, contact)
        self.patients.append(patient)
        self.next_patient_id += 1
        return patient

    def add_doctor(self, name, specialization, contact):
        doctor_id = self.next_doctor_id
        doctor = Doctor(doctor_id, name, specialization, contact)
        self.doctors.append(doctor)
        self.next_doctor_id += 1
        return doctor

    def schedule_appointment(self, patient, doctor, date_time):
        appointment_id = self.next_appointment_id
        appointment = Appointment(appointment_id, patient, doctor, date_time)
        self.appointments.append(appointment)
        patient.appointments.append(appointment)
        doctor.appointments.append(appointment)
        self.next_appointment_id += 1
        return appointment

# Example usage:
hospital = Hospital()

# Adding patients
patient1 = hospital.add_patient("John Doe", 30, "Male", "1234567890")
patient2 = hospital.add_patient("Jane Smith", 25, "Female", "9876543210")
patient3 = hospital.add_patient("Ameya Santosh Gidh", 24, "Male" "0226742474")
patient4 = hospital.add_patient("Vishwanath Jayaraman", 24, "Male", "7854698512")
patient5 = hospital.add_patient("Cole Bloomberg", 25, "male", "8954672453")
patient6 = hospital.add_patient("Neil Chawla", 30, "Male", "5879642259")
patient7 = hospital.add_patient("Victor Domstrang", 18, "Male", "9567842156")
patient8 = hospital.add_patient("Drake Raymond", 22, "Male", "8651478962")
patient9 = hospital.add_patient("Harry Styles", 29, "Male", "9578489251")

# Adding Doctors
doctor1 = hospital.add_doctor("Dr. Steven Smith", "Cardiologist", "1111111111")
doctor2 = hospital.add_doctor("Dr. Johnson Graham", "Dermatologist", "2222222222")
doctor3 = hospital.add_doctor("Dr. William Brown", "Otorhinolaryngologist", "3333333333")
doctor4 = hospital.add_docctor("Dr. Lewis Strauss", "Surgeon", "4444444444")
doctor5 = hospital.add_doctor("Dr. Jay jonah jameson", "Pulmonologist", "5555555555")
doctor6 = hospital.add_doctor("Dr. john raymond", "Endorinologist", "6666666666")
doctor7 = hospital.add_doctor("Dr. Naval vrikranth", "Opthalmologist", "7777777777")
doctor8 = hospital.add_doctor("Dr. Boris johnson", "Neurologist", "8888888888")
doctor9 = hospital.add_doctor("Dr. J. Robert Oppenheimer", "Radiologist", "9999999999")

# Appointments Schedule
hospital.schedule_appointment(patient1, doctor1, "2019-08-10 10:00 AM")
hospital.schedule_appointment(patient2, doctor2, "2019-08-12 3:00 PM")
hospital.schedule_appoitment(patient3, doctor3, "2019-8-01 4:00 PM")