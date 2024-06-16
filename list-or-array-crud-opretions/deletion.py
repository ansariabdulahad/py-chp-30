def deletion() :
    data = [1,  2, 3, 4, 5, 6, 7, 8, 9, 10]
    data.pop(0)
    print(data)
deletion()

def customDeletion() :
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    newList = []
    index = int(input("Enter index\n"))

    for i in range(len(data)) :
        if i != index :
            newList.append(data[i])
            
    print("old List:", data)
    print("new List:", newList)
customDeletion()