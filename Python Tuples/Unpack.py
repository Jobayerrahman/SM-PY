#Tuple
Fruitstuple = ("apple", "banana", "orange")
print(Fruitstuple)

#Unpacking a Tuple
(apel, kola, komola) = Fruitstuple

print(apel)
print(kola)
print(komola)

#Using Asterisk*
Fruitstuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(Fruitstuple)

(apel,kola,*fol) = Fruitstuple
print(apel)
print(kola)
print(*fol)

(apel, *fol, aamm) = Fruitstuple
print(apel)
print(*fol)
print(aamm)
