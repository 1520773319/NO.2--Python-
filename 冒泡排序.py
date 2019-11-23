array=[]

def puts():
    num=input()
    if num.isdigit():
        array.append(int(num))
        puts()
        
def BubbleSort(arr):
    puts()
    length=len(arr)
    for i in range(0,length-1):
        for j in range(0,length-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)

BubbleSort(array)