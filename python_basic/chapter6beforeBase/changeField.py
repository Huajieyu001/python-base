


temp = 100

def tryChange():
    global temp
    temp = 500
    print(temp)

tryChange()
print(temp)

temp2 = 100
def tryChange2(var):
    var = 500
    print(var)

tryChange2(temp2)
print(temp2)

# recursive
def recursive(var):
    '''返回var的累加值'''
    if(var == 1):
        return 1
    else:
        return recursive(var-1) + var


print(recursive(100))