# INF360B - Programming in Python
# Josiah Ball
# Assignment 3
##Write a Python script that has the following:
##(1/1 points) Initial Comments.
##(5/5 points) Create a dictionary for each vehicle that contains the fields/keys and values listed above.
####(5/5 points) Write a function that will take a list of
##these dictionaries and return a new dictionary with the 'name' value as the key, and the dictionary as the value.
####(5/5 points) Write a function that will go through the newly
##created dictionary and return a list of all the car's names, sorted alphabetically.
####(5/5 points) Write a function that will go through the newly
##created dictionary return a dictionary of all the cars names and year introduced.
####(5/5 points) Use a print statement to show the results of the
##function from step 3, each on their own line.
####(5/5 points) Use a print statement to show the results of the
##function from step 4 to display in the format: year : name. Sort by year introduced.
##Name	Year Introduced	Production of the Current Model	Generation	Vehicle Information
##1Ka            1996	2014	3rd	Developed by Ford Brazil as a super mini car
##2Fiesta	1976	2017	7th	Ford's long running subcompact line based on global B-car Platform
##3Focus	        1998	2018	3rd	Ford's Compact car based on global C-car platform
##4Mondeo	1992	2012	2nd	Mid sized passenger sedan with "One-Ford" design based on CD4 platform
##5Fusion	2005    2014	5th	Similar to Mondero
##6Taurus	1986	2009	6th	Full sized car based on D3 platform
##7Fiesta ST	2013	2013	1st	Fiesta's high performance factory tune
##8Focus RS	2015	2015	1st	Special high performance Focus developed by SVT
##9Mustang	1964	2014	6th	Ford's long running pony/muscle car
##10GT	        2004	2016	2nd	Ford's limited production super car inspired by the legendary race car GT40
##
import sys
#import Itemslist.py

veh_1 = {'Name': 'Ka',
        'Year Introduced': '1996',
        'Production of the Current Model': '2014',
        'Generation': "3rd",
        'Vehicle Information': 'Developed by Ford Brazil as a super mini car'}
veh_2 = {'Name': 'Fiesta',
        'Year Introduced': '1976',
        'Production of the Current Model': '2017',
        'Generation': "7th",
        'Vehicle Information': "Ford's long running subcompact line based on global B-car Platform"}
veh_3 = {'Name': 'Focus',
        'Year Introduced': '1998',
        'Production of the Current Model': '2018',      
        'Generation': "3rd",
        'Vehicle Information': "Ford's Compact car based on global C-car platform"}
veh_4 = {'Name': 'Mondeo',
        'Year Introduced': '1992',
        'Production of the Current Model': '2012',  #Mondeo	1992	2012	2nd	Mid sized passenger sedan with "One-Ford" design based on CD4 platform
        'Generation': "2nd",
        'Vehicle Information': "Mid sized passenger sedan with "'One-Ford'" design based on CD4 platform"}
veh_5 = {'Name': 'Fusion',
        'Year Introduced': '2005',
        'Production of the Current Model': '2014',
        'Generation': "5th",
        'Vehicle Information': "Similar to Mondero"}  #5Fusion	2005    2014	5th	Similar to Mondero
veh_6 = {'Name': 'Taurus',
        'Year Introduced': '1986',
        'Production of the Current Model': '2009',      ###Taurus	1986	2009	6th	Full sized car based on D3 platform
        'Generation': "6th",
        'Vehicle Information': "Full sized car based on D3 platform"}
veh_7 = {'Name': 'Fiesta ST',
        'Year Introduced': '2013',
        'Production of the Current Model': '2013',
        'Generation': "1st",
        'Vehicle Information': "Fiesta's high performance factory tune"}      #7Fiesta ST	2013	2013	1st	Fiesta's high performance factory tune
veh_8 = {'Name': 'Focus RS',
        'Year Introduced': '2015',
        'Production of the Current Model': '2015',
        'Generation': "1st",
        'Vehicle Information': "Special high performance Focus developed by SVT"}      #8Focus RS	2015	2015	1st	Special high performance Focus developed by SVT
veh_9 = {'Name': 'Mustang',
        'Year Introduced': '1964',
        'Production of the Current Model': '2014',
        'Generation': "6th",
        'Vehicle Information': "Ford's long running pony/muscle car"}  #9Mustang	1964	2014	6th	Ford's long running pony/muscle car
veh_10 = {'Name': 'GT',
        'Year Introduced': '2004',
        'Production of the Current Model': '2016',
        'Generation': "2nd",
        'Vehicle Information': "Ford's limited production super car inspired by the legendary race car GT40"}  #10GT	        2004	2016	2nd	Ford's limited production super car inspired by the legendary race car GT40
         #step 2 create list of vehicles
vehs= [veh_1, veh_2, veh_3, veh_4, veh_5, veh_6, veh_7, veh_8, veh_9, veh_10]
#function to create a new dictionary from the list of vehicles
def return_dictionary(vehicles):
    new_dictionary = {}
    for veh in vehicles:
        new_dictionary[veh["Name"]] = veh
    return new_dictionary

def vehsSort(new_dictionary):
    veh_list = list(new_dictionary.keys())
    veh_list.sort()
    return veh_list

#step3 Function vehilce names and years introduced
def veh_year(new_dictionary):
    new_dict = {}        
    for k, v in new_dictionary.items():
        new_dict[k] = v["Year Introduced"]
    return new_dict

#step 4

def return_dictionarylist(vehs):
    new_dict = list (return_dictionary.keys())
    veh_years.sort()
    print (veh_list)
    return veh_list

for name in vehsSort:
    print(name)
#step5
for name, year in veh_year(new_dictionary(vehs)).items():
    new_dict[year] = name
veh_years = list(newdict.keys())
veh_years.sort()

for year in veh_years:
    print(f"{year} : {new_dictionary[year]}")


        






