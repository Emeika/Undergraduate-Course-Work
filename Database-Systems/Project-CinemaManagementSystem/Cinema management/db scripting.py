from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Time, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import CreateTable
import random
from datetime import date, timedelta, time
from faker import Faker
import gender_guesser.detector as gender

fake = Faker()
detector = gender.Detector()

# Create the engine
engine = create_engine('mssql+pyodbc://adpak@BIG-MO-PC/hospital?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')

# Create a base class for declarative models
Base = declarative_base()

# Define the Department table
class Department(Base):
    __tablename__ = 'department'

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    department_name = Column(String(255))

# Define the Doctor table
class Doctor(Base):
    __tablename__ = 'doctor'

    doctor_id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = Column(Integer, ForeignKey('department.department_id'))
    first_name = Column(String(255))
    last_name = Column(String(255))
    date_of_birth = Column(Date)
    gender = Column(String(1))
    contact_number = Column(String(255))

    department = relationship("Department", backref="doctors")

# Define the Nurse table
class Nurse(Base):
    __tablename__ = 'nurse'

    nurse_id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = Column(Integer, ForeignKey('department.department_id'))
    first_name = Column(String(255))
    last_name = Column(String(255))
    date_of_birth = Column(Date)
    gender = Column(String(1))
    contact_number = Column(String(255))

    department = relationship("Department", backref="nurses")

# Define the Janitor table
class Janitor(Base):
    __tablename__ = 'janitor'

    janitor_id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = Column(Integer, ForeignKey('department.department_id'))
    first_name = Column(String(255))
    last_name = Column(String(255))
    date_of_birth = Column(Date)
    gender = Column(String(1))
    contact_number = Column(String(255))

    department = relationship("Department", backref="janitors")

# Define the Patient table
class Patient(Base):
    __tablename__ = 'patient'

    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    date_of_birth = Column(Date)
    gender = Column(String(1))
    address = Column(String(255))
    contact_number = Column(String(255))

# Define the Appointment table
class Appointment(Base):
    __tablename__ = 'appointment'

    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, ForeignKey('doctor.doctor_id'))
    patient_id = Column(Integer, ForeignKey('patient.patient_id'))
    appointment_date = Column(Date)
    appointment_time = Column(Time)
    appointment_reason = Column(String(255))
    amount_of_payment = Column(Integer)  
    mode_of_payment = Column(String(255)) 

    doctor = relationship("Doctor", backref="appointments")
    patient = relationship("Patient", backref="appointments")

# Define the Medical Record table
class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    record_id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, ForeignKey('doctor.doctor_id'))
    patient_id = Column(Integer, ForeignKey('patient.patient_id'))
    record_date = Column(Date)
    diagnosis = Column(String(255))
    treatment = Column(String(255))

    doctor = relationship("Doctor", backref="medical_records")
    patient = relationship("Patient", backref="medical_records")

# Define the Room table
class Room(Base):
    __tablename__ = 'room'

    room_number = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.department_id'))
    room_type = Column(String(255))

    department = relationship("Department", backref="rooms")

# Define the RoomAdmission table
class RoomAdmission(Base):
    __tablename__ = 'room_admission'

    admission_id = Column(Integer, primary_key=True, autoincrement=True)
    room_number = Column(Integer, ForeignKey('room.room_number'))
    patient_id = Column(Integer, ForeignKey('patient.patient_id'))
    admission_date = Column(Date)
    discharge_date = Column(Date)
    amount_of_payment = Column(Integer)  
    mode_of_payment = Column(String(255)) 
    nurse_id = Column(Integer, ForeignKey('nurse.nurse_id'))
    janitor_id = Column(Integer, ForeignKey('janitor.janitor_id'))

    room = relationship("Room", backref="admissions")
    patient = relationship("Patient", backref="room_admissions")
    nurse = relationship("Nurse", backref="room_admissions")
    janitor = relationship("Janitor", backref="room_admissions")

# Define the Ward table
class Ward(Base):
    __tablename__ = 'ward'

    ward_number = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.department_id'))

    department = relationship("Department", backref="wards")

# Define the Bed table
class Bed(Base):
    __tablename__ = 'bed'

    bed_number = Column(Integer, primary_key=True)
    ward_number = Column(Integer, ForeignKey('ward.ward_number'))

    ward = relationship("Ward", backref="beds")

