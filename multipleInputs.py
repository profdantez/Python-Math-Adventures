# Program for entering multiple inputs in a console until q is pressed
names = []
while True:
	name = input('Enter a bunch of names: ')
	if name == 'q':
		break
	else:
		names.append(name)
print(names) 
