dic = {
    "moez bouhamed":{"sexe":"men","age":55 , "number":25413109 ,"nationality":"tunisien"},
    "raafa khrouf":{"sexe":"women","age":46 , "number":27613883 ,"nationality":"tunisienne"},
    "mariem bouhamed":{"sexe":"women","age":22 , "number":27958820 ,"nationality":"tunisienne"},
    "ahmed bouhamed":{"sexe":"men","age":16 , "number":27451991 ,"nationality":"tunisien"}
}
name =input ("give me noun of a member of your family \n")
if name in dic :
    print (dic[name])
else : 
    print ("error this name is not dispo")