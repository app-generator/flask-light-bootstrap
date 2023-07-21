# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from dbModels import  login_manager, dbPerform, dbActionRetreiveUser

from apps.authentication.util import hash_pass
import os



class Users( UserMixin):

    def __init__(self, user, email, password, activePremium, billingDate):
        self.id = id
        self.user = user
        self.email = email
        self.password = password
        self.activePremium = activePremium
        self.billingDate = billingDate

    def hash_pass( **kwargs):

        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

        def __repr__(self):
          return str(self.username)
    
    def saveToDB():
         dbPerform(dbActionRetreiveUser('users',self.name, self.password, self.email, self.billingDate, self.activePremium), False)

    def getUserbyEmail():
        dbData = dbPerform(dbActionRetreiveUser(self.email))

        


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None

