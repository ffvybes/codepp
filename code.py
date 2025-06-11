print ("this is my second version")


import requests

info = requests.get("http://api.github.com/repos/kubernetes/kubernetes/pulls")

all_details = info.json
for i in range (len(all_details)):

print (all_details[i] ["user"] ["id"])


def contnum(n):
    num = 1 

    for i in range(0, n):
        for j in range (0, i + 1):
            print(num, end=" ")
            num = num + 1
            print("\r")

n = 5
contnum(n)

aTuple = ("orange", "mango", "apple",)

print(aTuple)

my_s = "python"
result =my_s[::-2]
print(result)



   0