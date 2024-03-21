arr = []
temp = head

while temp is not None:
    arr.append(temp.val)
    temp = temp.next

temp = head
for i in range(len(arr)-1, -1, -1):
    temp.val = arr[i]
    temp = temp.next

return head
