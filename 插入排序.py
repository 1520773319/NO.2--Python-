array=[]
def puts():
    num=input()
    if num.isdigit():
        array.append(int(num))
        puts()

def InsertionSort(arr):
  puts()
  length=len(arr)
  for i in range(1,length):
    j=i
    temp=arr[i]
    while j>0 and temp<arr[j-1]:
      arr[j]=arr[j-1]
      j-=1
    arr[j]=temp
  print(arr)

InsertionSort(array)