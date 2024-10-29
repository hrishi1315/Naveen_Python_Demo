a = "Matt John, Pet Hous"

abc = a.split()
abc[-3],abc[-4] = abc[-4], abc[-3]

output = ' '.join(abc)
print(output)

def f(n):
    if n==0: return 0
    elif n==1: return 1
    else:return f(n-1)+f(n-2)

for i in range(0,10):
    print(f(i))


def print2largest(sc, sc_size):

    sc.sort(reverse=True)

    for i in range(1, sc_size):

        if (sc[i] != sc[0]):
            print("The second largest element is", sc[i])
            return
            print("There is no second largest element")

sc = [12, 35, 1, 10, 34, 1]
n = len(sc)
print2largest(sc, n)


for i in range(9, 1, -1):
    print(i)

num1 = [1,3,5]
num2 = [1,3,5]
for i,k in zip(num1,num2):
    print(i,k)

l = [3,2,1]
l.reverse()
print(l)

o = [1,4,7,3,2]
o.sort()
print(o)
o.sort(reverse=True)
print(o)

m = ["d", "g", "a", "k", "z"]
m.sort()
print(m)
m.sort(reverse=True)
print(max(m))

b = "abc"
print(b[0:2])
b += " xyz "
print(b)

nc = "BANK SBI"
an = nc.split()
an[-1], an[-2] = an[-2], an[-1]
an = ' '.join(an)
print(an)


txt = ('a','n','c','d')
v = slice(3)
print(txt[v])


list1 = [10, 20, 4, 45, 99]
print("Largest element is:", max(list1))

#Interview asked
my_list = [i for i in range(3)]
print(my_list)
my_first_list = [0, 1]
my_second_list = [0, 1, 2]
print(my_first_list + my_second_list)

my_list = [1, 2, 3, 4]
new_list = my_list[2:]
print(new_list)

x = True
y = False
print(x or y)


