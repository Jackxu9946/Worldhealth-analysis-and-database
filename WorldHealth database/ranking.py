'''
Jack Xu
ranking.py
This module contrains function that will calculate the
top life expectancy for each category you choose such as
income category or/and region category.
'''


from utils import *



def sorted_ranking_data(data,year):
    '''

    :param data:a dictinonary with country name / code as key and country class type as value
    :param year: a string containing year of interest
    :return: A sorted list of countryvalue maker with
    country name and life expectancy value for that year

    It will iterate through every country in the dictionary using the
    key values and extract the life expectancy value for that year.
    It will then construct a countryvalue with life expectancy value
    and country name as its attributes.
    Afterward the new struct_type is inserted into the list.
    The list is sorted using the sorted function and Countryvalue.value as key

    '''
    Indexvalueyear = int(year) - 1960
    allkeyvalues = data.keys()
    Emptylist = []
    Namechecker = []# This is useful since I have two key values referring to the same thing
                    # Both country name and code are used as key value for that country
    for key in allkeyvalues:
        if data[key].Name in Namechecker:
            pass
        else:
            Namechecker.append(data[key].Name)
            if data[key].Life[Indexvalueyear] == '':
                pass
            else:
                Lifeexpect = float(data[key].Life[Indexvalueyear])
                Countryvaluemaker = Countryvalue(data[key].Name,Lifeexpect)
                Emptylist.append(Countryvaluemaker)
    Sortedlist = sorted(Emptylist,key= lambda Country:Country.value,reverse= True)
    return Sortedlist


def printtop10(countrylife,year):
    '''

    :param countrylife:  A list containing of countryvalue with life expectancy and country name
    :param year: string containg year of interest
    :return: None
    It will iterate through the countrylife list and print out the
    first 10 entries of the list with its rank,Country name and
    life expectancy data.
    '''
    Counter = 0
    #len(countrylife)
    print("Top 10 life expectancy for ",year)
    while Counter < 10 and Counter < len(countrylife):
        Countrydata = countrylife[Counter]
        print(Counter+1,": ",Countrydata.country,Countrydata.value)
        Counter +=1


def printbottom10(countrylife,year):
    '''

    :param countrylife:  A list containing of countryvalue with life expectancy and country name
    :param year: string containg year of interest
    :return: None
    It will iterate through the countrylife list and print out the
    last 10 entries of the list with its rank,Country name and
    life expectancy data.
    '''
    ranking = len(countrylife) #Gives me the rank of the data
    counter = 0
    print("Bottom 10 life expectancy for ",year)

    while counter <10 and counter < len(countrylife):
        Countrydata = countrylife[ranking-1]
        print(ranking,": ",Countrydata.country,Countrydata.value)
        counter+=1
        ranking-=1



def main():
    '''

    :return:None
    This function will run continuously and check if the user inputs are valid.
    It will exit when the user enters nothing.
    '''
    while True:
        yearofint = int(input("Enter year of interest(Enter -1 to break): "))
        if yearofint == -1:
            break
        elif yearofint < 1960 or yearofint > 2015:
            print(yearofint,"Is not a valid year of interest")
            print("valid years 1960-2015")
        else:
            Region = input("Enter region of interest(Type all to consider all): ")
            if (Region in Validregionchecker) == False:
                print( Region, " is not a valid region")
            else:
                Income = input( " Enter income category of interest: ")
                if (Income in Validincomechecker) == False:
                    print(Income, "Is not a valid income category")
                else:
                    data = read_data('s')
                    data = filter_income(data,Income)
                    #print("after income filter",data)
                    data = filter_region(data,Region)
                    #print("after region filter",data)
                    Sortedlistoflife = sorted_ranking_data(data,yearofint)
                    #print(Sortedlistoflife)
                    printtop10(Sortedlistoflife,yearofint)
                    print("\n")
                    printbottom10(Sortedlistoflife,yearofint)
if __name__ == "__main()__":
    main()
#main()