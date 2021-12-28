import pickle
def employee_input():
    employee = {}
    employee['passport'] = input('Passport data: ').split(' ')
    employee['education'] = input('Education: ')
    employee['speciality'] = input('Speciality: ')
    employee['position']=input('Position: ')
    employee['money']=input('Money: ')
    with open('emp_file.txt','wb') as file:
        pickle.dump(employee,file)
    return employee
def list_of_employee():
    n = int(input('Count of employee: '))
    return [employee_input() for i in range(n)]
def search_employee(employee_list, employee_name):
    return list(filter(lambda employee: employee['song'] == employee_name, employee_list))
employee_list = list_of_employee()

employee_name = input('Employee for search: ')
res = search_employee(employee_list, employee_name)
if len(res) > 0:
    print(res)
else:
    print('No result')