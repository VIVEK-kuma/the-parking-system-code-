#parking management system
import random
class Parking_system:
    def __init__(self):
        self.two=[1,2,3,4,5,6,7,8,9,10]
        self.light_w=[11,12,13,14,15,16,17,18,19,20]
        self.bus_t=[21,22,23,24,25,26,27,28,29,30]
        self.other_v=[31,32,33,34,3,36,37,38,39,40]
        
    #For input of two Wheeler van

    def two_wheeler(self):
        name1=input("Enter Owner Name\n")
        mobile_no=input("Mobile Number\n")
        van_no=input("Van Number\n")
        id_name=input("Identity proof\n")
        id_number=input("Identity Number\n")
        for i in self.two:
            if(i in [1,2,3,4,5,6,7,8,9,10]):
                print(i,end="  ")
        print("Slots are available\n")
        k=[name1,mobile_no,van_no,id_name,id_number]
        slot=int(input("Enter your slot number\n"))
        self.two[slot-1]=k
        
    #Availability Check for the Two wheeler
    def two_avail(self):
        k=self.two
        count=0
        for i in k:
            if(i in [1,2,3,4,5,6,7,8,9,10]):
                print(i,end=" ")
                count=1
        if(count==1):
            print("are available slots\n")
            ask=input("Do you want to park your vehicle sir?")
            if(ask=="yes"):
                self.two_wheeler()
        else:
            print("Sorry,We don't have any slots\n")
            
    #Delivery of two wheeler van
    def two_deli(self):
        name1=input("Enter Owner Name\n")
        mobile_no=input("Mobile Number\n")
        van_no=input("Van Number\n")
        id_name=input("Identity proof\n")
        id_number=input("Identity Number\n")
        new_del=[name1,mobile_no,van_no,id_name,id_number]
        if(new_del in self.two):
            print("Your vehicle is ready for depart\n")
            self.two.remove(new_del)
        else:
            print("Sorry Sir! Your vehicle is not here\n")
        
    #Display of the entire available vehicles
    def two_display(self):
        print("Owner Name\t\t\tMobile Number\t\t\tVan Number\t\t\tIdentity Proof\t\t\tIdentity Number\n")
        for i in self.two:
            if(i not in [1,2,3,4,5,6,7,8,9,10]):
                for j in i:
                    print(j,end="\t\t\t")
                print()
    #For input of light_weight van   
        
    def light_weight(self):
        name1=input("Enter Owner Name\n")
        mobile_no=input("Mobile Number\n")
        van_no=input("Van Number\n")
        id_name=input("Identity proof\n")
        id_number=input("Identity Number\n")
        for i in self.light_w:
            if(i in [11,12,13,14,15,16,17,18,19,20]):
                print(i,end="  ")
        print("Slots are available\n")
        k=[name1,mobile_no,van_no,id_name,id_number]
        slot=int(input("Enter your slot number\n"))
        self.light_w[slot-11]=k
        
    #availability of light weight vehicle
    def light_weight_avail(self):
        k=self.light_w
        count=0
        for i in k:
            if(i in [11,12,13,14,15,16,17,18,19,20]):
                print(i,end=" ")
                count=1
        if(count==1):
            print("are available slots\n")
            ask=input("Do you want to park your vehicle sir?")
            if(ask=="yes"):
                self.light_weight()
        else:
            print("Sorry Sir!,We don't have any slots\n")
    

        
    #ddilevery of light weight vehicle
    def light_weight_deli(self):
        name1=input("Enter Owner Name\n")
        mobile_no=input("Mobile Number\n")
        van_no=input("Van Number\n")
        id_name=input("Identity proof\n")
        id_number=input("Identity Number\n")
        new_del=[name1,mobile_no,van_no,id_name,id_number]
        if(new_del in self.light_w):
            print("Your vehicle is ready for depart\n")
            self.light_w.remove(new_del)
        else:
            print("Sorry Sir! Your vehicle is not here\n")
            
    #light weight display
    def light_weight_display(self):
        print("Owner Name\t\t\tMobile Number\t\t\tVan Number\t\t\tIdentity Proof\t\t\tIdentity Number\n")
        for i in self.light_w:
            if(i not in [11,12,13,14,15,16,17,18,19,20]):
                for j in i:
                    print(j,end="\t\t\t")
                print()


    #For input of Bus or Truck    
        
    def Bus_Truck(self):
        name1=input("Enter Owner Name\n")
        mobile_no=input("Mobile Number\n")
        van_no=input("Van Number\n")
        id_name=input("Identity proof\n")
        id_number=input("Identity Number\n")
        for i in self.bus_t:
            if(i in [21,22,23,24,25,26,27,28,29,30]):
                print(i,end="  ")
        print("Slots are available\n")
        k=[name1,mobile_no,van_no,id_name,id_number]
        slot=int(input("Enter your slot number\n"))
        self.bus_t[slot-21]=k

    #availability of Bus truck
    def Bus_Truck_avail(self):
        k=self.bus_t
        count=0
        for i in k:
            if(i in [21,22,23,24,25,26,27,28,29,30]):
                print(i,end=" ")
                count=1
        if(count==1):
            print("are available slots\n")
            ask=input("Do you want to park your vehicle sir?")
            if(ask=="yes"):
                self.Bus_Truck()
        else:
            print("Sorry Sir!,We don't have any slots\n")
        
        
    #delivery of Bus Truck
    def Bus_Truck_deli(self):
        name1=input("Enter Owner Name\n")
        mobile_no=input("Mobile Number\n")
        van_no=input("Van Number\n")
        id_name=input("Identity proof\n")
        id_number=input("Identity Number\n")
        new_del=[name1,mobile_no,van_no,id_name,id_number]
        if(new_del in self.bus_t):
            print("Your vehicle is ready for depart\n")
            self.bus_t.remove(new_del)
        else:
            print("Sorry Sir! Your vehicle is not here\n")
            
    
    #display of the Bus Truck vehicle
    def Bus_Truck_display(self):
        print("Owner Name\t\t\tMobile Number\t\t\tVan Number\t\t\tIdentity Proof\t\t\tIdentity Number\n")
        for i in self.bus_t:
            if(i not in [21,22,23,24,25,26,27,28,29,30]):
                for j in i:
                    print(j,end="\t\t\t")
                print()
    
    #For input of other van   
    def Other_Van(self):
        name1=input("Enter Owner Name\n")
        mobile_no=input("Mobile Number\n")
        van_no=input("Van Number\n")
        id_name=input("Identity proof\n")
        id_number=input("Identity Number\n")
        for i in self.other_v:
            if(i in [31,32,33,34,35,36,37,38,39,40]):
                print(i,end="  ")
        print("Slots are available\n")
        k=[name1,mobile_no,van_no,id_name,id_number]
        slot=int(input("Enter your slot number\n"))
        self.other_v[slot-31]=k



    #Availability Check
    def Other_Van_avail(self):
        k=self.other_v
        count=0
        for i in k:
            if(i in [31,32,33,34,35,36,37,38,39,40]):
                print(i,end=" ")
                count=1
        if(count==1):
            print("are available slots\n")
            ask=input("Do you want to park your vehicle sir?")
            if(ask=="yes"):
                self.Other_Van()
        else:
            print("Sorry Sir!,We don't have any slots\n")
    
    
    #Delivery of the vehicle
    def Other_Van_deli(self):
        name1=input("Enter Owner Name\n")
        mobile_no=input("Mobile Number\n")
        van_no=input("Van Number\n")
        id_name=input("Identity proof\n")
        id_number=input("Identity Number\n")
        new_del=[name1,mobile_no,van_no,id_name,id_number]
        if(new_del in self.other_v):
            print("Your vehicle is ready for depart\n")
            self.other_v.remove(new_del)
        else:
            print("Sorry Sir! Your vehicle is not here\n")
    

    #Display the available vehicles
    def Other_Van_display(self):
        print("Owner Name\t\t\tMobile Number\t\t\tVan Number\t\t\tIdentity Proof\t\t\tIdentity Number\n")
        for i in self.other_v:
            if(i not in [31,32,33,34,35,36,37,38,39,40]):
                for j in i:
                    print(j,end="\t\t\t")
                print()



