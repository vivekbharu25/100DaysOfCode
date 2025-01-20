import art

print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, "-": subtract, "*": multiply, "/":divide
}

def calculator(op,num_1,num_2):
    output = round(operations[op](num_1, num_2),2)
    return output
def part_one():
    num_1 = float(input("First Number:"))
    in_op = input("""Please Choose an operator:\n+\n-\n*\n/ :""")
    num_2 = float(input("Second Number:"))
    out_n = calculator(in_op, num_1, num_2)
    return out_n
def part_two(n):
    in_op = input("""Please Choose an operator:\n+\n-\n*\n/ :""")
    num_2 = float(input("Second Number:"))
    out_n = calculator(in_op, n, num_2)
    return out_n

number_1 = float(input("First Number:"))
input_op =  input("""Please Choose an operator:\n+\n-\n*\n/ :""")
number_2 = float(input("Second Number:"))
output_n  = calculator(input_op,number_1,number_2)
print(f"{number_1} {input_op} {number_2} = {output_n}")

restart  = True
while restart:
    continutiy =  input(f"""Type 'y' to use {output_n} for further calculation,
    'n' to start a new calculation,\notherwise anything to stop calculation""").lower()
    if continutiy  ==   "n":
        print('\n'*20)
        output_n = part_one()
        print(output_n)
        restart  = True
    elif continutiy  ==  "y":
        output_n = part_two(output_n)
        print(output_n)
        restart = True
    else:
        restart = False