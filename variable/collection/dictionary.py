# a collection of{key:value} pairs
#ordered and changable .No duplicates
capitals={"USA":"Washington D.C",
          "India":"Delhi",
          "Bangladesh":"Dhaka",
          "China":"Beijing"}
print(capitals.get("Bangladesh"))

if capitals.get("China"):
    print("That capital exists")
else:
    print("That capital doesn't exists")
    
#update
capitals.update({"Germany":"Berlin"})
capitals.update({"Bangladesh":"Barishal"})
#remove
capitals.pop("China")
capitals.popitem() #remove the latest insert 

print(capitals)
#get the keys
key =capitals.keys()
print(key)
for key in capitals.keys():
 print(key)
#get the values
values = capitals.values()
print(values)
for value in capitals.values():
    print(value)
    
#item method
itmes = capitals.items()
print(itmes)

for key , value in capitals.items():
 print(f"{key} : {value}")