#ordered and changable,duplicates ok
fruits =["mango","apple","orange","banana","jackfruit","lichi"]
print(fruits[1])
print(fruits[:3]) #print 1st 3 eliments
print(fruits[::2]) #it print every 2nd eliments from 1st 
print(fruits[::-1])  # it print revarce order /:: means list[start:stop:step] 

for fruit in fruits:
    print(fruit)
    
    
print(len(fruits)) #print length of list
print("apple" in fruits) #search eliments in the collection

#methods 
fruits.append("pickale") #add eliments
fruits.remove("orange") #remove eliments
fruits.insert(2,"malta") #add eliments on a index
fruits.sort() #sort
print(fruits)
fruits.reverse() #reverse 
print(fruits)
#fruits.clear() #clear the list
print(fruits)
print(fruits.index("apple")) #print the index number
print(fruits.count("banana"))



