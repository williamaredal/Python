# values kan representere informasjon algoritmen henter inn
values = [1000, 500, 100, 50, 5]
total_0 = 0
total_1 = 0

# funksjon som adderer eller subtraherer informasjonen dynamisk og kommer med en "konklusjon" i form av total
for i in range(len(values)-1):
    if values[i] < values[i+1]:
        total_0 -= values[i]
    else:
        total_0 += values[i]

print(len(values)-1)
print(total_0)

# total invers av forrige funksjon ettersom if og else er bundet og avhenger av '<' og '>'
for n in range(len(values)-1):
    print(values[n])
    if values[n] > values[n+1]:
        total_1 -= values[n]
    else:
        total_1 += values[n]
        
print(len(values)-1)
print(total_1)
