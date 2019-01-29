'''
Jack Xu
utils.py
This module have all the RIT_lib structure identified for later uses
This module containings data processing functions like region analysis
and income analysis
'''
from rit_lib import *

Countryclass = struct_type("Countryclass",(str,"Name"),(str,"Code"),(list,"Life"),((str,NoneType),"Region")
    ,((str,NoneType),"Income"),((str,NoneType),"Special"),((bool,NoneType),"Country"))

Countryvalue = struct_type("Countryvalue",(str,"country"),(float,"value"))
Range = struct_type("Range",(str,"country"),(int,"year1"),
                    (int,"year2"),(float,"value1"),(float,"value2"),(float,"difference"))


Validregionchecker = ["Middle East & North Africa","Europe & Central Asia","North America",
                       "Latin America & Caribbean","South Asia","East Asia & Pacific","Sub-Saharan Africa",'all'
                       ]
Validincomechecker = ["Lower middle income","High income","Upper middle income","Low income",'all']

def read_data(filename):
    '''Input: A string containg a existing filename
    Output: A dictionary with the country name and code as key for a Countryclass construct
    This function opens the file and iterate through it.
    If the country is not yet in the dictionary, it will make an entry
    for that country with its country name as the key and a Countryclass construct
    as a value.
    The countryclass construct includes a list of the country's life expectancy values,
    Countryname, Country code, country region, country income category ,country special
    and it will have a boolean to see if the country is a legitimate country or a large grouping
    '''
    fd = open("worldbank_life_expectancy_data.txt")
    new_dict = dict()
    counter = 0
    Regionalchecker = ["Middle East & North Africa","Europe & Central Asia","North America",
                       "Latin America & Caribbean","South Asia","East Asia & Pacific","Sub-Saharan Africa"
                       ]
    #This loop makes a dictionary using the country Code and name as key values
    for entry in fd:
        if counter == 0:
            counter +=1
        else:
            entrylist = entry.split(',')
            Countryname = entrylist[0]

            Code = entrylist[1]
            Life = entrylist[2:len(entrylist)-1]
            '''if Countryname == "Thailand":
                print(Life)'''
            new_dict[Countryname] = Countryclass(Countryname,Code,Life,None,None,None,None)
            new_dict[Code]= Countryclass(Countryname,Code,Life,None,None,None,None)
    newopen = open("worldbank_life_expectancy_metadata.txt")
    counter = 0
    #Adds the rest of the stuff onto dictionayr like Income group and region to the country
    for entry in newopen:
        if counter == 0:
            counter +=1
        else:
            entrylist = entry.split(',')
            Code = entrylist[0]
            Region = entrylist[1]
            Incomegroup = entrylist[2]
            Special = entrylist[3]
            new_dict[Code].Region = Region
            new_dict[Code].Income = Incomegroup
            new_dict[Code].Special = Special
            Countryname = new_dict[Code].Name
            new_dict[Countryname] = new_dict[Code]
            Regional = new_dict[Code].Region
            if Regional in Regionalchecker:
                new_dict[Code].Country = True
                new_dict[Countryname].Country = True
            else:
                new_dict[Code].Country = False
                new_dict[Countryname].Country = False

    return new_dict




def filter_region(data,region):
    '''Input:data( a dictionary with country name/code as key and countryclass struct as value)
            region( a region to filter the data by)( string)
    Output: a dictionary containing all the country in the input region
    It iterates through the dictionary by asking for a list
    of all the dicitionary value.and iterate through that.
    While it is iterating it will build a new dictionary with all the country class
    struct containing the input region
    '''
    new_dict = {}
    allkeyvalues = data.keys()
    if region == "all" or region == "All":
        for key in allkeyvalues:
            if data[key].Country == True:
                new_dict[key]= data[key]
        return new_dict
    for key in allkeyvalues:
        if data[key].Region == region:
            new_dict[key] = data[key]
    return new_dict

def filter_income(data,income):
    '''Input = Input:data( a dictionary with country name/code as key and countryclass struct as value)
            Income( an income category to filter the data by)( string)
        Output: a dictionary containing all the country in the input income category
        It iterates through the dictionary by asking for a list
        of all the dicitionary value.and iterate through that.
        While it is iterating it will build a new dictionary with all the country class
        struct containing the input Income category '''

    new_dict = {}
    allkeyvalues = data.keys()
    if income == "all" or income == "All":
        for key in allkeyvalues:
            if data[key].Country == True:
                new_dict[key]= data[key]
        return new_dict

    for key in allkeyvalues:
        if data[key].Income == income:
            new_dict[key] = data[key]
    return new_dict

