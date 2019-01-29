from utils import *

import turtle



Validregionchecker = ["Middle East & North Africa","Europe & Central Asia","North America",
                       "Latin America & Caribbean","South Asia","East Asia & Pacific","Sub-Saharan Africa"
                       ]
Validincomechecker = ["Lower middle income","High income","Upper middle income","Low income",'all']

def findmedianvalue(dict):
    '''

    :param dict: dictionary of Countryclass struct_type with the country name/code as the key
    :return: a list of life expectancy value(string) by year using the index
    This function will initially make iterate through the dictionary using all the
    key value and eliminiate the duplicates.
    Afterwards, the function will make a list of lists.
    It will then fill up the list of list using life
    expectancy value from each country.
    It will then sort each list within the list from smallest to biggest.
    The function will extract the median value from each list of list
    and put them into a new list.
    '''
    allkeyvalues = dict.keys()#Gets all the key values
    ListofCountry = []
    Namechecker = []#This is to eliminate the duplicates since I have country
                    # and code pointing to the same thing
    for key in allkeyvalues:
        Countrydata = dict[key]
        if (Countrydata.Name in Namechecker):
            pass
        else:
            ListofCountry.append(Countrydata.Life)
            Namechecker.append(Countrydata.Name)

    Numberofentry = len(ListofCountry[0])# Finds number of life expectancy value in the list
    Databyyearlist = []#The list to store all the median values
    Outerloopcounter = 0 #This will also acts as the year counter and iterate through the lists
                        # within the list
    Countrylength = len(ListofCountry)# Find how many country there are
    while Outerloopcounter < Numberofentry:
        Databyyearlist.append([])#Makes a Numberofentry number of emptylist within a list
        Outerloopcounter+=1
    Outerloopcounter = 0# Resets the outerloop
    while Outerloopcounter < Countrylength:# This will iterate through every country
        Listoflifedata = ListofCountry[Outerloopcounter]#This gives the list of life expectancy
                                                        #Data for that country
        Innerloopcounter = 0 # Iterate through every single value in the life expectancy list
        while Innerloopcounter < Numberofentry:
            yeardata = Listoflifedata[Innerloopcounter]
            Databyyearlist[Innerloopcounter].append(yeardata)# puts every single life expectancy value
                                                    # into the correct list
            Innerloopcounter +=1
        Outerloopcounter+=1
    Outerloopcounter = 0#Resets the outerloop to go through every single list within the list
    print(Databyyearlist)
    while Outerloopcounter < Numberofentry:#Iterate through the list
        #I use the index as year counter, index 0 of the list is year 1960 and so on.
        Lifedatalist = sorted(Databyyearlist[Outerloopcounter])#Sorts the list of life expectancy of that year
        #print(Outerloopcounter+1960,Lifedatalist)
        Medianindex = (len(Lifedatalist) // 2) #Finds the middle index of the list
        #print(Outerloopcounter+1960,Medianindex)
        #print(Medianindex)
        Medianval = Lifedatalist[Medianindex]#Finds the median value of the list
        Databyyearlist[Outerloopcounter] = Medianval# Replace the entire list of life expectancy of
                                            # that year by the median value
        Outerloopcounter+=1
    return (Databyyearlist)


def grapher(ListOMedian):
    '''

    :param ListOMedian: List of median values(string)
    :return:None
    This function will graph the every single value of ListOMedian
    with a corresponding Y value.
    '''
    Xcor = 1960 # Sets the year value to 1960
    Ycor = 0 # Y coordinate starts from 0
    Listitercounter = 0
    firstcounter = 0
    while Listitercounter < len(ListOMedian):
        Xcor = Listitercounter*5 # multiply it by 5 to scale it by 5.
        '''if ListOMedian[Listitercounter] == '':
            print(1)'''
        Ycor = float(ListOMedian[Listitercounter])*3 # multiply it by 3 to scale it by 3.
        '''Plots the point'''
        if firstcounter == 0:
            turtle.up()
            turtle.setpos(Xcor,Ycor)
            firstcounter+=1
            turtle.down()
            Listitercounter+=1
        else:
            Listitercounter+=1
            turtle.setpos(Xcor,Ycor)



def drawallinitialized():
    '''

    :return:None
    Initialize the canvas to draw by setting turtle speed and making
    the turtle pos at 0,0. It will also draw the x and y axis of the graph.
    '''
    turtle.home()
    turtle.speed(0)
    turtle.left(90)
    counter = 1
    #Moves 90*3 to enlarge by 3 times
    turtle.fd(90*3)
    turtle.home()
    turtle.up()
    turtle.setheading(180)
    turtle.fd(15)
    turtle.setheading(90)
    turtle.write(0)
    while counter < 10:

        turtle.fd(30)
        turtle.setheading(270)
        turtle.write(counter*10)
        turtle.setheading(90)
        counter+=1
    turtle.home()
    turtle.down()
    turtle.fd(55 * 5)
    turtle.home()
    turtle.penup()
    turtle.setheading(270)
    turtle.fd(15)
    turtle.setheading(0)
    turtle.write(1960)
    turtle.fd(55*5)
    turtle.write(2015)


colorbox = ["black","green","yellow","orange","red","purple","blue"]
colorbox2 = ["orange","red","green","blue"]
def drawlegend(Listofmedianvalue):
    '''

    :param Listofmedianvalue: List of median values(strings)
    :return: NOne
    Draws the legend depending on which graph. It uses the Listofmedianvalue
    as a checkpoint.
    '''
    countervalue = len(Listofmedianvalue)
    upperwardcounter = 0
    if countervalue <= 4:
        turtle.up()
        turtle.setpos(300, 300)
        while upperwardcounter < countervalue:
            turtle.pencolor(colorbox2[upperwardcounter])
            turtle.write(Incomeprint[upperwardcounter])
            turtle.up()
            turtle.setheading(270)
            turtle.fd(15)
            turtle.down
            upperwardcounter+=1
    else:
        turtle.up()
        turtle.setpos(300, 300)
        while upperwardcounter < countervalue:
            turtle.pencolor(colorbox[upperwardcounter])
            turtle.write(Regionprint[upperwardcounter])
            turtle.up()
            turtle.setheading(270)
            turtle.fd(15)
            turtle.down
            upperwardcounter += 1

Incomeprint = ["High Income","Upper middle income","Lower middle income","Low income"]
Regionprint = [ "Middle East & North Africa","Europe & Central Asia","North America","Latin America & Caribbean",
                "South Asia","East Asia & Pacific","Sub-Saharan Africa"]
def graphall(Listofmedianvalue):
    '''

    :param Listofmedianvalue:
    :return:
    '''
    turtle.ht()
    drawallinitialized()
    turtle.down()
    drawlegend(Listofmedianvalue)
    Drawcounter =0
    while Drawcounter < len(Listofmedianvalue):
        if len(Listofmedianvalue) > 4:

            turtle.pencolor(colorbox[Drawcounter])
            grapher(Listofmedianvalue[Drawcounter])
            Drawcounter+=1
        else:
            turtle.pencolor(colorbox2[Drawcounter])
            grapher(Listofmedianvalue[Drawcounter])
            Drawcounter += 1







def filterallregion(data):
    MENA = filter_region(data,"Middle East & North Africa")
    MENA2 = findmedianvalue(MENA)
    ECA = filter_region(data,"Europe & Central Asia")
    ECA2 = findmedianvalue(ECA)
    NA = filter_region(data,"North America")
    NA2 = findmedianvalue(NA)
    LAC = filter_region(data,"Latin America & Caribbean")
    LAC2 = findmedianvalue(LAC)
    SA = filter_region(data,"South Asia")
    SA2 = findmedianvalue(SA)
    #print("List of all median South Asia",SA2)
    EAP = filter_region(data,"East Asia & Pacific")
    EAP2 = findmedianvalue(EAP)
    SSA= filter_region(data,"Sub-Saharan Africa")
    SSA2 = findmedianvalue(SSA)
    #print("List of all median Sub-Saharan Africa",SSA2)
    Listofeverything = [MENA2,ECA2,NA2,LAC2,SA2,EAP2,SSA2]
    return(Listofeverything)

def filterallincome(data):
    High = filter_income(data,"High income")
    Uppermiddle = filter_income(data,"Upper middle income")
    Lowermiddle = filter_income(data,"Lower middle income")
    Low = filter_income(data,"Low income")
    High2 = findmedianvalue(High)
    Uppermiddle2 = findmedianvalue(Uppermiddle)
    Lowermiddle2 = findmedianvalue(Lowermiddle)
    Lower2 = findmedianvalue(Low)
    Listofeverything = [High2,Uppermiddle2,Lowermiddle2,Lower2]
    #print(Listofeverything)
    return(Listofeverything)

def grapheverything(Listoincomedata,Listoregiondata):
    drawallinitialized()
    turtle.down()
    drawlegend(Listoregiondata)
    Drawcounter = 0
    while Drawcounter < len(Listoregiondata):
        if len(Listoregiondata) > 4:

            turtle.pencolor(colorbox[Drawcounter])
            grapher(Listoregiondata[Drawcounter])
            Drawcounter += 1
        else:
            turtle.pencolor(colorbox2[Drawcounter])
            grapher(Listoregiondata[Drawcounter])
            Drawcounter += 1
    Enter = input("Press enter to draw next graph ")
    if Enter == '':
        turtle.reset()
        drawallinitialized()
        turtle.down()
        drawlegend(Listoincomedata)
        Drawcounter = 0
        while Drawcounter < len(Listoincomedata):
            if len(Listoincomedata) > 4:

                turtle.pencolor(colorbox[Drawcounter])
                grapher(Listoincomedata[Drawcounter])
                Drawcounter += 1
            else:
                turtle.pencolor(colorbox2[Drawcounter])
                grapher(Listoincomedata[Drawcounter])
                Drawcounter += 1
    else:
        turtle.done()
    turtle.done()

def main():
    data =read_data('s')
    turtle.ht()
    filterallregion(data)
    ListoIncomeData = filterallincome(data)
    ListoRegiondata = filterallregion(data)
    grapheverything(ListoIncomeData,ListoRegiondata)



main()