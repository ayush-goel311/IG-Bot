# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:12:57 2020

@author: hp
"""

from instapy import InstaPy 
session = InstaPy(username="ayush_brainbox_goel", password="devil123@@##")
session.login()
session.like_by_tags(["bmw","mercedes"],amount = 5)
