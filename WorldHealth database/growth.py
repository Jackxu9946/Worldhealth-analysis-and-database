'''
Jack Xu
growth.py
This module contains functions that allow you to find the
growth in life expectancy for a region in a time frame
'''


from utils import *


def sorted_growth_data(data,year1,year2):
    '''

    :param data: a dictinonary with country name / code as key and country class type as value
    :param year1: Initial year of interest as an int
    :param year2: Ending year of interest as an int
    :return: A list containing Countryvalue sorted in desending order
    This function will iterate through the dictionary using all the dictionary keys.
    It will construct a Countryvalue type with the country's name and its absolute value
    between the life expectancy of year 1 and year 2.
    Then it will use the built in sort function to sort the list using the absolute value
    as the key.
    '''
    Emptylist = []
    indexofyear1 = year1-1960
    indexofyear2= year2-1960
    allkeyvalues = data.keys()
    Namechecker = []
    for key in allkeyvalues:
        Countryname = data[key].Name
        if Countryname in Namechecker:
            pass
        else:
            if data[key].Life[indexofyear2] =='' or data[key].Life[indexofyear1] =='':
                pass
            else:
                Alllifedata = data[key].Life
                firstyeardata = float(Alllifedata[indexofyear1])
                secondyeardata = float(Alllifedata[indexofyear2])
                difference = abs(firstyeardata- secondyeardata)
                Countrydata = Countryvalue(Countryname,difference)
                Emptylist.append(Countrydata)
                Namechecker.append(Countryname)
    Emptylist = sorted(Emptylist,key = lambda difference:difference.value,reverse=True)
    return Emptylist

def printtop10(countrylife, year1,year2):
    '''

        :param countrylife:  A list containing of countryvalue with life expectancy and country name
        :param year1: string containing first year of interest
        :param year2: string containing second year of interest
        :return: None
        It will iterate through the countrylife list and print out the
        first 10 entries of the list with its rank,Country name and
        life expectancy growht data.
        '''
    Counter = 0
    # len(countrylife)
    print("Top 10 life expectancy growth from", year1,"to ", year2)
    while Counter < 10 and Counter < len(countrylife):
        Countrydata = countrylife[Counter]
        print(Counter + 1, ": ", Countrydata.country, Countrydata.value)
        Counter += 1

def printbottom10(countrylife, year1,year2):
    '''

        :param countrylife:  A list containing of countryvalue with life expectancy and country name
        :param year1: string containing year of interest
        :param year 2: string containing second year of interest
        :return: None
        It will iterate through the countrylife list and print out the
        last 10 entries of the list with its rank,Country name and
        life expectancy growth data.
        '''
    ranking = len(countrylife)  # Gives me the rank of the data
    counter = 0
    print("Bottom 10 life expectancy growth from ", year1,"to", year2)

    while counter < 10 and counter < len(countrylife):
        Countrydata = countrylife[ranking - 1]
        print(ranking, ": ", Countrydata.country, Countrydata.value)
        counter += 1
        ranking -= 1

def main():
    '''

    :return:None
    This function will check if the user inputs are valid or not and it will
    make the function run in a continuous loop until the user says stop.
    '''
    data = read_data('s')
    while True:
        yearofint1 = int(input("Starting year of interest(-1 to quit):" ))
        if yearofint1 == -1:
            break
        elif yearofint1 <1960 or yearofint1 > 2015:
            print(yearofint1,"Is not a valid year")
        else:
            yearofint2 = int(input("Ending year of interest(-1 to quit): "))
            if yearofint2 == -1:
                break
            elif yearofint2 <1950 or yearofint2>2015:
                print(yearofint2, "Is not a valid year")
            else:
                Region = input("Region of interest: ")
                if (Region in Validregionchecker) == False:
                    print(Region,"Is not a valid region")
                else:
                    Income = input("Enter income category: ")
                    if (Income in Validincomechecker) == False:
                        print(Income,"Is not a valid category")
                    else:
                        data = filter_income(data,Income)
                        data = filter_region(data,Region)
                        sorted_growth = sorted_growth_data(data,yearofint1,yearofint2)
                        print('\n')
                        printbottom10(sorted_growth,yearofint1,yearofint2)
                        print('\n')
                        printtop10(sorted_growth,yearofint1,yearofint2)
                        print('\n')

if __name__ == "__main()__":
    main()

#main()




