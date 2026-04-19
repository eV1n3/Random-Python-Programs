i = 1
x = 1
var = 0

while(True):
    if (i % 2 == 0):
        var -= (4/x)
        print(var)
    else:
        var += (4/x)
        print(var)
    
    i += 1
    x += 2