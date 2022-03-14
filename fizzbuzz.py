def fibuzz(n):
    for i in range(n):
        if i % 3 == 0:
            print(f'{i}: fizz')
        if i % 5 == 0:
            print(f'{i}: buzz')

fibuzz(100)