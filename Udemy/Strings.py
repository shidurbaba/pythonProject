str = "RahulShettyAcademy.com"
str1 = "Consulting Firm"
str2 = "Moses Pie"
str3 = "RahulShetty"
str4 = "great "
#Substring

print(str[0:5])

#Concatenate

print(str,str1,str2)

#Validation Opertation - True or False

print(str2 in str) # return false
print(str3 in str) #return true

#Split and trim

var = str.split(".")
print(var) #return a list
print(var[0]) #returns value from zeroth index

print(str4.strip()) #default trim
print(str4.lstrip()) #left trim
print(str4.rstrip()) #right trim


