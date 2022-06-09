array1 = input("string1: ").split()
array2 = input("string2: ").split()

c = 0
for val1 in array1:
    val1 = val1.lower()
    for val2 in array2:
        val2 = val2.lower()
        if val1 == val2 and val1.isalpha():
            c+=1
if c >= 2:
    print("true")
else:
    print("false")