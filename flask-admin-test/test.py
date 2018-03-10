import os

current = os.path.dirname(os.path.abspath(__file__))
db_path = 'sqlite:////{}{}'.format(current, '/db/app.db')
print(db_path)
