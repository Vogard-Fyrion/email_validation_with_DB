from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self,data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = (
            "INSERT INTO emails (email) "
            "VALUES (%(email)s);"
        )
        return connectToMySQL('emails').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = (
            "SELECT * FROM emails;"
        )
        results = connectToMySQL('emails').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails

    @classmethod
    def get_one_by_id(cls, data):
        query = (
            "SELECT * FROM emails "
            "WHERE id = %(id)s;"
        )
        results = connectToMySQL('emails').query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_one_by_email(cls, data):
        query = (
            "SELECT * FROM emails "
            "WHERE email = %(email)s"
        )
        results = connectToMySQL('emails').query_db(query, data)
        return cls(results[0])

    @classmethod
    def delete(cls, data):
        query = (
            "DELETE FROM emails "
            "WHERE id = %(id)s;"
        )
        connectToMySQL('emails').query_db(query, data)

    @staticmethod
    def validator(form_data):
        is_valid = True
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid