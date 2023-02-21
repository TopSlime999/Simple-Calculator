# Simple-Calculator
A calculator that can run one binary operator. (Multiplication, Division, Addition, Subtraction, Exponentiation)


## Using This
To use this calculator you will need to input an equation using one of these operators, (x: Multiplication, /: Division, ^: Exponetiation, +: Addition, -: Subtraction.), using infix notation. you can include at least one space on each side. Example: 

```bash
> 999 x 999
998001
```

## Design

### wrap
The wrap function converts your equation string into a list, that way it may be tinkered with by the other functions. 

### unwrap
The unwrap function loops over the wrap list, putting the first half, second half, and operator into their own variables then returns those as a dictionary. It does this by switching when it arrives at the operator.

### runner
The runner function just searches for the operator that was used, and does the corerlating math problem. 


