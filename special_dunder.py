

##  __str__
##------------------------------------------------------------

class Book:
    def __init__(self,n,p,a):
        self.name=n
        self.price=p
        self.author=a

    def __str__(self):
        return self.name+' '+self.author

python=Book('pyhton',1000,'Van Guido Rossum')
django=Book('Django',5000,'Abcd')
print(python)







##  __del__
##------------------------------------------------------------------------------

class Book:
    def __init__(self,n,p,a):
        self.name=n
        self.price=p
        self.author=a

    def __del__(self):
        print("__del__ is called")

python=Book('pyhton',1000,'Van Guido Rossum')
django=Book('django',5000,'Abcd')
print(python)
del python













## Example:-
class Employee:
    company_name='JSP'
    company_ceo='ABD'
    emp_count=0
    def __init__(self,n,i,s,e):
        self.Ename=n
        self.Eid=i
        self.Esalary=s
        self.Eexperience=e
        Employee.emp_count+=1
    def __del__(self):
        print(self,'is deleted')
        Employee.emp_count-=1
    def __str__(self):
        return self.Ename
tushar=Employee('Tushar',1234,50000,5)
arnab=Employee('Arnab',4567,10000,2)

print(Employee.emp_count)
print(tushar.emp_count)
print(arnab.emp_count)

del arnab
print(Employee.emp_count)
print(tushar.emp_count)

