for ([expresion-inicial]; [condicion]; [expresion-final])

letters = ['a', 'b', 'c', 'd', 'e']
reversed_letters = []
for i in range(len(letters)-1, -1, -1):
    reversed_letters.append(letters[i])
print(reversed_letters)   
 
 
range_number2= range(11,1,-1)
for i in range_number2:
    print(i)
print(type(range_number2))    
 

 number = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
total=0
for i in number:
    total+= i
print(total)  