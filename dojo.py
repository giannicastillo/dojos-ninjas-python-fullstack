
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:

    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninjas=[]
    
    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_and_ninjas2').query_db(query)
        print(results)
        dojos =[]
        for dojo_data in results:
            dojos.append(cls(dojo_data))
        return dojos
    
    @classmethod
    def one_dojo(cls,data):
        query= "SELECT * FROM dojos WHERE id = %(id)s;"
        results=connectToMySQL('dojo_and_ninjas2').query_db(query,data)
        print(results)
        return cls(results[0])



    @classmethod
    def dojo_with_ninjas(cls,data):
        query= "SELECT * FROM dojo_and_ninjas2.dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id= %(id)s;"
        results=connectToMySQL('dojo_and_ninjas2').query_db(query,data)
        print (results)

        dojos= cls(results[0])
        # dojo_ids = []// PARSING 2 

        # for data in results:  //PARSING #1
        #     if data['id'] not in dojo_ids:
        #         dojo_ids.append(data['id'])
        #         dojos.append(cls(data))

        for data in results:

            ninja_data = {
                "id" : data['ninjas.id'],
                "first_name" : data['first_name'],
                "last_name" : data['last_name'],
                "age" : data['age'],
                "created_at" : data['ninjas.created_at'],
                "updated_at" : data['ninjas.updated_at']
            }
            dojos.ninjas.append(ninja.Ninja(ninja_data))
            # dojos[len(dojos)-1].ninjas.append(ninja.Ninja(ninja_data))// parsing 2  
        return dojos

    @classmethod
    def add_dojo(cls,data):
        query="INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        results = connectToMySQL('dojo_and_ninjas2').query_db(query,data)
        return results

# METHOD FOR THE DROPDOWN ON NEWNINJA HTML 

    @classmethod
    def newninja_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_and_ninjas2').query_db(query)
        print(results)
        dojos =[]
        for dojo_data in results:
            dojos.append(cls(dojo_data))
        return dojos