# Define the BedAdmission table
class BedAdmission(Base):
    __tablename__ = 'bed_admission'

    admission_id = Column(Integer, primary_key=True, autoincrement=True)
    bed_number = Column(Integer, ForeignKey('bed.bed_number'))
    patient_id = Column(Integer, ForeignKey('patient.patient_id'))
    admission_date = Column(Date)
    discharge_date = Column(Date)
    amount_of_payment = Column(Integer)  
    mode_of_payment = Column(String(255))
    nurse_id = Column(Integer, ForeignKey('nurse.nurse_id'))
    janitor_id = Column(Integer, ForeignKey('janitor.janitor_id'))

    room = relationship("Bed", backref="admissions")
    patient = relationship("Patient", backref="bed_admissions")
    nurse = relationship("Nurse", backref="bed_admissions")
    #janitor = relationship("Janitor", backref="room_admissions")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Drop existing tables
Base.metadata.drop_all(engine, checkfirst=True)

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Additional objects for each table
departments_data = [
    'Cardiology',
    'Pediatrics',
    'Gynecology',
    'Dermatology',
    'Psychiatry'
]


diagnoses_and_treatments = {
    1: {
        'Hypertension': 'Prescription for blood pressure medication, to be taken daily',
        'Myocardial infarction': 'Immediate hospitalization, aspirin for 30 days, beta-blockers for 1 year',
        'Arrhythmia': 'Anti-arrhythmic medication as needed, duration varies',
        'Congestive heart failure': 'Diuretics, ACE inhibitors, beta-blockers, lifestyle modifications',
        'Hypertension': 'Prescription for blood pressure medication, to be taken daily',
        'Myocardial infarction': 'Immediate hospitalization, aspirin for 30 days, beta-blockers for 1 year',
        'Arrhythmia': 'Anti-arrhythmic medication as needed, duration varies',
        'Arrhythmia': 'Anti-arrhythmic medication as needed, duration varies',
        'Congestive heart failure': 'Diuretics, ACE inhibitors, beta-blockers, lifestyle modifications',
        'Hypertension': 'Prescription for blood pressure medication, to be taken daily',
        'Myocardial infarction': 'Immediate hospitalization, aspirin for 30 days, beta-blockers for 1 year',
        'Arrhythmia': 'Anti-arrhythmic medication as needed, duration varies',
        'Congestive heart failure': 'Diuretics, ACE inhibitors, beta-blockers, lifestyle modifications',
        'Hypertension': 'Prescription for blood pressure medication, to be taken daily',
        'Myocardial infarction': 'Immediate hospitalization, aspirin for 30 days, beta-blockers for 1 year',
        'Arrhythmia': 'Anti-arrhythmic medication as needed, duration varies',
        'Congestive heart failure': 'Diuretics, ACE inhibitors, beta-blockers, lifestyle modifications',
        'Coronary artery disease': 'Antiplatelet agents, statins, angioplasty or bypass surgery if needed',
        'Coronary artery disease': 'Antiplatelet agents, statins, angioplasty or bypass surgery if needed',
        'Angina': 'Nitroglycerin as needed, beta-blockers or calcium channel blockers for 6 months',
        'Valvular heart disease': 'Medication to manage symptoms, surgical repair or replacement if necessary',
        'Cardiomyopathy': 'Medication to manage symptoms, lifestyle changes, heart transplant in severe cases',
        'Atrial fibrillation': 'Anticoagulants, rate or rhythm control medications, cardioversion if needed',
        'Peripheral artery disease': 'Lifestyle modifications, antiplatelet medication, angioplasty or bypass surgery if needed',
        'Heart failure': 'Diuretics, ACE inhibitors, beta-blockers, aldosterone antagonists, lifestyle changes',
        'Mitral valve prolapse': 'Monitoring, lifestyle modifications, medication if necessary',
        'Ventricular septal defect': 'Monitoring, medication if necessary, surgical repair in severe cases',
        'Pulmonary embolism': 'Anticoagulants for 3-6 months, oxygen therapy, thrombolytic therapy in severe cases',
        'Cardiac arrhythmias': 'Medication, pacemaker implantation, catheter ablation if necessary',
        'Pericarditis': 'Nonsteroidal anti-inflammatory drugs (NSAIDs) for 1-2 weeks, rest',
        'Endocarditis': 'Intravenous antibiotics for 4-6 weeks, surgical repair or replacement of damaged valves if necessary',
        'Cardiac tamponade': 'Pericardiocentesis, surgical drainage, treatment of underlying cause',
        'Hypertrophic cardiomyopathy': 'Beta-blockers, calcium channel blockers, surgical myectomy or alcohol septal ablation if necessary',
        'Coronary artery aneurysm': 'Antiplatelet medication, surgical repair if necessary',
    },
    2: {
        'Common cold': 'Symptomatic relief with acetaminophen, rest and hydration',
        'Asthma': 'Inhaled bronchodilators (e.g., albuterol) as needed, long-term controller medications for 6-12 months',
        'Ear infection': 'Antibiotics for 7-10 days, pain relief with acetaminophen or ibuprofen',
        'Chickenpox': 'Symptomatic relief, antiviral medication if severe',
        'Common cold': 'Symptomatic relief with acetaminophen, rest and hydration',
        'Asthma': 'Inhaled bronchodilators (e.g., albuterol) as needed, long-term controller medications for 6-12 months',
        'Common cold': 'Symptomatic relief with acetaminophen, rest and hydration',
        'Asthma': 'Inhaled bronchodilators (e.g., albuterol) as needed, long-term controller medications for 6-12 months',
        'Ear infection': 'Antibiotics for 7-10 days, pain relief with acetaminophen or ibuprofen',
        'Ear infection': 'Antibiotics for 7-10 days, pain relief with acetaminophen or ibuprofen',
        'Chickenpox': 'Symptomatic relief, antiviral medication if severe',
        'Growth and development concerns': 'Nutritional counseling, monitoring, potential referrals',
        'Acute otitis media': 'Antibiotics for 10 days, pain relief with acetaminophen or ibuprofen',
        'Allergies': 'Antihistamines as needed, avoidance of triggers, immunotherapy in severe cases',
        'Croup': 'Cool mist humidifier, steroids as prescribed, breathing treatments as needed',
        'Gastroenteritis': 'Oral rehydration solution, symptomatic relief, rest',
        'Bronchiolitis': 'Supportive care, nasal suctioning, humidified oxygen if necessary',
        'ADHD': 'Behavioral therapy, stimulant medications as prescribed',
        'Allergies': 'Antihistamines as needed, avoidance of triggers, immunotherapy in severe cases',
        'Croup': 'Cool mist humidifier, steroids as prescribed, breathing treatments as needed',
        'Gastroenteritis': 'Oral rehydration solution, symptomatic relief, rest',
        'Bronchiolitis': 'Supportive care, nasal suctioning, humidified oxygen if necessary',
        'ADHD': 'Behavioral therapy, stimulant medications as prescribed',
        'Strep throat': 'Antibiotics for 10 days, pain relief with acetaminophen or ibuprofen',
        'Pneumonia': 'Antibiotics for 7-14 days, rest, hydration, symptom management',
        'Urinary tract infection': 'Antibiotics for 7-14 days, increased fluid intake',
        'Conjunctivitis': 'Antibiotic eye drops or ointment for 7 days, warm compresses, hygiene measures',
        'Hand, foot, and mouth disease': 'Symptomatic relief, rest, hydration',
        'Tonsillitis': 'Pain relief with acetaminophen or ibuprofen, antibiotics for 10 days if bacterial',
        'Gastroesophageal reflux': 'Positioning, smaller and more frequent feedings, medication as prescribed',
        'Kawasaki disease': 'Intravenous immunoglobulin, aspirin for 6-8 weeks, cardiac monitoring',
        'Meningitis': 'Antibiotics for 7-21 days, supportive care, hospitalization',
    },
    3: {
        'Menstrual cramps': 'Over-the-counter pain relievers (e.g., ibuprofen) as needed, rest',
        'Urinary tract infection': 'Antibiotics for 7-10 days, increased fluid intake',
        'Polycystic ovary syndrome': 'Oral contraceptives for 6-12 months, lifestyle changes (e.g., diet, exercise)',
        'Menstrual cramps': 'Over-the-counter pain relievers (e.g., ibuprofen) as needed, rest',
        'Urinary tract infection': 'Antibiotics for 7-10 days, increased fluid intake',
        'Polycystic ovary syndrome': 'Oral contraceptives for 6-12 months, lifestyle changes (e.g., diet, exercise)',
        'Endometriosis': 'Pain medication, hormonal therapy for 3-6 months, laparoscopic surgery if needed',
        'Cervical dysplasia': 'Colposcopy, biopsy, possible excision or cryotherapy',
        'Premenstrual syndrome': 'Lifestyle changes, over-the-counter pain relievers, hormonal birth control',
        'Menopause': 'Hormone replacement therapy, lifestyle modifications, symptom management',
        'Menopause': 'Hormone replacement therapy, lifestyle modifications, symptom management',
        'Pelvic inflammatory disease': 'Antibiotics for 14 days, rest, pain relief, sexual partner treatment',
        'Ovarian cysts': 'Monitoring, pain medication, surgical removal if necessary',
        'Uterine fibroids': 'Monitoring, pain medication, hormone therapy, surgical options if necessary',
        'Vaginal yeast infection': 'Antifungal medication (e.g., clotrimazole) for 7-14 days, hygiene measures',
        'Infertility': 'Fertility testing, medication, assisted reproductive techniques as recommended',
        'Infertility': 'Fertility testing, medication, assisted reproductive techniques as recommended',
        'Ovarian cancer': 'Surgery, chemotherapy, radiation therapy as recommended',
        'Cervical cancer': 'Screening, biopsy, surgery, chemotherapy, radiation therapy as recommended',
        'Menorrhagia': 'Hormonal therapy, nonsteroidal anti-inflammatory drugs (NSAIDs), surgical options',
        'Pelvic organ prolapse': 'Pelvic floor exercises, pessary, surgical repair if necessary',
        'Vulvodynia': 'Pain management, topical creams, pelvic floor physical therapy',
        'Gestational diabetes': 'Dietary changes, blood sugar monitoring, insulin if necessary',
        'Ectopic pregnancy': 'Medical management or surgery, depending on the situation',
        'Sexually transmitted infections': 'Antibiotics, partner notification and treatment, prevention counseling',
        'Sexually transmitted infections': 'Antibiotics, partner notification and treatment, prevention counseling',
    },
    4: {
        'Acne': 'Topical retinoids, benzoyl peroxide, or antibiotics for 6-12 weeks, duration varies',
        'Acne': 'Topical retinoids, benzoyl peroxide, or antibiotics for 6-12 weeks, duration varies',
        'Eczema': 'Topical corticosteroids, moisturizers, avoidance of triggers',
        'Eczema': 'Topical corticosteroids, moisturizers, avoidance of triggers',
        'Scabies': 'Topical scabicidal medication, washing of clothes and bedding, duration varies',
        'Psoriasis': 'Topical corticosteroids, phototherapy, systemic medications for severe cases',
        'Skin infections': 'Topical or oral antibiotics, antifungal medications as appropriate, duration varies',
        'Skin cancer': 'Surgical excision, radiation therapy, chemotherapy if needed',
        'Rosacea': 'Topical or oral antibiotics, gentle skincare, avoidance of triggers',
        'Contact dermatitis': 'Avoidance of allergens, topical corticosteroids, antihistamines',
        'Hives': 'Antihistamines, avoidance of triggers, identification and treatment of underlying cause',
        'Vitiligo': 'Topical corticosteroids, topical calcineurin inhibitors, phototherapy',
        'Hair loss (alopecia)': 'Topical minoxidil, oral medications (e.g., finasteride) for several months, hair transplantation if necessary',
        'Nail fungus': 'Antifungal medication (e.g., terbinafine), topical treatments, duration varies',
        'Warts': 'Cryotherapy, topical medications, laser treatment, surgical removal',
        'Herpes simplex': 'Antiviral medication (e.g., acyclovir) for 7-10 days, symptom management, prevention counseling',
        'Fungal infections': 'Antifungal medication (e.g., clotrimazole, ketoconazole), topical treatments',
        'Melasma': 'Topical depigmenting agents, sun protection, chemical peels',
        'Scabies': 'Topical scabicidal medication, washing of clothes and bedding, duration varies',
        'Scabies': 'Topical scabicidal medication, washing of clothes and bedding, duration varies',
        'Cellulitis': 'Antibiotics for 7-14 days, elevation of affected area, rest',
        'Seborrheic dermatitis': 'Topical antifungal or corticosteroid medications, gentle cleansing',
        'Lupus erythematosus': 'Topical corticosteroids, antimalarial medications, immunosuppressive therapy',
        'Molluscum contagiosum': 'Topical treatments, cryotherapy, immune response modifiers, duration varies',
    },
    5: {
        'Depression': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy',
        'Anxiety disorder': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy',
        'Bipolar disorder': 'Mood stabilizers (e.g., lithium) for long-term management, antipsychotics as needed',
        'Schizophrenia': 'Antipsychotic medications for long-term management, therapy, support services',
        'Depression': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy',
        'Anxiety disorder': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy',
        'Bipolar disorder': 'Mood stabilizers (e.g., lithium) for long-term management, antipsychotics as needed',
        'Obsessive-compulsive disorder': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy, exposure and response prevention',
        'Obsessive-compulsive disorder': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy, exposure and response prevention',
        'Obsessive-compulsive disorder': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy, exposure and response prevention',
        'Attention deficit hyperactivity disorder': 'Stimulant medications for 6-12 months, behavioral therapy',
        'Post-traumatic stress disorder': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy, trauma-focused therapy',
        'Eating disorders': 'Psychotherapy, nutritional counseling, medication if necessary',
        'Substance abuse': 'Detoxification, rehabilitation, counseling, support groups',
        'Autism spectrum disorder': 'Behavioral therapy, social skills training, educational support',
        'Panic disorder': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy, relaxation techniques',
        'Borderline personality disorder': 'Dialectical behavior therapy, medication if necessary, support services',
        'Borderline personality disorder': 'Dialectical behavior therapy, medication if necessary, support services',
        'Borderline personality disorder': 'Dialectical behavior therapy, medication if necessary, support services',
        'Alzheimers disease': 'Cholinesterase inhibitors for symptom management, memantine, supportive care',
        'Insomnia': 'Sleep hygiene practices, cognitive-behavioral therapy for insomnia, medication if necessary',
        'Insomnia': 'Sleep hygiene practices, cognitive-behavioral therapy for insomnia, medication if necessary',
        'Schizoaffective disorder': 'Mood stabilizers, antipsychotics, therapy, support services',
        'Social anxiety disorder': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy, exposure therapy',
        'Antisocial personality disorder': 'Psychotherapy, support services, social skills training',
        'Narcissistic personality disorder': 'Psychotherapy, support services, self-reflection',
        'Generalized anxiety disorder': 'Selective serotonin reuptake inhibitors (SSRIs) for 6-12 months, therapy, relaxation techniques',
    }
}

