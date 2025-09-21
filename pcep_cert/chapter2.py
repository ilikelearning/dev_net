print("Hello World!", end=" ")
print("How are you,today?")

print("Hello", "World!", sep=",")

print("Programming","Essesntials","in", sep="***", end="...")
print("Python")

a = f"    *"
b = f"   * *"
c = f"  *   *"
d = f" *     *"
e = f"***   ***"
f = f"  *   *"
g = f"  *   *"
h = f"  *****"

print("\n",a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h)
print("Decimal for Octal number 0o123 is",0o123, "and that of Hex number, 0x123 is ", end="")
print(0x123)
print(bin(11))
print(0b1011)
print(0.4)
print(2e5)
print(0.0000000000000000000000000001)
print(True > False)
print(True < False)
print("\"I\'m\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

print(9.0//2) 
print(25%13)
print(-4.0 + 8)
print(f'{6.0/2:.6f}')
print(2+3*5)
print(2**5*2)
print(9%6%2)
print(2**2**3)
print(2*3%5)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print(-13 // 4)
print(1%-4)
print(5%4)

john = 3
mary = 5
adam = 6
print(john,mary,adam, sep=",")
total_apples = john+mary+adam
print(f'Total number of apples: {total_apples}')

kilometers = 12.25
miles = 7.38
miles_to_kilometers = 1.61 * miles
kilometers_to_miles = kilometers / 1.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#x = input("Type your input: ")
#x = float(x)
#y = ((3*x**3)-(2*x**2)+(3*x)-1)
#print(f"y= {y}")

#x = float(input("Enter value for x: "))
#y = 1/(x+(1/(x+(1/(x+(1/x))))))
#print("y =", y)

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
end_time = (hour*60) + mins  + dura
end_hour = (end_time // 60) % 24
end_min = end_time % 60
print(f'The event will end at {end_hour}:{end_min}')
print(0)