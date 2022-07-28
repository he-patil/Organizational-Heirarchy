class Employee():
    tabCount = 0
    allEmployee = []
    def __init__(self, id, name, designation, reporteeId, dob, salary, reimbursement, attributeX):
        self.id = id
        self.name = name
        self.designation = designation
        self.reporteeId = reporteeId
        self.dob = dob
        self.salary = salary
        self.reimbursement = reimbursement
        self.attributeX = attributeX
        self.subordinates = []

    def addSubordinate(self, employee):
        self.subordinates.append(employee)

    def display(self):
        for i in range(0, Employee.tabCount):
            print("\t",end="")
        
        if Employee.tabCount != 0:
            print("|->",end="")

        print(self.name+" ("+self.designation+")")
        for emp in self.subordinates:
            Employee.tabCount+=1
            emp.display()
            Employee.tabCount-=1

    @staticmethod
    def isIdExist(id):
        for emp in Employee.allEmployee:
            if emp.id == id:
                return True
        return False

    @staticmethod
    def getEmployees(file):
        for line in file.readlines():
            id, name, designation, reportee, dob, salary, reimbursement, attributeX =[x.strip('\'') for x in line.split(",")]
            if not Employee.isIdExist(id):
                employee = Employee(id, name, designation, reportee, dob, salary, reimbursement, attributeX)
                Employee.allEmployee.append(employee)

    @staticmethod
    def getHead():
        i = 0
        while i < len(Employee.allEmployee):
            employee = Employee.allEmployee[i]
            if employee.reporteeId == "NULL":
                head = employee
                Employee.allEmployee.remove(employee)
                i-=1
                head.getOrganization()
                return head
            i+=1

    def getOrganization(self):
        i = 0
        while i < len(Employee.allEmployee):
            employee = Employee.allEmployee[i]
            if employee.reporteeId == self.id:
                sub = employee
                self.addSubordinate(sub)
                Employee.allEmployee.remove(employee)
                i-=1
                sub.getOrganization()
            i+=1

file = open("emp.txt")
Employee.getEmployees(file)
head = Employee.getHead()
head.display()
file.close()

# Emp2 = Employee("Emp2", "Des2", 25)
# Emp3 = Employee("Emp3", "Des2", 40)
# Emp4 = Employee("Emp4", "Des2", 30)
# Emp1 = Employee("Emp1", "Des1", 45, [Emp2, Emp3, Emp4])

# Emp1.display()

################ OUTPUT ########################
# KING-WEB (PRESIDENT)
#         |->BLAKE (MANAGER)
#                 |->MARTIN (SALESMAN)
#                 |->ALLEN (SALESMAN)
#                 |->TURNER (SALESMAN)
#                 |->JAMES (CLERK)
#                 |->WARD (SALESMAN)
#         |->CLARK (MANAGER)
#                 |->MILLER (CLERK)
#         |->JONES (MANAGER)
#                 |->SCOTT (ANALYST)
#                         |->ADAMS (CLERK)
#                 |->FORD (ANALYST)
#                         |->SMITH (CLERK)
################################################