def add(x,y):
    """This function is used for addition of 2 numbers."""
    result= x+y
    print("The result of addition = ",result)
    
def add1(x,y):
    result= x+y
    return result
   
def add2(x,y=10):
    
    result= x+y
    print("The result of addition = ",result)

def add3(*num):
    sum=0
    for i in num:
        sum = sum+i
        
    #print(type(num))
    print("Result = ",sum)

def add4(*num):
    print(num)
    result=list(map(lambda x,y:x+y,num[0],num[1]))
    print(result)
