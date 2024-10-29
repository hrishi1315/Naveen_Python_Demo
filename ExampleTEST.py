
a = "Matt John, Pet Hous"

abc = a.split()
abc[-3],abc[-4] = abc[-4], abc[-3]

output = ''.join(abc)
print(output)




