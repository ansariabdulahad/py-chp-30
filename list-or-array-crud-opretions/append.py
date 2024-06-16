def append() :
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data.append("Ahad Ansari")
    print(data)
append()

def customAppend() :
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    item = input("Enter your data\n")
    data = data + [item]

    print(data)
customAppend()