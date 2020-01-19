b = "sd:asd:ads:u1"
qw =['']
mydict = {
    "u1" : 123,
    "u2" : 234,
    "k3" : 1
}

usersName = (b.split(":")[3].split(","))
print(qw)
print(len(qw))
print(usersName)
for i in usersName:
    for myd in mydict:
        if i == myd:
            print(i)