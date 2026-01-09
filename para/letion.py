arr=[0,1,2,3,4,5,6,7,8,9]
min=arr[0]
max=arr[0]
i = 0
# for i in range(len(arr)):
while i < len(arr):
    if min> arr[i]:
        min==arr[i]
    if max < arr[i]:
        max=arr[i]
    i+=1 
print(f'max={max},min={min}')

