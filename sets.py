fruits={"apple","banana","orange"}

fruits.add("grapes")

fruits.remove("banana")

print("is apple in set","apple"in fruits)
print("is banana in set","banana"in fruits)


set_length= len(fruits)

print(set_length)

print("Set elements:")
for fruit in fruits:
    print(fruit)


#sets does not allow repetitive value wheras tuple allow

employees = {
    "name": "Bob", "job": "Engineer",
    name: "Sue", "job": "Designer",
    name: "Tom", "job: "Manager"
}
#print(employees[102])

#employees = {"name": "Linda", "job": "HR"}
print(employees)


#for employee in employees:
  #  print(f"Name:{employee["name"]},job:{employee['job']} " )
