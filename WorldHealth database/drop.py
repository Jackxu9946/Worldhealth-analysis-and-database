'''
Jack Xu
drop.py
This module contains functions  that will calculate
the biggest drop in life expectancy in the world and p
print it.
'''

from utils import *



def findbiggestdrop(listvalue):
    '''

    :param listvalue: a list containing life expectancy value for a country
    :return: year1counter: (int) the first year of the drop
    :return: year2counter: (int) the second of the drop
    :return: year1value:(int) the value of life expectancy for the first year
    :return: year2value:(int)the vlaue of life expectancy for the second year
    It will initializing a loop through the listvalue,
    It will take the a value and compare it to all the values after it,
    It will change the value of year1counter,year2counter,year1value,
    year2value if the difference between the first value and the value after it is
    greater than the difference counter.
    It will continue iterating through the list until the 2 years of greatest difference
    are found.
    It treats empty strings as a skip.
    '''
    year1counter = 0
    year2counter = 1
    year1value = 0.0
    year2value = 0.0
    itercounter = 0
    differenceounter = -100000000000000000000000000000000
    while itercounter < len(listvalue):

        if listvalue[itercounter] == '':
            itercounter +=1
        else:

            insideloopcounter = itercounter +1
            itervalue = float(listvalue[itercounter])
            while insideloopcounter < len(listvalue):
                if listvalue[insideloopcounter] == '':
                    insideloopcounter+=1
                else:
                    difference = itervalue - float(listvalue[insideloopcounter])
                    if difference > differenceounter:
                        year1counter = itercounter
                        year2counter = insideloopcounter
                        year1value = float(itervalue)
                        year2value = float(listvalue[insideloopcounter])
                        differenceounter=difference
                    insideloopcounter +=1
            itercounter +=1
    return year1counter,year2counter,year1value,year2value













def CheckList(listvalue):
    #Input --> listvalue a list containing life expectancy value for a country
    #Checks if everything in the list is an empty string
    #Return True if everything is an empty string
    #Retrun False if everything is not an empty string
    counter = 0
    while counter < len(listvalue):
        if listvalue[counter] == '':
            counter +=1
        else:
            break

    if counter != len(listvalue):
        return False
    else:
        return True



def sorted_drop_data(data):
    '''
    :param data: dictionary of countryclass struct
    :return: list of Range data
    This function will return a list of Range data sorted by their drop values.
    This function will iterate through the dictionary using all the key values and
    it will feed each countryclass struct into a helper function called
    findbiggest drop which finds the biggest drop for that country. It will then store
    the drop value of year 1, drop value of year 2, year 1 and year 2, and difference
    into a Range struct_type. After every country has been added to the list,
    it will sort the list by the drop value of each country.
    '''
    Emptylist = []
    Namechecker = []
    allkeyvalues = data.keys()
    for key in allkeyvalues:
        Countryname = data[key].Name
        lifedata = data[key].Life
        if Countryname in Namechecker:
            pass
        elif CheckList(lifedata) == True:
            pass
        else:
            year1counter,year2counter,year1value,year2value = findbiggestdrop(lifedata)
            year1counter += 1960
            year2counter += 1960
            difference = year1value - year2value
            Insertvalue = Range(Countryname,year1counter,year2counter,year1value,year2value,difference)
            Emptylist.append(Insertvalue)
            Namechecker.append(Countryname)
    Emptylist = sorted(Emptylist,key = lambda Country:Country.difference,reverse=True)
    return Emptylist

def printworstdrop(Listvalue):
    '''

    :param Listvalue: List of Range struct_type
    :return:None
    This function will print the first 10 values of Listvalue which
    are suppose to be the worst 10 drop.
    '''
    counter = 0
    while counter < 10:
        year1 = Listvalue[counter].year1
        year2 = Listvalue[counter].year2
        year1value = Listvalue[counter].value1
        year2value = Listvalue[counter].value2
        Countryname = Listvalue[counter].country
        difference = Listvalue[counter].difference
        print(counter+1,':',Countryname,'from',year1,"(",year1value,")","to", year2, "(",year2value,"):",difference*-1)
        counter+=1

def main():
    '''

    :return: None
    This function will initialize all the data and feed it into
    the required function to do all the calculations.
    '''
    fdata = read_data('s')
    fdata = filter_region(fdata,'all')
    Listdata = sorted_drop_data(fdata)
    print("Top 10 worst drop in the world 1960 to 2015")
    printworstdrop(Listdata)

if __name__ =="__main()__":
    main()
#main()


