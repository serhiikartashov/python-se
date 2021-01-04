# string concatenation
name = "Serhii "
name += "Kartashov"
print(name)

# f-strings (formatted)
guess = 8
print(f"your guess of {guess} was incorrect!")

print(name[7])
print(name[-2])

# a string in triple quotes can span several lines without using the escape character:

city = """
... Toronto is the largest city in Canada 
... and the provincial capital of Ontario. 
... It is located in Southern Ontario on the 
... northwestern shore of Lake Ontario.
... """
print(city)
