import Employee

# Main function
def main():

    # Calls the get super visor function
    contractor = getContractor()

    # Displays all the user entered information
    displayContractor(contractor)

# Function to get supervisor data from the user
def getContractor():

    # Input
    name = input('Enter the contractor name: ')
    id = int(input('Enter the contractor ID number: '))
    department = input('Enter the contractor department: ')
    job_title = input('Enter the contractor job title: ')
    contractenddate = (input('Enter the contract end date: '))
    ABN = int(input('Enter the contractor ABN: '))
    fixedsalary = float(input('Enter the contractor fixed salary: '))
    print()

    # Creates the shift supervisor object and stores the data
    contractor = Employee.Contractor(name, id, department, job_title, contractenddate, ABN, fixedsalary)
    return contractor

# Function to display the information
def displayContractor(contractor):

    #Output
    print('Contractor Details:')
    print('---------------------')
    print('Name:', contractor.get_name())
    print('ID number:', contractor.get_id())
    print('Department:', contractor.get_department())
    print('Job Title:', contractor.get_job_title())
    print('Contract end date:', contractor.get_contractenddate())
    print('ABN: ', (contractor.get_ABN())
    print('Fixed Salary: $',(contractor.get_fixedsalary(),',.2f'), sep='')

# Calls the main function
main()