doctors_data = []

for i in range(80):
    name = fake.name().split()
    gender = detector.get_gender(name[0])
    fake_date = fake.date_between(start_date='-80y', end_date='-25y')
    dic = {"male":"M", "female":"F", "mostly_female": "F", "mostly_male": "M"}
    if gender not in dic:
        continue
    
    doctors_data.append([name[0], name[1], f"{fake_date}", dic[gender]])

nurses_data = []

for i in range(150):
    nurse_name = fake.name().split()
    nurse_gender = detector.get_gender(nurse_name[0])
    nurse_fake_date = fake.date_between(start_date='-80y', end_date='-18y')
    dic = {"male":"M", "female":"F", "mostly_female": "F", "mostly_male": "M"}
    if nurse_gender not in dic:
        continue
    
    nurses_data.append([nurse_name[0], nurse_name[1], f"{nurse_fake_date}", dic[nurse_gender]])

janitors_data = []

for i in range(150):
    janitor_name = fake.name().split()
    janitor_gender = detector.get_gender(name[0])
    janitor_fake_date = fake.date_between(start_date='-70y', end_date='-18y')
    dic = {"male":"M", "female":"F", "mostly_female": "F", "mostly_male": "M"}
    if janitor_gender not in dic:
        continue
    
    janitors_data.append([janitor_name[0], janitor_name[1], f"{janitor_fake_date}", dic[janitor_gender]])

