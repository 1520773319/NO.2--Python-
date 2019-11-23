array=[]
def puts():
    num=input()
    while num.isdigit():
        array.append(int(num))
        puts()
        break

def SelectSort(arr):
    puts()
    length=len(arr)
    for i in range(0,length-2):
        indexMin=i
        for j in range(i+1,length):
            if(arr[indexMin]>arr[j]):
                indexMin=j
        if indexMin!=i:
            temp=arr[indexMin]
            arr[indexMin]=arr[i]
            arr[i]=temp 
    print(arr)

SelectSort(array)