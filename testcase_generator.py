import random

for i in range(100000):

    # generate a string value test which is input string by doing stuff
    test = ''

    # the weird multiline comment is just to make it easier to switch between
    # testing the logic and writing to files
    '''print(test)
    r'''
    f = open(r'C:\Users\ksdfg\Desktop\rsc\input\input' + str(i) + '.txt', 'w')
    f.write(test)
    #'''


    # generate a string value res which is output string by doing stuff
    res = ''

    # the weird multiline comment is just to make it easier to switch between
    # testing the logic and writing to files
    '''print(res)
    r'''
    f = open(r'C:\Users\ksdfg\Desktop\rsc\output\output' + str(i) + '.txt', 'w')
    f.write(res)
    #'''

'''
The format of the zip file is that it should have two folders - input (with all
the input test files) and output (with all the output test files). akhilnarang,
zip the two folders input and output (in C:\Users\ksdfg\Desktop\rsc for me)
into a single zip file that is to be uploaded.
Someone check out if there's a hackerrank api for uploading this zip file.
'''
