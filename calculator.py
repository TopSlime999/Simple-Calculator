"""
produced my Mr. Waltz
Update: Apr 27, 2023. Added decimals and pi (p)
Date: feb 15  - Vr 2 feb 20, 2023 (To be added: Psuedoparser)
Reason: I just kinda want a fun wittle calculator.
"""

#Variables and stuff  
equation = input("> ")
equation = equation.replace('p', '3.1415926535897932384626')
# converts string into a list.
def wrap(equation: str) -> list:
    listed = []
    for l in equation:
        listed.append(l)
    return(listed)

listed = wrap(equation) # All of above works.

# loops over the list, and gives the data its own variables. 
def unwrap(listed: list) -> dict:
    first_half = str()
    second_half = str()
    ops = ['x','/','-','+', '^']
    used = str()
    second_half_write = False
    for x in listed:
        # switches on operator. 
        if x.isdigit() or x == '.':
            if not second_half_write:            
                first_half += str(x)
            else:
                second_half += str(x)
            #listed.remove(x)
        elif x in ops:
            used = str(x)
            second_half_write = not second_half_write
    
    # returns as dictionary. 
    equation = {
        "first_half" : first_half,
        "second_half" : second_half,
        "operator": used
    }
    
    return(equation)
        
        

       
output = unwrap(listed)
listed, first_half, second_half = output

# runs the above equation
def runner(equation: dict):
    
    if output["operator"] == '+':
        print(float(output["first_half"]) + float(output["second_half"]) )
    elif output["operator"] == '-':
        print(float(output["first_half"]) - float(output["second_half"]) )
    elif output["operator"] == '/':
        print(float(output["first_half"]) / float(output["second_half"]) )
    elif output["operator"] == '^':
        print(float(output["first_half"]) ** float(output["second_half"]))
    elif output["operator"] == 'x':
        print(float(output["first_half"]) * float(output["second_half"]) )
    
    
runner(output)

# print(eval(output["first_half"] + output["operator"] + output['second_half']))
# Simple but unsafe...          

