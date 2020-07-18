# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:13:17 2020

@author: hp
"""

from instapy import InstaPy
session = InstaPy(username = 'ayushgoel65', password = 'devil123@@##', headless_browser = False)
session.login()
session.like_by_tags(["bmw","mercedes"], amount=4)
session.set_dont_like(["naked","nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice :)","Beautiful","Awesome"])
session.end()
