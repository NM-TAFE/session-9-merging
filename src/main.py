import unroll as ur
# Sample python code for github
print("Hello!, Good Morning!")

person=ur.Person()
young=ur.Person("Michael Hepburn")
person.addFriend(young)

person3=ur.Person("Michael OBrien")
person.addFriend(person3)

person4=ur.Person("Ian McMullen")
person.addFriend(person4)

person5=ur.Person("Kaltails David Honey")
person.addFriend(person5)



print(person.friends)