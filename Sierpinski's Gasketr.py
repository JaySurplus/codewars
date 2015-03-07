def sierpinski(n):
    result = []
    for i in range(0,n+1):
        if i == 0:
            result.append('"')
        else:
            for j in range(2**(i-1),2**i):
            	result.append(addSpace(j,i,result))	
    r = result[0]
    for line in result[1:]:
        r= r+'\n'+line
    return r

def addSpace(l,n,string_list):
    result = string_list[l-2**(n-1)]
    space = len(range(0,2*2**(n-1)-l)) * 2 - 1 
    for i in range(0,space):
        result = ' ' +result
    return string_list[l-2**(n-1)]+result



#print sierpinski(1)
print sierpinski(6)