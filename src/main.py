from unroll import Person
# Sample python code for github
print("Hello!, Good Morning!")

patient_zero=Person()
p2=Person("Reece")
patient_zero.addFriend(p2)
p3=Person("Ben")
p2.addFriend(p3)
p4=Person("Ray")
p2.addFriend(p4)
p3.addFriend(p4)

print(patient_zero)
