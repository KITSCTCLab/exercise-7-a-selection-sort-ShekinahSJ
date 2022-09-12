from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(size-1):
    for j in range(i,size-1):
      if array[j]<array[j+1]:
        min=array[j]
        minpos=j
      else:
        min=array[j+1]
        minpos=(j+1)
    temp=array[i]
    array[i]=min
    array[minpos]=temp
    
      

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