obj=Parking_system()
while(1):
    print("\n\n")
    print("A.Entry ",end="\t")
    print("B.Delivery",end="\t")
    print("C.Availability Check",end="\t")
    print("D.Display",end="\t")
    print("E.Exit")
    print("Enter your choice\n")
    num=input()
    if(num=="A" or num=="a"):
        while(1):
            print("\n\n")
            print("1.Two Wheeler",end="\t")
            print("2.Light Weight Van",end="\t")
            print("3.Bus and Truck",end="\t")
            print("4.Other Van",end="\t")
            print("5.Exit",end="\t")
            print("\n\n")
            print("Enter your choice\n")
            num=int(input())
            if(num==1):
                obj.two_wheeler()
            elif(num==2):
                #For light Weight van
                obj.light_weight()
            elif(num==3):
                #for Bus and Truck
                obj.Bus_Truck()
            elif(num==4):
                # For Other van
                obj.Other_Van()
            elif(num==5):
                break
            else:
                print("Please make Right Choice\n")
    elif(num=="C" or num=="c"):
        while(1):
            print("\n\n")
            print("1.Two Wheeler",end="\t")
            print("2.Light Weight Van",end="\t")
            print("3.Bus and Truck",end="\t")
            print("4.Other Van",end="\t")
            print("5.Exit",end="\t")
            print("\n\n")
            print("Enter your choice\n")
            num=int(input())
            if(num==1):
                obj.two_deli()
            elif(num==2):
                #For light Weight van
                obj.light_weight_deli()
            elif(num==3):
                #for Bus and Truck
                obj.Bus_Truck_deli()
            elif(num==4):
                # For Other van
                obj.Other_Van_deli()
            elif(num==5):
                break
            else:
                print("Please make Right Choice\n")
    elif(num=="B" or num=="b"):
        #availability
        while(1):
            print("\n\n")
            print("1.Two Wheeler",end="\t")
            print("2.Light Weight Van",end="\t")
            print("3.Bus and Truck",end="\t")
            print("4.Other Van",end="\t")
            print("5.Exit",end="\t")
            print("\n\n")
            print("Enter your choice\n")
            num=int(input())
            if(num==1):
                obj.two_avail()
            elif(num==2):
                #For light Weight van
                obj.light_weight_avail()
            elif(num==3):
                #for Bus and Truck
                obj.Bus_Truck_avail()
            elif(num==4):
                # For Other van
                obj.Other_Van_avail()
            elif(num==5):
                break
            else:
                print("Please make Right Choice\n")
    elif(num=="D" or num=="d"):
        while(1):
            print("\n\n")
            print("1.Two Wheeler",end="\t")
            print("2.Light Weight Van",end="\t")
            print("3.Bus and Truck",end="\t")
            print("4.Other Van",end="\t")
            print("5.Exit",end="\t")
            print("\n\n")
            print("Enter your choice\n")
            num=int(input())
            if(num==1):
                obj.two_display()
            elif(num==2):
                #For light Weight van
                obj.light_weight_display()
            elif(num==3):
                #for Bus and Truck
                obj.Bus_Truck_display()
            elif(num==4):
                # For Other van
                obj.Other_Van_display()
            elif(num==5):
                break
            else:
                print("Please make Right Choice\n")
        #display of available Vans
    elif(num=="E" or num=="e"):
        break
    else:
        print("Wrong Choice\n")
