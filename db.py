'''
This file contains mongodb uri
'''
from pymongo import MongoClient


client = MongoClient('mongodb://ahmed_soliman:123456@ds247699.mlab.com:47699/goal-tracker')
db = client['goal-tracker']