def regionanalysis(data):
    '''Input = Input:data( a dictionary with country name/code as key and countryclass struct as value)
     Output= None
     This function will iterate through the dictionary by using the key values.
     It will group the region and have a count of how many countries in that region.
     It will create a list of count and print the corresponding region
     with its country count'''
    MENA = 0
    ECA = 0
    NA = 0
    LAC = 0
    SA = 0
    EAP = 0
    SSA = 0
    allkeyvalue = data.keys()
    for key in allkeyvalue:
        if data[key].Region == "Middle East & North Africa":
            MENA += 1
        elif data[key].Region == "Europe & Central Asia":
            ECA += 1
        elif data[key].Region == "North America":
            NA += 1
        elif data[key].Region == "Latin America & Caribbean":
            LAC += 1
        elif data[key].Region == "South Asia":
            SA += 1
        elif data[key].Region == "East Asia & Pacific":
            EAP += 1
        elif data[key].Region == "Sub-Saharan Africa":
            SSA += 1
    printcounter = 0
    while printcounter < 7:
        if printcounter == 0:
            print("Middle East & North Africa: ",MENA//2)
            printcounter +=1

        elif printcounter ==1:
            printcounter +=1
            print("Europe & Central Asia: ",ECA//2)

        elif printcounter ==2:
            printcounter +=1
            print( "North America: ",NA//2)

        elif printcounter ==3:
            printcounter +=1
            print( "Latin America & Caribbean",LAC//2)

        elif printcounter ==4:
            printcounter +=1
            print("South Asia",SA//2)

        elif printcounter ==5:
            printcounter +=1
            print("East Asia & Pacific",EAP//2)
        elif printcounter ==6:
            printcounter +=1
            print("Sub-Saharan Africa",SSA//2)


def incomeanalysis(data):
    '''

    :param data: ( a dictionary with country name/code as key and countryclass struct as value)
    :return: None
    This function will iterate through the dictionary by using the key values.
     It will group the income category and have a count of how many countries in that category.
     It will create a list of count, and print the corresponding income category
     with its country count
    '''
    Lowmiddle = 0
    uppermiddle = 0
    upper =0
    low = 0
    allkeyvalues = data.keys()
    for key in allkeyvalues:
        if data[key].Income == "Lower middle income":
            Lowmiddle +=1
        elif data[key].Income == "Upper middle income":
            uppermiddle +=1
        elif data[key].Income == "High income":
            upper +=1
        elif data[key].Income == "Low income":
            low +=1
    printcounter =0
    while printcounter < 4:
        if printcounter ==0:
            print("Lower middle income: ",Lowmiddle//2)
            printcounter+=1
        elif printcounter ==1:
            print("Upper middle income: ", uppermiddle//2)
            printcounter+=1

        elif printcounter ==2:
            print("Upper income: ",upper//2)
            printcounter+=1

        elif printcounter ==3:
            print("Low income: ",low//2)
            printcounter+=1

    return (Lowmiddle,uppermiddle,upper,low)

def countcountry(data):
    '''

    :param data: ( a dictionary with country name/code as key and countryclass struct as value)
    :return: None
    It will iterate through the dictionary and count how many data values
    are countries.
    It will then print the country count.
    '''
    allkeyvalue = data.keys()
    Countrycount= 0
    for key in allkeyvalue:
        if data[key].Country == True:
            Countrycount +=1
    return Countrycount


def main():
    '''

    :return: None
    This function will read the data and feeds it into various function
    that will analyze the data and print the analysis.
    '''
    dataset = read_data('s')
    Countrycount = countcountry(dataset)
    print("Total number of entities: ", len(dataset)//2)
    print("Total number of Countries: ", Countrycount//2)
    print("\n")
    print("\n")
    regiondataanalysis = regionanalysis(dataset)
    print("\n")
    print("\n")
    incomedataanalysis = incomeanalysis(dataset)
    print("\n")
    print("\n")
    Regionname = input("Enter region name: ")
    Regionfilter = filter_region(dataset,Regionname)
    Regionfilterkey = Regionfilter.keys()
    Regionchecker = []
    for key in Regionfilterkey:
        if (Regionfilter[key].Name in Regionchecker) == False:
            print(Regionfilter[key].Name,Regionfilter[key].Code)
            Regionchecker.append(Regionfilter[key].Name)
        else:
            pass
    #print(Regionchecker)
    print("\n")
    print("\n")
    Incomecategory = input("Enter income category: ")
    Incomefilter = filter_income(dataset,Incomecategory)
    Incomefilterkey = Incomefilter.keys()
    Incomechecker = []
    for key in Incomefilter:
        if (Incomefilter[key].Name in Incomechecker) == False:
            print(Incomefilter[key].Name,Incomefilter[key].Code)
            Incomechecker.append(Incomefilter[key].Name)
        else:
            pass
    print("\n")
    print("\n")
    while True:
        Countryname = input("Enter name of country or country code(Enter to quit): ")
        if Countryname == '':
            break
        elif (Countryname in dataset) == False:
            print(Countryname,'Is not a valid code or country')
        else:
            print("Life expectancy data for ", Countryname)
            lifeexpect = dataset[Countryname].Life
            Yearcounter = 1960
            for value in lifeexpect:
                if value != '':
                    print(Yearcounter,"Life expectancy: ",value)
                    Yearcounter +=1
                else:
                    Yearcounter +=1
    



if __name__ == '__main()__':
    main()
#main()