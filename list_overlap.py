'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
'''

    my_list = ['red, orange, yellow, green, blue, purple, cyan, indigo']

    some_other_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan', 'indigo']

    #1st example
    for item in my_list:
        if "e" in item:
            print(item)

    print('\n\n\n\n\n')

    #2nd example
    for item in some_other_list:
        if "e" in item:
            print(item)


    #Example output
    '''
    red, orange, yellow, green, blue, purple, cyan, indigo






    red
    orange
    yellow
    green
    blue
    purple
    '''
