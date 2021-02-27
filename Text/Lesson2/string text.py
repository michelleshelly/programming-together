number=1
name="mich3"
# this is still considered as a string as all not numbers, unless u state m=1 (like algebra)

print(str(number) + name)
# put str() to convert integer type to string type because equation must be same type
# hierachy of types
# string, float (can be integer too), integer

result=str(number) + name
print(result)
print("my name is", name)
print(f"my name is {name}")
# to put a variable between a statement and not end, have to put f("")
#' and " means the same
print(f"my name {name} is")
    
input(0)
# input will convert everything to string even though it might be a number

# conditional execution
x=1 
y=2
if x==0:
    print("yes its zero")
print("no!, its aint zero")

    
