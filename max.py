r1=int(input("Road 1"))
r2=int(input("Road 2"))
r3=int(input("Road 3"))
r4=int(input("Road 4"))

if ((r1>=r2 and r1>=r3) and r1>=r4) or (r1>=r2 and (r1>=r3 and r1>=r4)):
    max=r1
    print("ROad 1 is largest --> ",max)
elif ((r2>=r1 and r2>=r3) and r2>=r4) or (r2>=r1 and (r2>=r3 and r2>=r4)):
    max=r2
    print("Road 2 is largest --> ",max)
elif ((r3>=r1 and r3>=r2) and r3>=r4) or (r3>=r1 and (r3>=r3 and r3>=r4)):
    max=r3
    print("Road 3 is largest --> ",max)
elif ((r4>=r1 and r4>=r3) and r4>=r3) or (r4>=r1 and (r4>=r3 and r4>=r3)):
    max=r4
    print("Road 4 is largest --> ",max)

