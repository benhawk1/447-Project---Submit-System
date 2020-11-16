# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:33:09 2020

@author: benhawk1
"""

import pandas as pd
import hashlib


# Tool for hashing given passwords for a specified user in the userbase csv file
def encode(password, row, df):
    salt = b'1\xcc\xf09V\x1b\xed\xf5\x87\x13p\xe7/3ZA\x80\xdfN\t\xd1P\xa1\xf9\x95\xc7T\xfe\x19\xa0\xd4\x0b'
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
    df.at[row, 'Key'] = key
    # Replace the string with the desired path to save the file
    df.to_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv", mode='w', index=False)