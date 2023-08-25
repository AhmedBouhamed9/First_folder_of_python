pets = {"cat","dog","fish"}
for index, pet in enumerate(sorted(pets)):
    print ( "the pet is ",pet, "has position of ",index)

print(type(pets))
#pets , reverse=true
for index, pet in enumerate(sorted(pets, reverse=True)):
    print ( "the pet is ",pet, "has position of ",index)
nu={2,3,58}
print(min(nu))
print(max(nu))