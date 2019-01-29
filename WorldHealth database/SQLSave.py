#Create a mysql database with the following properties
#Primary Key, Country, Country code, year 1960-2017, Region, Wealth ,
import mysql.connector
from mysql.connector import Error
DataField = ["CountryName","CountryCode"]
YEAR = "YEAR"
def main():
    mysql.connector.connect(host='localhost', database='mysql',
                            user='sysadmin', password='1234567890')

def connect():
    "Connect o mySQL database"
    try:
        conn = mysql.connector.connect(host='localhost',database = 'worldhealth',
                             user='sysadmin',password='1234567890')
        if conn.is_connected():
            #conn.cursor("CREATE DATABASE WorldHealth")
            #print("Connected successfully")
            #conn.cursor().execute("CREATE TABLE healthtabble (CountryID int auto_increment primary key)")
            #AddAllOtherField(conn.cursor())
            #AdllAllYear(conn.cursor())
            #conn.cursor().execute("ALTER TABLE STD ADD PRIMARY KEY (CountryCode)");
            read_data("worldbank_life_expectancy_data.txt",conn.cursor())
            conn.commit()
    except Error as e:
        print(e)


#This function will read a file and then update all the appropriate field with the correct
#Value from that file
def read_data(filename,cursor):
    fd = open(filename)
    counter = 0
    for line in fd:
        if counter ==0:
            counter +=1
        else:
            EntryList = line.split(",");
            #print(len(EntryList))
            #Everything in this format [CountryName,CountryCode,Yearblank"
            secondcounter = 0
            QueryString = "INSERT INTO healthtabble VALUES(null"
            for L in EntryList:
                if secondcounter < 2:
                    if "'" in L:
                        print('yeet')
                        L = L.replace("'","");
                        print(L)
                    QueryString = QueryString +"," + "'" +L +"'"
                    secondcounter+=1

                else:
                    if(L == ""):
                        L = "0" ;
                    QueryString =  QueryString+","+L;
            AnotherQString = QueryString[:len(QueryString) - 2]
            AnotherQString += ")";

            print(len(AnotherQString.split(",")))
            print(AnotherQString)
            cursor.execute(AnotherQString)











def AddAllOtherField(cursor):
    VarC = " VARCHAR(50) NOT NULL"
    for n in DataField:
        query = "ALTER TABLE healthtabble ADD COLUMN "+n+ VarC
        cursor.execute(query)


#Intialize all the proper tables needed
def AdllAllYear(cursor):
    year = 1960
    for n in range(60,61):
        x = year +n
        #cursor.execute("ALTER TABLE std")
        x = "Year"+ str(x)
        query = "ALTER TABLE healthtabble DROP COLUMN  " + x #+" float "
        print(query)
        cursor.execute(query)
        #cursor.execute("ADD COLUMN "+str(x)+" INT NOT NULL");


if __name__=='__main__':
    connect()

