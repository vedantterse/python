import os


class Employee:
    def __init__(self, EMid, name, joiningDate, department, salary): # EMid is just EMPLOYEE id
        self.EMid = EMid
        self.name = name
        self.joiningDate = joiningDate
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"The details of Employee {self.EMid} are:")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Joining Date: {self.joiningDate}")
        print(f"Salary: {self.salary}")

    def save_to_file(self):
        filename = f"{self.EMid}.txt"
        file_path = os.path.join("employee_data", filename)

        with open(file_path, "w") as file:
            file.write(f"EMid: {self.EMid}\n")
            file.write(f"Name: {self.name}\n")
            file.write(f"Department: {self.department}\n")
            file.write(f"Joining Date: {self.joiningDate}\n")
            file.write(f"Salary: {self.salary}\n")


# Create a directory to store employee data files
os.makedirs("employee_data", exist_ok=True)

# Create a list to store employee objects
employees = []
def load_employees():
    for filename in os.listdir("employee_data"):
        if filename.endswith(".txt"):
            file_path = os.path.join("employee_data", filename)
            with open(file_path, "r") as file:
                lines = file.readlines()
                emp_dict = {}
                for line in lines:
                    key, value = line.strip().split(": ")
                    emp_dict[key] = value
                emp = Employee(emp_dict['EMid'], emp_dict['Name'], emp_dict['Joining Date'], emp_dict['Department'],
                               emp_dict['Salary'])
                employees.append(emp)


# Load existing employees into the list
load_employees()


# Function to add employee details
def add_employee():
    EMid = input("Enter the EMid: ")
    for emp in employees:
        if emp.EMid == EMid:
            print("Employee with the same EMid already exists.")
            return
    name = input("Enter the name: ")
    joiningDate = input("Enter the joining date: ")
    department = input("Enter the department: ")
    salary = input("Enter the salary: ")
    for emp in employees:
        if emp.EMid == EMid:
            print("Employee with the same EMid already exists.")
            return

    emp = Employee(EMid, name, joiningDate, department, salary)
    emp.save_to_file()
    employees.append(emp)
    print("Employee details added successfully!")


# Function to display employee details by EMid
def display_employee_details():
    EMid = input("Enter the EMid to display details: ")
    found = False
    print('\n')
    for emp in employees:
        if emp.EMid == EMid:
            emp.display_details()
            found = True
            break
    print('\n')
    if not found:
        print("Employee not found!")
        print('\n')



def update_employee_details( ):
        EMid = input("Enter the EMid of the employee to modify: ")

        # Check if the file exists
        if os.path.exists(os.path.join("employee_data", EMid + ".txt")):

            # Open the file in write mode
            with open(EMid+".txt", "w") as file:
                print("Enter the new details:")
                name = input("Name: ")
                joiningDate = input("Joining Date: ")
                department = input("Department: ")
                salary = input("Salary: ")

                # Write the updated details to the file
                file.write(f"EMid: { EMid}\n")
                file.write(f"Name: { name}\n")
                file.write(f"Joining Date: { joiningDate}\n")
                file.write(f"Department: { department}\n")
                file.write(f"Salary: { salary}\n")

                print("Employee details updated successfully.")
        else:
            print("Employee not found.")

def print_all_emids():
    print("List of all EMids:")
    for emp in employees:
        print(f'{emp.EMid} : {emp.name}' )
print_all_emids()
    # # Take user input for the specific EMid##
## UNCOMMENT THIS IF YOU WANT TO TAKE USER INPUT TO OPEN A SPECIFIC FILE###
def open_a_specifcFile():
    EMid = input("Enter the EMid to open the employee file: ")
    found = False

    for emp in employees:
        if emp.EMid == EMid:
            emp.display_details()
            found = True
            break

    if not found:
        print("Employee not found!")


# Main loop
print('\n')

while True:
    print('select below options for particular action:-  ')
    print("1. Add Employee")
    print("2. Display Employee Details")
    print("3. modify  Employee Details")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employee_details()
    elif choice=='3':
        update_employee_details()




    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
        print('\n')
