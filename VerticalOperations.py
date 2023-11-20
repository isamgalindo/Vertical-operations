def arithmetic_arranger(problems, ans = False):

    # As requested, if there are more than five problems, the function will return the error: "Error: Too many problems"
    if len(problems) > 5:
        return "Error: Too many problems."
    
    f_numbers = []
    op_and_s_numbers = []
    line = []
    results = []
    
    for a in problems:
        # There are three elements in each problem: first number, operator and secod number. If there is more than three, the problem is invalid and the function will return the error: "Error: Invalid problem." 
        if len(a.split()) != 3:
            return "Error: Invalid problem."
        
        first_number = a.split()[0]
        operator = a.split()[1]
        second_number = a.split()[2]
        
        # If the first or second number has a character that is not numeric, the function will return the error: "Error: Number must only contain digits."
        if not first_number.isnumeric() or not second_number.isnumeric():
            return "Error: Numbers must only contain digits."
        
        # As requested, if either of the number has more than 4 digits, gthe function will return the error: "Error: Numbers cannot be more than four digits."
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        

        # Takes into account which number is bigger to correctly right align.
        max_length = max(len(first_number), len(second_number)) + 2
        
        f_numbers.append(first_number.rjust(max_length))
        
        op_and_s_numbers.append(operator + second_number.rjust(max_length - 1))
        
        line.append("-" * max_length)

        if ans:
           result = ""
           if operator == "+":
               result = str(int(first_number) + int(second_number))
           elif operator == "-":
               result = str(int(first_number) - int(second_number))
           else:
               #As requested, If the operator is neither "+" nor "-", the function it will return the error: "Error: Operator must be '+' or '-'."
               return "Error: Operator must be '+' or '-'."
           results.append(result.rjust(max_length))
        
    
    arranged_problems = ""
    arranged_problems += "    ".join(f_numbers) + "\n"
    arranged_problems += "    ".join(op_and_s_numbers) + "\n"
    arranged_problems += "    ".join(line)
    
    if ans:
        arranged_problems += "\n" + "    ".join(results)
    
    return arranged_problems
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], False))
