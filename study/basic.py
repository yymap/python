# First python
print('hello,world')
print("Enter name:")
name = input()
print('nice to meet you ' + name)
print("the lenth of you name is: ")
print(len(name))
print('enter age:')
age = input()
print('you will be ' + str(int(age) + 1) + ' in a year')

print('Enter age:')
age = input()
if int(age) ==35 :
    print('right , you are 35')
else :
    print('you are not 35')

print('Enter age:')
age = int(input())
if 10 <= age < 40 :
    print("Age is in 10 to 40")
elif 40 <= age < 50 :
    print('Age is in 40 to 50')
else :
    print('Age is other')

for i in range(3) :
    print('for ' + str(i))

    
count = 5
print('Noe test your calculate.')
while count < 10 :
    print('hell')
    count = count + 1
    

while True :
    print('Who are you?')
    name = input()
    if name != 'eric' :
        continue
    print('Enter password:')
    pwd = input()
    if pwd == '111' :
        print('pwd right!')
        break
    else :
        print('pwd wrong')
print("Login success!")
