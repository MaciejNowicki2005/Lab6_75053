#Opcja importu A
import f_mat
print(
"Kwadrat:",f_mat.kwadrat(10),
"Sześcian:",f_mat.szescian(3),
"Dodaj:",f_mat.dodaj(10,5))

#Opcja importu B
from f_mat import kwadrat, szescian, dodaj

print(
"Kwadrat:",kwadrat(10),
"Sześcian:",szescian(3),
"Dodaj:",dodaj(10,5))


