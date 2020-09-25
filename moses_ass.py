print('CHOOSE ACCESS...')
print('1. Admin')
print('2. User')
print('3. Exit')
menu1 = int(input('Choose access: '))
##print(menu1)
##print(' ')
##print(' ')

if menu1 == 2:
    print('       USER MENU')
    print('1. Display')
    print('2. Buy Items')
    print('3. Return')
    menu2 = int(input('Choose User Menu: '))
    if menu2 == 1:
        print('========================================================')
        print('            MAL ADAMU IFE RETAIL MARKET')
        print('========================================================')
        import csv
        print(('Item                            Av. Quantity              Unit Price').upper())
        print()
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], ' '*(28-len(row[0])), str(row[1]), ' '*(30-len(str(row[1]))), row[2])

    
    elif menu2 == 2:
        print('Supply Item ID(s) and Quantity(ies) to continue...')
        go_on = 'y'
        while go_on == 'y':
            itemID = int(input('Enter Item ID: '))
            itemQty = int(input('Enter Quantity: '))
            go_on = str(input('Do you still need another item?[y/n]: ')).lower()
        
    
elif menu1 == 1:
    print('1. Display Items')
    print('2. Set Item Price')
    print('3. Update Quantities')
    print('4. Add New Item')
    print('5. View Sales Record')
    print('6. Return')
    menu_user = int(input('Choose User Menu: '))
    if menu_user == 1:
        print('Thank you for patronage')
        print('========================================================')
        print('            MAL ADAMU IFE RETAIL MARKET')
        print('========================================================')
        import csv
        print(('Item                            Av. Quantity              Unit Price').upper())
        print()
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], ' '*(28-len(row[0])), str(row[1]), ' '*(30-len(str(row[1]))), row[2])
        


    
    

