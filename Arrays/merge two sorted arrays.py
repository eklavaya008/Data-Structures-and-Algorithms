#Solution

def findUnion( a, b):
    result = []
    n,m = len(a) , len(b)
    i,j = 0,0
    while i<n and j<m:
        if a[i] <= b[j]:
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i+=1
        else:
            if len(result) == 0 or result[-1] != b[j]:
                result.append(b[j])
            j+=1
                
    while i<n:
        if i<n:
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i+=1
    while j<m:
            if j<m:
                if len(result) == 0 or result[-1] != b[j]:
                    result.append(b[j])
                j+=1
    return result
                
a = [1,1,2,3,3,4,5,5]
b = [1,3,4,4,6,7,8,9]
print(findUnion(a,b))