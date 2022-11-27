from geopy.geocoders import ArcGIS

import pymysql as mq
mydatabase = mq.connect(host="localhost",user="root",passwd="")

mycursor = mydatabase.cursor()


mycursor.execute("create database if not exists Addressbook")
mycursor.execute("use Addressbook")
mycursor.execute("create table if not exists StoreAddressbook( housenumber varchar(10) , colonyname varchar(100), cityname varchar(50), latitude varchar(10), longitude varchar(10) , householdername varchar(50) )")


try:
    while True:
        print("--------------------------------------------------------------")
        print("*************************ADDRESS******************************")
        print("--------------------------------------------------------------")
        print("1. ADD ADDRESS")
        print("2. UPDATE ADDRESS")
        print("3. DELETE ADDRESS")
        print("4. Exist")


        choice = int(input(" Enter your choice :--"))
        Housecoordinate=ArcGIS()

        # Here we are adding the address

        if (choice == 1):
           print("-----------------------------------------")
           print("*************ENTER THE ADDRESS***********")
           print("-----------------------------------------")
           HouseHolderName = input("Enter the Name of person whose house  is  ")
           HouseNumber = int(input("Enter the house number:--"))
           ColonyName = input("Enter the colony name :--")
           CityName = input(" Enter the city name :-- ")
           colonyname = Housecoordinate.geocode()
           mycursor=mydatabase.cursor()
           InsertValue = "insert into StoreAddressbook (HouseNumber , ColonyName ,CityName ,HouseHolderName ) values (%s ,%s ,%s ,%s)"
           Valu = ( HouseNumber,ColonyName ,CityName ,HouseHolderName)
           mycursor.execute(InsertValue,Valu)
           mydatabase.commit()
           print("\t\t\t!!!!Information Saved Successfully !!!!")
           print("----------------------------------------------")



           # Here we are  Updateing the address

        elif choice == 2 :
           print("-----------------------------------------")
           print("*************UPDATE THE ADDRESS***********")
           print("-----------------------------------------")

           HouseHolderName = input("Enter the house holder name whose Address you want to update:-->")
           HouseNumber = int(input("Enter correct the house number:--"))
           ColonyName = input("Enter the correct colony name :--")
           CityName = input(" Enter the correct city name :-- ")

           mycursor = mydatabase.cursor()
           Updatedata = "update StoreAddressbook set HouseNumber = %s ,ColonyName =%s ,CityName = %s where HouseHolderName = %s "
           data = ( HouseNumber , ColonyName , CityName , HouseHolderName)
           mycursor.execute(Updatedata , data)
           mydatabase.commit()
           print("\t\t\t!!!!Information Update Successfully !!!!")
           print("------------------------------------------")



         # Here we are Deleteing the addresss


        elif choice == 3 :
           print("---------------------------------------------------------------")
           print("*************DELETE ADDRESS***************")
           print("---------------------------------------------------------------")

           mycursor=mydatabase.cursor()
           HouseHolderName=input("Enter the house holder name whoes information you want to delete :-->")
           sql = "delete from StoreAddressbook where householdername = %s "
           mycursor.execute(sql,HouseHolderName)
           mydatabase.commit()
           print("\t\t\t!!!!Record deleted successfully !!!!")
           print("------------------------------------------")

        elif choice == 4 :
             break

        else:
             print("\t\t\t!!!! Invalid Input !!!!")
             print("please enter the correct number")


except:
       print("You commit mistake Please do it agin")
















