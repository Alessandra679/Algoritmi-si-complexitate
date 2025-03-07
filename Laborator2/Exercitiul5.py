from Exercitiul4 import creare_lista

def determinare_min_max(lista, result):
     min = lista[0]
     max = lista[0]
     for element in lista:
         if element < min:
             min = element
         if element > max:
             max = element
     match result:
         case "min":
            return min
         case "max":
            return max
         case _:
            return min, max
if __name__ == "__main__":
    n = int(input("Introduceti numarul de elemente: "))
    lista = creare_lista(n)
    print(determinare_min_max(lista,"max"))