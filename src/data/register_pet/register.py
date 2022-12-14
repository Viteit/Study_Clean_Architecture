from typing import List, Type, Dict
from src.data.find_user import FindUser
from src.domain.use_cases import RegisterPet as RegisterPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.models import Pets, Users

class RegisterPet(RegisterPetInterface):
    """ Class to define usecase: Register Pet """
    
    def __init__(self, pet_repository: Type[PetRepository], find_user: Type[FindUser]):
        self.__pet_repository = pet_repository
        self.__find_user = find_user
        
        
    def register(self, name: str, specie: str, user_information: Dict[int,str], age: int = None) -> Dict[bool, Pets]:
        """ Register user use case
         :param - name: pet name
                - specie: specie of pet
                - age: age of pet
                - user_id: user_id of pet
        :return - Dictionary with informations of the process
        """
        
        response = None
        
        # Validate entry and trying to find an user
        validate_entry = isinstance(name, str) and isinstance(specie, str)  and isinstance(age, int)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Sucess"]
       
        if checker:
            response = self.__pet_repository.insert_pet(name, specie, age, user_information["user_id"])
        
        return {"Sucess": checker, "Data": response} 
             
    def __find_user_information(self, user_information: Dict[int,str]) -> Dict[bool, List[Users]]:
        """Check user Infos and select user 
        :param - user_information: Dictionary with user_id and/or user_name
        :return - Dictionary with the response of find_use use case
        """
        
        user_founded = None
        user_params = user_information.keys()
        
        if "user_name" in user_params and not "user_id" in user_params:
            user_founded = self.__find_user.by_name(user_information["user_name"])
        
        elif "user_id" in user_params and not "user_name" in user_params :
            user_founded = self.__find_user.by_id(user_information["user_id"])
        
        elif "user_id" and "user_name" in user_params :
            user_name = self.__find_user.by_name(user_information["user_name"])
            user_id = self.__find_user.by_id(user_information["user_id"])
            user_founded = user_name and user_id
            
        else:
            return {"Sucess": False, "Data": None}
        
        return user_founded
        
    
        
        