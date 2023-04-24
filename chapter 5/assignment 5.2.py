smallest = largest = 0
n = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numb = int(num)
    except:
        print('Invalid input')
        continue
    n.append(numb)
    if numb == n[0]:
        smallest = largest = numb
    elif largest < numb:
        largest = numb
    elif smallest > numb:
        smallest = numb

print("Maximum is", largest)
print("Minimum is", smallest)