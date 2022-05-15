from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT into dojos (name,location,language,comment) VALUES (%(name)s, %(location)s,%(language)s,%(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

    @classmethod
    def get_last_dojo(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return Dojo(results[0])

    @staticmethod
    def is_valid(dojo):
        is_valid = True 
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 1:
            flash("Must choose a Dojo Location.")
            is_valid = False
        if len(dojo['language']) < 1:
            flash("Must choose Favorite Language.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comments must be at least 3 characters.")
            is_valid = False
        return is_valid