patients_data = []

for i in range(400):
    name = fake.name().split()
    gender = detector.get_gender(name[0])
    fake_date = fake.date_between(start_date='-80y', end_date='-18y')
    dic = {"male":"M", "female":"F", "mostly_female": "F", "mostly_male": "M"}
    if gender not in dic:
        continue
    
    patients_data.append([name[0], name[1], f"{fake_date}", dic[gender]])


# Generating random addresses for patients
addresses = [
    'Elm St', 'Oak St', 'Pine St', 'Maple St', 'Cedar St',
    'Birch St', 'Willow St', 'Hickory St', 'Chestnut St', 'Magnolia St',
    'Juniper St', 'Sycamore St', 'Poplar St', 'Ash St', 'Mulberry St',
    'Spruce St', 'Cypress St', 'Beech St', 'Walnut St', 'Cherry St',
    'Rose St', 'Vine St', 'Ivy St', 'Fern St', 'Lily St',
    'Daisy St', 'Tulip St', 'Orchid St', 'Jasmine St', 'Lotus St',
    'Sunflower St', 'Daffodil St', 'Carnation St', 'Peony St', 'Marigold St',
    'Cactus St', 'Palm St', 'Olive St', 'Magnolia St', 'Magnolia St',
    'Camellia St', 'Zinnia St', 'Dahlia St', 'Carnation St', 'Tulip St',
    'Lavender St', 'Hyacinth St', 'Azalea St', 'Primrose St', 'Bluebell St',
    'Snowdrop St', 'Forget-Me-Not St', 'Hibiscus St', 'Mimosa St', 'Wisteria St'
]

