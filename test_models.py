#!/usr/bin/python3

from models import doctor, storage
from models.user import User
from models.patient import Patient
from models.appointment import Appointment

def test_model_creation():
    user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
    user.save()
    print(f"User created: {user}")

    patient = Patient(name="Jane Doe")
    patient.save()
    print(f"Patient created: {patient}")

    appointment = Appointment(procedure="Extraction", status="Ended")
    appointment.save()
    print(f"Appointment created: {appointment}")

    storage.save()

if __name__ == "__main__":
    test_model_creation()
