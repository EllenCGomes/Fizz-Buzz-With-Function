def Fizz(x):
    y=x%3
    z=x%5
    if y==0 and z!=0:
        return True
    else:
        return False    

def Buzz(x):
    y=x%3
    z=x%5
    if y!=0 and z==0:
        return True
    else:
        return False 

def FizzBuzz(x):
    y=x%3
    z=x%5
    if y==0 and z==0:
        return True
    else:
        return False 

def fizzbuzz(x):
    Fizz(x)
    Buzz(x)
    FizzBuzz(x)
    if Fizz(x) == True:
        return "Fizz"
    else:
        if Buzz(x) == True:
            return "Buzz"
        else:
            if FizzBuzz(x) == True:
                return "FizzBuzz" 
            else:
                return x       
    