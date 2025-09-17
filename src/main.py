import unroll as ur
# Sample python code for github
print("Hello!, Good Morning!")

person=ur.Person()
young=ur.Person("Michael Hepburn")
person.addFriend(young)

person3=ur.Person("Other Michael")
person.addFriend(person3)

print(person.friends)