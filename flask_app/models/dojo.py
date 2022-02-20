from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:

    def __init__(self,data):
        self.id = data['id']

        self.name= data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']

        self.created_at = data['created_at']
        self.updated_at= data['updated_at']

#=======================================================
# save the survery data
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name,location,language,comment, created_at) VALUES(%(name)s, %(location)s, %(language)s, %(comment)s, NOW());"
        return connectToMySQL("dojo_survey_schema").query_db(query, data)
#=======================================================

#=======================================================
#This methods extracts the data of the newest submission from db and displays on second.html
    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1"
        survey = connectToMySQL('dojo_survey_schema').query_db(query)
        return Dojo(survey[0])

#=======================================================

#=======================================================
#create staticmethods for the validations for the survey

    @staticmethod
    def is_valid(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(dojo['location']) < 1:
            is_valid = False
            flash("You must select a dojo location.")
        if len(dojo['language']) < 1:
            is_valid = False
            flash("You must select a favorite language.")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("Comment must have at least 3 characters.")
        return is_valid
#=======================================================