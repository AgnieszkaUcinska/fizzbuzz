def fizzbuzz():
    for i in range (1,101):
        if not i % 3 and not i % 5:
            print ('Fizzbuzz')
        if not i % 3:
            print ('Fizz')
        elif not i % 5:
            print ('Buzz')

        else:
            print (i)


if __name__=='__main__':
    fizbuzz()