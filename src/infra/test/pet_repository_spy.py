from typing import List
from src.domain.test import mock_pets
from src.domain.models import Pets


class PetRepositorySpy(): 
    """ Spy to Pet Repository """
    
    def __init__(self):
        self.insert_pet_params = {}
        self.select_pet_by_id_params = {}
        self.select_pet_by_user_id_params ={}
        
             
    def insert_pet(self, name: str, especie: str, age: int, user_id: int) -> Pets:
        """ Spy to all the attributes"""
   
        self.insert_pet_params["name"] = name
        self.insert_pet_params["especie"] = especie
        self.insert_pet_params["age"] = age
        self.insert_pet_params["user_id"] = user_id
        
        return mock_pets()
   
   
    def select_pet_by_id(self, id: int = None) -> List[Pets]: 
        """ Spy to all the attributes"""  
        self.select_pet_by_id_params["id"] = id
        
        return mock_pets()
   
          
    def select_pet_by_user_id(self, user_id: int = None) -> List[Pets]:
        """ Spy to all the attributes"""   
        self.select_pet_by_user_id_params["user_id"] = user_id  
    
        return mock_pets()
        