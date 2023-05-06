Vehicle = {}
slots = [i for i in range(1, 41)]

def main():
    print("----------------------------------------------------------------------------------------")
    print("\t\tParking System")
    print("----------------------------------------------------------------------------------------")
    try:
        while True:
            print("1.Vehicle Entry")
            print("2.Remove Entry")
            print("3.View Parked Vehicle")
            print("4.Close Programme")
            print("+---------------------------------------------+")
            ch=int(input("Select option:"))
            if ch==1:
                no=True
                while no==True:
                    print("\tpress '*' to go back to previous menu")
                    Vno=input("\tEnter vehicle number (XXXX) - ").upper()
                    if Vno=="" or Vno is None:
                        pass
                    elif Vno == "*":
                        no=not True
                    elif Vno in Vehicle:
                        print("\t!!!!Vehicle Number Already Exists")
                    elif len(Vno)==4:
                        no=not True
                        if len(Vehicle) == 40:
                            print("\t!!!!No space availble!!")
                        else:
                            slot = slots.pop(0)
                            level = "A" if slot//21 == 0 else "B"
                            Vehicle[Vno] = {"level":level, "spot":slot}
                    else:
                        print("\t###### Enter Valid Vehicle Number ######")
                
                print("\t....................Record detail saved..........................")

            elif ch==2:
                no=True
                while no==True:
                    print("\tpress '*' to go back to previous menu")
                    Vno=input("\tEnter vehicle number to Delete(XXXX) - ").upper()
                    if Vno=="" or Vno is None:
                        pass
                    elif Vno == "*":
                        no=not True
                    elif len(Vno)==4:
                        if Vno in Vehicle:
                            slots.append(Vehicle[Vno]["spot"])
                            del Vehicle[Vno]
                            no=not True
                            print("\t...................Removed Sucessfully...................")
                        elif Vno not in Vehicle:
                            print("\t...................No Such Entry...................")
                        else:
                            print("\tError")
                    else:
                        print("\t###### Enter Valid Vehicle Number ######")

            elif ch==3:
                print("\tpress '*' to go back to previous menu")
                Vno=input("\tEnter vehicle number to Find Spot(XXXX) - ").upper()
                if Vno=="" or Vno is None:
                    pass
                elif Vno == "*":
                    no=not True
                elif len(Vno)==4:
                    if Vno in Vehicle:
                        print(f'\tVehicle {Vno} is parked at level:{Vehicle[Vno]["level"]} and spot:{Vehicle[Vno]["spot"]}')
                    elif Vno not in Vehicle:
                        print("\t...................No Such Entry...................")
                    else:
                        print("\tError")
                else:
                    print("\t###### Enter Valid Vehicle Number ######")
                
            elif ch==4:
                print("...................Thank you for using our service...................")
                break
                quit
    except:
        main()
main()
