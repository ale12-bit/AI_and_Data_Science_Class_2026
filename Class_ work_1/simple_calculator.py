aa=input('enter a number;')
print(type(aa))
aa=int(aa)
print(type(aa))
bb=int(input('enter a number;'))
print(type(bb))
print('PLEASED TO HAVE YOU PERTICIPATE WITH US TODAY')
print(f'your numbers are {aa} , {bb}')
print('what would you like to calculate')
print('1 for addition')
print('2 for subtraction')
print('3 for multiplication')
print('4 for division')
calc=int(input('addition;'))
if calc== 1:
    print(aa+bb)
elif calc== 2:
    print(aa-bb)
elif calc== 3:
    print(aa*bb)
elif calc== 4:
    print(aa/bb)
else: print('error')
