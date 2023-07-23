# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from apps import login_manager
from apps.dbModels import dbPerform, dbActionRetreiveUser
from apps.authentication.util import hash_pass
import os



class Users( UserMixin):

    def __init__(self, user, email, password, activePremium, billingDate):
        self.uid = uid
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

        
    
    def saveToDB():
         dbPerform(dbActionRetreiveUser('users', name, password, email, billingDate, activePremium), False)

    def getUserbyEmail():
        user = dbPerform(dbActionRetreiveUser(email), True)
        return user

    def __repr__(self):
          return str(username)

        

@login_manager.user_loader
def user_loader(uid):
    user = request.form.get('uid')
    if id:
        user = dbPerform(dbActionRetreiveUser(uid), true)
        return user if user else None
    return  none


@login_manager.request_loader
def request_loader(request):
    
    username = request.form.get('username')
    print(" request made")
    
    if username:
        print("user requested")
        user = dbPerform(dbActionRetreiveUser(username), True)
        return user if user else None
    return None
