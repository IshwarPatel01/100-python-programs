# Mass = Density x Volume.
# Density = Mass ÷ Volume.
# Volume = Mass ÷ Density




mass = int(input("Enter Mass"))
destiny = int(input("Enter destiny"))
volume = int(input("Enter volume"))

result = destiny * volume
result2 = mass / volume
result3 = mass / destiny

print(f"Mass : density * volume = {result}")
print(f"Density : Mass / volume = {result2}")
print(f"Volume : Mass / Density = {result3}")