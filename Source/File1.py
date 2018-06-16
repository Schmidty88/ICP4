class Employee:

  count=0
  salary=0
# this is wherer i set the employee requirements
  def __init__(self,employee_name,employee_family,employee_salary,employee_dept):
      self.employee_name = employee_name
      self.employee_family = employee_family
      self.employee_salary = employee_salary
      self.employee_dept = employee_dept
      Employee.count+=1
      Employee.salary += employee_salary

  def display(self):
      print("Name:", self.employee_name, "Family:", self.employee_family, "Salary:", self.employee_salary, "Department:", self.employee_dept)


class Fulltime(Employee):
    def __init__(self,n,f,s,d):
        Employee.__init__(self,n,f,s,d)

# inputting names, salary and job
employee1=Employee("Mike","Moses",100000,"App Developer")
employee2=Employee("Dave","Macdonald",95000,"Help Desk")
employee3=Employee("Sam","Gates",87000,"Software Engineer")


employee4=Fulltime("Kate","Reddy",55000,"Hiring Manager")

employee1.display()

print("------Full Time-------")
employee4.display()

print("Total number of employees:", Employee.count)

# finding the average salary for the employee
print("The average salary is:",Employee.salary//Employee.count)