def prepend():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data.insert(1, "ahad")
    print(data)
prepend()

def customPrepend():
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    item = input("Enter your data\n")
    data = [item] + data

    print(data)
customPrepend()