for patient in patients_data:
    patient.append(f"{random.randint(0, 999)} {random.choice(addresses)}")

# Generating random phone numbers
numbers = random.sample(range(1000000000, 9999999999), len(doctors_data)+len(patients_data))

for i in range(len(doctors_data)+len(patients_data)):
    if i < len(doctors_data):
        doctors_data[i].append(str(numbers[i]))

    else:
        patients_data[len(doctors_data)-i].append(str(numbers[i]))

for i in range(len(nurses_data)+len(janitors_data)):
    if i < len(nurses_data):
        nurses_data[i].append(str(numbers[i]))

    else:
        janitors_data[len(nurses_data)-i].append(str(numbers[i]))

# Add Department objects
departments = [Department(department_name=name) for name in departments_data]
session.add_all(departments)

# Add Doctor objects
doctors = []

for doctor in doctors_data:
    doctors.append(Doctor(department=random.choice(departments), first_name=doctor[0], last_name=doctor[1], date_of_birth=doctor[2], gender=doctor[3], contact_number=doctor[4]))

session.add_all(doctors)

# Add Nurses objects
nurses = []

for nurse in nurses_data:
    nurses.append(Nurse(department=random.choice(departments), first_name=nurse[0], last_name=nurse[1], date_of_birth=nurse[2], gender=nurse[3], contact_number=nurse[4]))

