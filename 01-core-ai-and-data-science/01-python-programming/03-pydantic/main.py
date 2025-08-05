# ####Frist Problem####
# # def add_data(name, age):
# #     print(name)
# #     print(age)

# #     print("inserted")

# # add_data("moiz", "twenty three")

# ###Second Problem: Here we can't enforce datatype###
# # def add_data(name:str, age:int):
# #     print(name)
# #     print(age)

# #     print("inserted")

# # add_data("moiz", "23")

# ###First Solution. It is not Scalable...###
# def add_data(name: str, age: int):
#     if type(name) == str and type(age) == int:
#          print(name)
#          print(age)

#          print("inserted")
#     else:
#          raise TypeError("Incorrect DataType")
    
# add_data("moiz", "23")


#Now Pydantic Solves all these problem:
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    #Here we do type validation

    ##=Now adding metadata of name
    name: Annotated[str, Field(max_length = 20, title = "Enter your name", description = "Enter name in 20 words", example = ["moiz ali", "moiz ali afzaal"])]
    age: int = Field(gt=0, lt=100)
    weight: Annotated[float, Field(gt=0, strict = True)]
    allergies: Annotated[Optional[List[str]], Field(default = None, max_length = 5)]
    details: Dict[str, str]
    email: EmailStr
    linkedin_url: AnyUrl

def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.details)
    print(patient.email)
    print(patient.linkedin_url)

    print("Inserted")

patient_info = {"name" : "Moiz", "age" : 23, "weight": 43.4,  "details" : {"email": "abc@gmail.com", "phon no. ": "0009292"}, "email": "moia@gmail.com", "linkedin_url" : "http://linkedin.com"} #here we write '700' pydantic do coerce (convert)
patient1 = Patient(**patient_info)



insert_data(patient1)    

##########################################################################
