"""salary = int (input("enter annual salary"))"""
def tax_relief(salary = int (input("enter annual salary"))):
    if salary > 200000:
        return((0.01*salary) + (0.2*salary))
    else:
        return(200000 + (0.2*salary))
print(tax_relief)
"""gross_salary = input("enter annual salary ")
print(int(gross_salary + 50000))"""