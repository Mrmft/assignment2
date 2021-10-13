import math

def calc_main(operator, a):
    if operator == 'sum' or operator == '+':
        b = int (input('enter the second nmber: '))
        result = sum(a, b)
        return result
    elif operator == 'sub' or operator == '-' :
        b = int (input('enter the second nmber: '))
        result = subtract(a, b)
        return result
    elif operator == 'mul' or operator == '*' :
        b = int (input('enter the second nmber: '))
        result = muliply(a, b)
        return result
    elif operator == 'div' or operator == '/' :
        b = int (input('enter the second nmber: '))
        result = divide(a, b)
        return result
    #elif operator == 'equation' :
        result = equation()
        return result
    elif operator == 'sin' :
        result = sin(a)
        return result
    elif operator == 'cos' :
        result = cos(a)
        return result
    elif operator == 'tan' :
        result = tan(a)
        return result
    elif operator == 'cot' :
        result = cot(a)
        return result
    elif operator == 'log' :
        result = log(a)
        return result    
    else :
        print('oopps!!! try another command')
    
    
def sum(a, b):
    result = a + b
    print(result)
    return result

def subtract(a, b):
    result = a - b
    print(result)
    return result
    
def muliply(a, b):
    result = a * b
    print(result)
    return result
    
def divide(a, b):
    if b == 0:
        print('oopps wrong choice!!! Try again...')
    else :
        result = a / b
        print(result)
        return result
        
def sin(a):
    degree= math.radians(a)
    result = math.sin(degree)
    print(result)        
    return result
    
def cos(a):
    degree= math.radians(a)
    result = math.cos(degree)
    print(result)  
    return result      
    
def tan(a):
    degree= math.radians(a)
    result = math.tan(degree)
    print(result)    
    return result    

def cot(a):
    result = 1/tan(a)
    print(result)   
    return result     

#def equation():
    equ= input('enter your equation: ')
    result= eval(equ)
    print(result)
    return float(result)

def log(a):
    b = input('enter the base number: ')
    result = math.log(a, b)
    return result
    

    
result_operator = 'no'    
continue_flag = 'yes'
while continue_flag == 'yes' :    
    print('*******welcome to python calculator*******\n1.sum\n2.sub\n3.mul\n4.div\n###5.equation###\n6.sin\n7.cos\n8.tan\n9.cot\n10.log')

    
    if result_operator == 'yes' :
        print('the first number: ', a)
        operator= input('enter your command: ')    
        result = calc_main(operator, a) 
        continue_flag1 = input('if you want to continue enter "yes" else enter "no" to Exit: ')
        if continue_flag1 == 'no':
            continue_flag = 'no'
        if continue_flag == 'yes' :
            result_operator = input('if you want to keep the result enter yes else enter no : ')
            if result_operator == 'yes' :
                a = result
    elif result_operator == 'no' :
        a = int(input('enter the first number/degree: ')) 
        operator= input('enter your command: ')   
        result = calc_main(operator, a)
        continue_flag1 = input('if you want to continue enter "yes" else enter "no" to Exit: ')
        if continue_flag1 == 'no':
            continue_flag = 'no'
        if continue_flag == 'yes' :
            result_operator = input('if you want to keep the result enter yes else enter no : ')
            if result_operator == 'yes' :
                a = result
        
        
        
               