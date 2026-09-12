from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Annotated

class Patient(BaseModel):
    name: str = Field(max_length=10, title="Name of the Patient", description="Add the name of the patient with maximan character length as 10")
    age: Annotated[int, Field(gt=18, title="Age of the Patient")]
    email: str
    weight: float
    allergies: List[str] = Field(default=None, title="Allergies patient suffering from", description="Provide the list of allergies patient is suffering from.")
    contact_details: Dict[str, str]
    married: bool = False

    @field_validator("email")
    @classmethod
    def check_email(cls, value):
        print("From validators: ",value)
        print("From validators: ",cls)

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value

    @field_validator('name')
    @classmethod
    def convert_name(cls, value):
        return value.upper()

def register_patient(patient: Patient) -> None:
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)

pt = {

    "name": "Shanawaz",
    "age" : 28,
    "email": "bahadurshanawaz@hdfc.com",
    "weight": 22,

    "allergies": ["Dizzeness", "Lactose"],
    "contact_details": {
        'email': 'bahadurshanawaz@gmail.com',
        'phoneno': "8356817047"
    },
    "married": True
}

try:
    patient_1 = Patient(**pt)
    print("modeldump",patient_1.model_dump(), type(patient_1.model_dump()))
    print("modeldumpjson",patient_1.model_dump_json(), type(patient_1.model_dump_json()))
    register_patient(patient_1)
except Exception as e:
    print("Exception :", f"{type(e).__name__}: {e}")
