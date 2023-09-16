def employee(emp_id):
    x = check_hr(emp_id)
    if(not x):
        name = emp_name(emp_id)
        print("Welcome {} !!".format(name))
        while(True):
            print("Enter 1 to view own Details\nEnter 2 to view all HR names\nEnter q to exit")
            a = input("Enter your option: ")
            if(a == '1'):
                view_own_details(emp_id)
            elif(a == '2'):
                all_hr_names()
            elif(a =='q'):
                print("Thanks Employee")
                break
    else:
        print("Welcome {} from HR!!".format(emp_name(emp_id)))
        while(True):
            print("Enter 1 to view own details\nEnter 2 to view All employees\nEnter q to exit")
            b = input("Enter your option: ")
            if(b == '1'):
                view_own_details(emp_id)
            elif(b == '2'):
                all_emp_name()
                designation()                          
            elif(b == 'q'):
                print("Thanks HR")
                break
                


def all_emp_name():
    file=open("employee.txt",'r')
    line =file.readlines()
    for m in line:
        v = m.split(',')
        print("ID = {}\tName = {}\tDesignation = {}".format(v[0],v[1],v[3]))
    
    file.close()
    
def designation():
    file=open("employee.txt",'r')
    line =file.readlines()
    lst1=[]
    x =[]
    for i in line:
            j = i.split(',')
            x.append(j[3])
    print("Designations are:")
    for i in x:
        if i not in lst1:
            lst1.append(i)
    for i in lst1:
        print(i)
    print("All(to display details of all employees)")
    count=0
    des =input("Enter the designation to search for: ")
    if des != 'All':
        for m in line:
            v = m.split(',')
            if(v[3] == des):
                print("Employee id= {}\nName= {}\nDOJ = {}\nDesignation= {}\nSalary= {}".format(v[0],v[1],v[2],v[3],v[4]))
            #else:
                #count = 1
    else:
        for m in line:
            v = m.split(',')
            print("Employee id= {}\nName= {}\nDOJ = {}\nDesignation= {}\nSalary= {}".format(v[0],v[1],v[2],v[3],v[4]))
    #if(count == 1):
        #print("Wrong Designation Inputted")
    file.close()

def emp_name(emp_id):
    file=open("employee.txt",'r')
    line =file.readlines()
    for m in line:
        v = m.split(',')
        if(emp_id == v[0]):
            return v[1]
    
    file.close()



def check_hr(emp_id):
    emp_file = open("employee.txt",'r')
    hr_file = open("hr.txt",'r')
    emp_lines = emp_file.readlines()
    hr_lines = hr_file.readlines()
    # print(emp_lines)
    flag = 0
    for i in emp_lines:
        for j in hr_lines:
            x = i.split(',')
            y = j.split(',')
            if(emp_id == x[0] == y[0]):
                return True
                flag = 1
                break
    if(flag == 0):
        return False
    emp_file.close()
    hr_file.close()

def view_own_details(emp_id):
    file=open("employee.txt",'r')
    line =file.readlines()
    for i in line:
        j = i.split(',')
        if(j[0] == emp_id):
            print("Employee ID  = {}\nName= {}\nDOJ = {}\nDesignation= {}\nSalary= {}".format(j[0],j[1],j[2],j[3],j[4]))
            break
    file.close()



def all_hr_names():
    emp_file = open("employee.txt",'r')
    hr_file = open("hr.txt",'r')
    emp_lines = emp_file.readlines()
    hr_lines = hr_file.readlines()
    for i in emp_lines:
        x = i.split(',')
        for j in hr_lines:
            y = j.split(',')
            if(x[0] == y[0]):
                print("Department = {}\nHR Name = {}\nHR Role = {}".format(y[1],x[1],y[2]))

    
 