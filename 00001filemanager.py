class filemanage:
    def read(self):
        try:
            x=open("description.txt","rt")
        except FileNotFoundError as e:
            print("error is",e)
        else:
            x=open("description.txt","rt")
            print(f"value is:{x.read()}")
        finally:
            print("done")
    def write(self,a):
        try:
            x=open("description.txt","w")
        except FileNotFoundError as e:
            print("error is",e)
        else:
            x.write(a)
        finally:
            print("done")
    def append(self,a):
        try:
            x=open("description.txt","a")
        except FileNotFoundError as e:
            print("error is",e)
        else:
            x.write(a)
        finally:
            print("done")

    

file=filemanage()
op = input(f"Enter your operation: \n"
           "Enter 1: read\n"
           "Enter 2: write\n"
           "Enter 3: append\n")

if op=="1" or op.lower=="read":
    file.read()
elif op=="2" or op.lower=="write":
    a=input("enter your value to write: ")
    file.write(a)
else:
    a=input("enter your value to append: ")
    file.append(a)
