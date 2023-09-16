def add_employee(emp_id, emp_name, emp_DOJ, emp_designation, emp_salary):
    file1 = open('employee.txt', 'a')
    file2 = open('login.txt', 'a')
    emp = emp_id + ',' + emp_name + ',' + emp_DOJ + ',' + emp_designation + ',' + emp_salary + '\n'
    l = emp_name.split()
    emp_login = emp_id + ' ' + l[0]+'\n'
    file1.writelines(emp)
    file2.writelines(emp_login)
    file1.close()
    file2.close()
    return "Employee added Successfully"


def remove(emp_id, files, s):
    f = open(files, 'r')
    a = f.readlines()
    for i in range(len(a)):
        j = a[i].split(s)
        if j[0] == emp_id:
            a[i] = ''
            break
    f.close()
    f = open(files, 'w')
    f.writelines(a)
    f.close()
def remove_employee(emp_id):
    remove(emp_id, 'employee.txt', ',')
    remove(emp_id, 'hr.txt', ',')
    remove(emp_id, 'login.txt', ' ')
    
    
def check(emp_id):
    flag = False
    file = open("employee.txt", 'r')
    employee = file.readlines()
    for i in employee:
        j = i.split(',')
        if j[0] == emp_id:
            flag = True
    return flag


def add_hr(emp_id, hr_dept, hr_role):
    file = open('hr.txt', 'a')
    hr = emp_id + ',' + hr_dept + ',' + hr_role + '\n'
    file.writelines(hr)
    file.close()
    return "HR added successfully"
def remove_hr(emp_id):
    remove(emp_id, 'hr.txt', ',')
def admin():
    while 1:
        print("Welcome to admin!!")
        print("Enter 1 to add employee\nEnter 2 to remove employee\nEnter 3 to add hr\nEnter 4 to remove hr\nEnter q to "
              "exit")
        c = input("Enter your Option: ")
        if c == '1':
            emp_id = input("Employee ID - ")
            emp_name = input("Employee Name - ")
            emp_DOJ = input("Date of Joining - ")
            emp_designation = input("Designation: ")
            emp_salary = input("Salary: ")
            print(add_employee(emp_id, emp_name, emp_DOJ, emp_designation, emp_salary))
        elif c == '2':
            emp_id = input("Employee ID - ")
            remove_employee(emp_id)
        elif  c == '3':
            emp_id = input("Employee ID - ")
            if (check(emp_id)):
                hr_dept = input("HR Department - ")
                hr_role = input("HR Role ")
                print(add_hr(emp_id, hr_dept, hr_role))
            else:
                print("Employee does not exist")
                break
        elif c == '4':
            emp_id = input("Employee ID - ")
            print("Is he leaving the company totally?")
            y = input("Enter yes or no: ")
            if y == 'yes':
                remove_employee(emp_id)
            else:
                remove_hr(emp_id)
        elif c == 'q':
            break
 

