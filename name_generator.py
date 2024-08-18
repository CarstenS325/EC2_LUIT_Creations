from random import uniform
first_name = input('What\'s your first name? ') # variable one
last_name = input('What\'s your last name? ') # variable two
project_name = input('What is the project name? ') # variable three
print(last_name,first_name[0][:1],'_',project_name,uniform(2.5, 10.0),sep='')
