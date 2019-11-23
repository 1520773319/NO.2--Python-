array=[]
def puts():
    num=input()
    if num.isdigit():
        array.append(int(num))
        puts()

def MergeSort(left,right):
    result=[]
    il=ir=0
    while len(left)>il and len(right)>ir:
        if left[il]<right[ir]:
            result.append(int(left[il]))
            il+=1
        else:
            result.append(int(right[ir]))
            ir+=1
    while len(left)>il:
        result.append(int(left[il]))
        il+=1
    while len(right)>ir:
        result.append(int(right[ir]))
        ir+=1
    return result

def Slice(arr):
    length=len(arr)
    mid=round(length/2)
    if length==1:
        return arr
    if length==2:
        left=[arr[0]]
        right=[arr[1]]
    if length>2:
        left=arr[:mid]
        right=arr[mid:]
    return MergeSort(Slice(left),Slice(right)) 

puts()
print(Slice(array))

