from typing import List
from src.data.interfaces import UserRepositoryInterface
from src.domain.models import Users
from src.infra.config import DBConnectionHandler 
from src.infra.entities import Users as UsersModel

class UserRepository(UserRepositoryInterface):
    """ Class to manage User Repository """
    
    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """ insert data in user entity
        :param - name: person name
               - password: user password
        :return - tuple with new user inserted
        """
        

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
            
                return UsersModel(
                    id=new_user.id,
                    name=new_user.name, 
                    password=new_user.password
                    )
            except:
                db_connection.session.rollback()
                raise          
            finally:
                db_connection.session.close()
            
        return None
    
    @classmethod
    def select_user_by_id(cls, id: int = None) -> List[Users]:
         """
        Select data in user entity by id and/or name
        :param - id: Id of the registry
        :return - List with Users selected
        """    
         try:
                query_data = None
      
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=id)
                        .one()
                )
                query_data = [data]
                    
                return query_data
         except:
                        db_connection.session.rollback()
                        raise  
         finally: 
                    db_connection.session.close()
                
         return None
    
    
    @classmethod
    def select_user_by_name(cls, name: str = None) -> List[Users]:
         """
        Select data in user entity by id and/or name
        :param  - name: User name
        :return - List with Users selected
        """
         try:
                query_data = None
      
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(name=name)
                        .one()
                )
                query_data = [data]
                    
                return query_data
         except:
                        db_connection.session.rollback()
                        raise  
         finally: 
                    db_connection.session.close()
                
         return None