import os

user_choice = -1


def main_menu():
    print("1. Wybierz model")
    print("2. Pokaż wszystkie artykuły")
    print("3. Dodaj filtr")
    print("4. Usuń filtr")
    print("0. Wyjdź")

def first_choice():
    end = -1
    if end != 1:
        path = 'C:/Users/Bartek/Desktop/programowanie/Python/Katalog/Modele/'
        print("Wpisz nazwę modelu: ")
        for models in os.listdir(path):
            print(models)
        print()
        model = input('Podaj nazwę modelu: ')
        filters_list = open(path + model)
        for filters in filters_list:
            print(str(filters).strip('\n'))
        filters_list.close()
        print('__________________')
        print("1. Ok!")
        end = input('Wybierz numer: ')
      
    print()
    
def second_choice():
    end = -1
    if end != 1:
        path = 'C:/Users/Bartek/Desktop/programowanie/Python/Katalog/Modele/'
        all_products = []
        for models in os.listdir(path):
            filters_list = open(path + str(models)).readlines()
            all_products.extend(filters_list)

        all_products = sorted(set(all_products))

        for filters in all_products:
            print(str(filters).strip('\n'))

        print('__________________')
        print("1. Ok!")
        end = input('Wybierz numer: ')
        print()

def third_choice():
    end = -1
    if end != 1:
        products = []
        path = 'C:/Users/Bartek/Desktop/programowanie/Python/Katalog/Modele/'
        for model in os.listdir(path):
            print(model)
        print("Jeżeli chcesz dodać nowy model, wpisz jego nazwę.")
        print("0. Wróć do głównego menu.")
        print()
        model = input("Do jakiego modelu dodać filtr?: ")
        if model == '0':
            return
        else:
            file = open(str(path + model), 'a+')
            new_filter = str(input('Podaj nazwę filtra: ') + ': ' + str(input('podaj numer filtra: ') + '\n'))
            file.write(new_filter)
            file.close()

            filters_list = open((path + model)).readlines()
            products.extend(filters_list)
            products = sorted(set(products))
            file = open(str(path + model), 'w') 
            for filter in list(products):
                file.write(filter)
            file.close()

            print('__________________')
            print(str(new_filter).strip('\n') + " został dodany do " + model + "!")
            print()

            print('__________________')
            print("1. Ok!")
            end = input('Wybierz numer: ')
            print()

def fourth_choice():
    
    path = 'C:/Users/Bartek/Desktop/programowanie/Python/Katalog/Modele/'
    for model in os.listdir(path):
        print(model)
    print("0. Wróć do głównego menu.")
    print()
    model = input("Wybierz model, z którego chcesz usunąć filtr: ")
    if model == '0':
        return False
    
    n = -1
    x = 0
    for lista in os.listdir(path):
        if model == str(lista):
            while n == -1:
                file = open((path + model))
                products = file.readlines()
                print()
                print("To są wszyskie filtry przypisane do " + model + ": ")
                for filter in products:
                    x += 1
                    print(str(x) + '. ' + filter.strip('\n'))
                n = int(input("Wybierz numer pozycji: "))
                y = len(products)
                if n == 0:
                    print()
                    print("Nie ma takiego filtra. ")
                    print('__________________')
                    print("1. Ok!")
                    end = input('Wybierz numer: ')
                    print()
                    return False
                
                if int(n) <= y:
                    print()
                    print('__________________')
                    print(str(products[n-1]).strip('\n') + " został usunięty z " + model + "!")
                    print()
                    products.pop(n- 1)
                    file.close()
                    file = open(str(path + model), 'w')
                    for filter in products:
                        file.write(filter)
                    file.close()
                
                    print('__________________')
                    print("1. Ok!")
                    end = input('Wybierz numer: ')
                    print()
                    return False
                
                if int(n) > y:
                    print()
                    print("Nie ma takiego filtra. ")
                    print('__________________')
                    print("1. Ok!")
                    end = input('Wybierz numer: ')
                    print()
                    return False
                file.close()
    print()
    print("Nie ma takiego modelu. ")    
    print('__________________')
    print("1. Ok!")
    end = input('Wybierz numer: ')
    print()            
                

    

while user_choice != 0 :
    if user_choice == 1:
        first_choice()
        os.system("cls")
    
    if user_choice == 2:
        second_choice()
        os.system("cls")
    
    if user_choice == 3:
        third_choice()
        os.system("cls")
    
    if user_choice == 4:
        fourth_choice()
        os.system("cls")
        
    
    main_menu()
    user_choice = int(input("\nWybierz numer:"))
    print()