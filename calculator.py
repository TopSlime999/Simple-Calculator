""" Each Tested method will have a certain code that goes with it for ultimate testing.
produced my Mr. Waltz
Date: feb 15  - Vr 2 feb 20, 2023 (To be added: Psuedoparser)
Reason: I just kinda want a fun wittle calculator. """

#Variables and stuff  
equation = input("> ")
def wrap(equation):
    listed = []
    for l in equation:
        listed.append(l)
    print(listed)
    return(listed)

listed = wrap(equation) # All of above works.

def unwrap(listed):
    first_half = str()
    second_half = str()
    ops = ['x','/','-','+', '^']
    used = str()
    second_half_write = False
    for x in listed:
        if x.isdigit():
            if not second_half_write:            
                first_half += str(x)
            else:
                second_half += str(x)
            #listed.remove(x)
        elif x in ops:
            used = str(x)
            second_half_write = not second_half_write
    
    equation = {
        "first_half" : first_half,
        "second_half" : second_half,
        "operator": used
    }
    
    return(equation)
        
        

       
output = unwrap(listed)
listed, first_half, second_half = output
print(output["operator"] )

def runner(equation: dict):
    
    if output["operator"] == '+':
        print(int(output["first_half"]) + int(output["second_half"]) )
    elif output["operator"] == '-':
        print(int(output["first_half"]) - int(output["second_half"]) )
    elif output["operator"] == '/':
        print(int(output["first_half"]) / int(output["second_half"]) )
    elif output["operator"] == '^':
        print(int(output["first_half"]) ** int(output["second_half"]))
    elif output["operator"] == 'x':
        print(int(output["first_half"]) * int(output["second_half"]) )
    
    
runner(output)

# print(eval(output["first_half"] + output["operator"] + output['second_half']))
# Simple but unsafe...          

