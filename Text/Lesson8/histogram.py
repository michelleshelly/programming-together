bag = ("candy":1, "money":2)
result = None
if "candy" in bag:
    result = bag["candy"]
else:
    result = 20
print(result)

getResult = bag.get("candy",20)
print(getResult)

#get result means get the value if its inside, if not get the default