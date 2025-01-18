def get_number(index):
    x = (index + 2) // 3
    y = (index + 1) // 3
    z = index // 3
    values = (4 * x) + (4 * y) - (1 * z)
    print(values)

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70