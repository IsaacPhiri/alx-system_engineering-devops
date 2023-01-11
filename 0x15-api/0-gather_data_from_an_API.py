#!/usr/bin/python3
import json
import sys
import urllib.request

def get_todo_list(employee_id):
    """
    Function to get the todo list for a given employee ID
    :param employee_id: The ID of the employee
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = urllib.request.urlopen(employee_url)
    employee_data = json.loads(employee_response.read())
    employee_name = employee_data.get("name")
    completed_tasks = [task for task in data if task["completed"]]
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(data)}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide an employee ID as a parameter")
    else:
        employee_id = int(sys.argv[1])
        get_todo_list(employee_id)