session.add_all(nurses)

# Add Nurses objects
janitors = []

for janitor in janitors_data:
    janitors.append(Janitor(department=random.choice(departments), first_name=janitor[0], last_name=janitor[1], date_of_birth=janitor[2], gender=janitor[3], contact_number=janitor[4]))

session.add_all(janitors)

# Add Patient objects
patients = [Patient(first_name=data[0], last_name=data[1], date_of_birth=data[2], gender=data[3], address=data[4], contact_number=data[5]) for data in patients_data]
session.add_all(patients)

# Adding Room objects
rooms = []
for number in range(1, 201):
    for department_id in range(1, len(departments)+1):
        if number < 10:
            room_number = int(f"{department_id}00{number}")
        
        elif number < 100:
            room_number = int(f"{department_id}0{number}")

        else:
            room_number = int(f"{department_id}{number}")

        room_type = random.choice(["Standard", "Standard", "Premium"])
        rooms.append(Room(room_number=room_number, department_id=department_id, room_type=room_type))

session.add_all(rooms)

# Add ward objects
wards = []
for number in range(1, 3):
    for department_id in range(1, len(departments)+1):
        ward_number = int(f"{department_id}{number}")
        wards.append(Ward(ward_number=ward_number, department_id=department_id))

session.add_all(wards)

# Add bed objects
beds = []
for number in range(1, 81):
    for ward in wards:
        if number < 10:
            bed_number = int(f"{ward.ward_number}0{number}")
        
        else:
            bed_number = int(f"{ward.ward_number}{number}")

        beds.append(Bed(bed_number=bed_number, ward_number=ward.ward_number))

session.add_all(beds)
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Simulation
appointments = []
medical_records = []
room_admissions = []
bed_admissions = []

# Range of available dates
available_dates = [date(2023, 6, 15) + timedelta(days=i) for i in range(30)]
available_slots = [time(9), time(10), time(11), time(12), time(13)]
modes = ["Cash", "Card", "Card", "Card"]
charges = {"Premium": 300, "Standard": 200}

odds = {1: [True*5 + False*2],
        2: [True*5 + False*2],
        3: [True*4 + False*3],
        4: [True*2 + False*5],
        5: [True, False]}

