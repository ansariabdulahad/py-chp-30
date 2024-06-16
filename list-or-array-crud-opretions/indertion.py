def insertion() :
    data = [1, 2, 3, 4, 5, 'just', 'ahad']
    data.insert(5, 'just for code')
    print(data)
# insertion()

def customInsertion() :
    data = [1, 2, 3, 4, 5, 'just',]
    newList = []
    index = int(input("Enter index\n"))
    item = input("Enter item\n")

    for i in range(len(data)) :
        if i == index :
            newList.append(item)
        else :
            newList.append(data[i])
    print("Old List:", data)
    print("New List:", newList)

customInsertion()