nums = []

while len(nums) < 5:
    user = int(input("Enter a number"))
    nums.append(user)

print(nums)

if len(nums) == 5:
    pili = input(("Naa ang sir or wala ")).lower()
    if pili == "naa":
        ador = input("Add or Delete? ").lower()
        if ador == "add":
            nadd = int(input("Enter a number to add: "))
            nums.append(nadd)
        elif ador == "delete":
            nums.pop(0)
    elif pili == "wala":
        ador = input("Add or Delete? ").lower()
        if ador == "add":
            nnadd = int(input("Enter a number to add: "))
            nums.append(nnadd)
        elif ador == "delete":
            nums.pop()
else:
    print("Error")
print(nums)
    