# Generate appointments for each day
for appointment_date in available_dates:

    # Generate appointments for each doctor
    for doctor in doctors:
        prices = {"Checkup": 10*(random.randint(80, 120)//10), "Follow-up": 10*(random.randint(30, 50)//10), "Consultation": 10*(random.randint(130, 180)//10)}

        # Checking against each time slot
        for i in range(len(available_slots)):
            appointment_time = random.choice(available_slots)

            # Checking if the exact appointment already exists
            existing_appointments = [appointment for appointment in appointments if
                            appointment.doctor_id == doctor.doctor_id and
                            appointment.appointment_date == appointment_date and
                            appointment.appointment_time == appointment_time]
            
            # Check doctor and patient availability and check if the doctor already has appointments at the chosen time
            if (appointment_date.weekday() < 5) and (not existing_appointments):  # Assuming doctors work on weekdays
                # Select a random patient for the appointment
                patient = random.choice(session.query(Patient).all())
                is_admitted = False

                # If patient is currently admitted in room, move forward
                for admission in room_admissions:
                    if (admission.patient_id == patient.patient_id) and (appointment_date <= admission.discharge_date):
                        is_admitted = True
                        break

                # If patient is currently admitted in ward, move forward
                for admission in bed_admissions:
                    if (admission.patient_id == patient.patient_id) and (appointment_date <= admission.discharge_date):
                        is_admitted = True
                        break

                if is_admitted:
                    continue

                # Ensuring female patients in Gynecology
                if doctor.department_id == 3:    
                    if patient.gender != "F":
                        continue

                # Assign a random appointment reason
                appointment_reasons = ["Checkup", "Checkup", "Checkup", "Follow-up", "Follow-up", "Consultation"]
                appointment_reason = random.choice(appointment_reasons)

                # Determining mode and amount of payment
                amount = prices[appointment_reason]
                mode = random.choice(modes)
                
                # Add the appointment to the list
                appointments.append(Appointment(doctor_id=doctor.doctor_id, patient_id=patient.patient_id,
                                                appointment_date=appointment_date, appointment_time=appointment_time,
                                                appointment_reason=appointment_reason, amount_of_payment=amount,
                                                mode_of_payment=mode))
                
                # Adding medical records
                diagnosis = random.choice(list(diagnoses_and_treatments[doctor.department_id].keys()))
                treatment = diagnoses_and_treatments[doctor.department_id][diagnosis]

                # Check if a medical record already exists for the patient-doctor pair
                existing_medical_record = session.query(MedicalRecord).filter_by(doctor_id=doctor.doctor_id, patient_id=patient.patient_id).first()

                if existing_medical_record:
                    # Update the existing medical record with new diagnosis and treatment
                    existing_medical_record.diagnosis = diagnosis
                    existing_medical_record.treatment = treatment

                else:
                    # Create a new medical record
                    medical_record = MedicalRecord(doctor_id=doctor.doctor_id, patient_id=patient.patient_id,
                                                   record_date=appointment_date ,diagnosis=diagnosis, treatment=treatment)
                    session.merge(medical_record)
            
                existing_admission = [admission for admission in room_admissions if
                            admission.patient_id == patient.patient_id and
                            admission.admission_date == appointment_date]
                
                existing_admission += [admission for admission in bed_admissions if
                            admission.patient_id == patient.patient_id and
                            admission.admission_date == appointment_date]
                
                # Simulating bed and room admissions
                if (appointment_reason in appointment_reasons[3:]) and (random.choice(odds[doctor.department_id])) and (not existing_admission):
                    room_or_bed = random.choice(["Room", "Bed"])

                    if room_or_bed == "Room":
                        desired_room = int(f"{doctor.department_id}001")

                        for room in [r for r in rooms if r.department_id == doctor.department_id]:
                            if (room.room_number == desired_room) and room.room_number not in [r.room_number for r in room_admissions]:
                                days = random.choice([1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10])
                                charge = charges[room.room_type] * days

                                room_admissions.append(RoomAdmission(room_number=desired_room, patient_id=patient.patient_id,
                                                    admission_date=appointment_date,
                                                    discharge_date=appointment_date + timedelta(days=days),
                                                    amount_of_payment=charge, mode_of_payment=mode,
                                                    nurse_id=random.choice([nurse.nurse_id for nurse in nurses if nurse.department_id == doctor.department_id]),
                                                    janitor_id=random.choice([janitor.janitor_id for janitor in janitors if janitor.department_id == doctor.department_id])))
                            
                                break

                            else:
                                desired_room += 1

                    else:
                        random_ward = random.choice([ward.ward_number for ward in wards if ward.department_id == doctor.department_id])
                        desired_bed = int(f"{random_ward}01")

                        for bed in [b for b in beds if b.ward_number == random_ward]:
                            if (bed.bed_number == desired_bed) and bed.bed_number not in [b.bed_number for b in bed_admissions]:
                                days = random.choice([1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10])
                                charge = 100 * days

                                bed_admissions.append(BedAdmission(bed_number=desired_bed, patient_id=patient.patient_id,
                                                    admission_date=appointment_date,
                                                    discharge_date=appointment_date + timedelta(days=days),
                                                    amount_of_payment=charge, mode_of_payment=mode,
                                                    nurse_id=random.choice([nurse.nurse_id for nurse in nurses if nurse.department_id == doctor.department_id]),
                                                    janitor_id=random.choice([janitor.janitor_id for janitor in janitors if janitor.department_id == doctor.department_id])))
                                break

                            else:
                                desired_bed += 1

                    
# Add all the generated data to the session and commit
session.add_all(appointments)
session.add_all(medical_records)
session.add_all(room_admissions)
session.add_all(bed_admissions)

# Commit changes to db
session.commit()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Retrieve the create table statements
create_statements = []
for table_name, table_obj in Base.metadata.tables.items():
    create_statement = CreateTable(table_obj)
    create_statements.append(str(create_statement))

# Retrieve the insert statements
insert_statements = []
with engine.connect() as connection:
    inspector = inspect(engine)
    for table_name in inspector.get_table_names():
        select_statement = f"SELECT * FROM {table_name}"
        result = connection.execute(select_statement)

        for row in result:
            values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in row])
            insert_statement = f"INSERT INTO {table_name} VALUES ({values});"
            insert_statements.append(insert_statement)


