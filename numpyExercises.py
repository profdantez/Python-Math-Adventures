grade = int(input('Enter grade: '))

if 0 <= grade <= 100:
	if grade >= 90:
		print('Highest Recommendation')
	elif grade >= 80 and grade < 90:
		print('Strong Recommendation')
	elif grade >= 70 and grade < 80:
		print('Recommended')
	else:
		print('Not Recommended')
else:
	print('Wrong Input')