# Define the order of tables for insert statements
table_order = ['department', 'patient', 'doctor', 'nurse', 'janitor', 'appointment', 'medical_records', 'room', 'room_admission', 'ward', 'bed', 'bed_admission']

# Write the create table statements to a file
with open('sql_output.txt', 'w') as file:
    for create_statement in create_statements:
        file.write(create_statement + "\n")

    file.write("\n")

    # Write the insert statements of tables in the specified order
    for table_name in table_order:
        # Find the insert statements for the current table
        table_insert_statements = [stmt for stmt in insert_statements if stmt.startswith(f"INSERT INTO {table_name}")]

        if table_insert_statements:
            for insert_statement in table_insert_statements:
                # Split the insert statement into table name and values
                table_name, values = insert_statement.split("VALUES ")

                # Split the values into individual attributes
                attributes = values.strip("();").split(", ")

                # Iterate over the attributes and add quotation marks around date fields
                for i, attribute in enumerate(attributes):
                    if attribute.startswith("'") and attribute.endswith("'"):
                        # Skip if the attribute already has quotation marks
                        continue
                    elif attribute.isdigit():
                        # Skip if the attribute is a numeric value
                        continue

                    # First 5 tables
                    elif ("-" in attribute or ":" in attribute) and (table_name.split()[-1] in table_order[:5]):
                        # Add quotation marks around fields
                        attributes[i] = f"'{attribute}'"

                    # Appointments table
                    elif ("-" in attribute or ":" in attribute) and (table_name.split()[-1] == table_order[5]) and (attribute in attributes[3:5]):
                        # Add quotation marks around fields
                        attributes[i] = f"'{attribute}'"
                    
                    # Medical Records table
                    elif ("-" in attribute) and (table_name.split()[-1] == table_order[6]) and (attribute == attributes[3]):
                        # Add quotation marks around fields
                        attributes[i] = f"'{attribute}'"

                    # Room admissions table
                    elif ("-" in attribute) and (table_name.split()[-1] == table_order[8]):
                        # Add quotation marks around fields
                        attributes[i] = f"'{attribute}'"

                    # Bed admissions table
                    elif ("-" in attribute) and (table_name.split()[-1] == table_order[11]):
                        # Add quotation marks around fields
                        attributes[i] = f"'{attribute}'"

                # Reconstruct the modified insert statement
                modified_insert_statement = f"{table_name}VALUES ({', '.join(attributes)});"

                file.write(modified_insert_statement + "\n")
            file.write("\n")

print("SQL statements written to sql_output.txt file.")
