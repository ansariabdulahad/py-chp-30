def search() :
    data = ['ahad', 'noor', 'samad', 'wahid']
    print(data.index('samad'))
search()

def customSearch() :
    data = [2, 'ahad', 'noor', 'samad', 'wahid']
    newList = []
    searchIndex = None
    try : item = input("Enter search item\n")
    except : print("Only string values are allowed")
    else :
        for i in range(len(data)) :
            if data[i] == item :
                newList.append(item)
                searchIndex = i
                break
        print("Old list: ", data)
        print(f"search item is {newList} from {data} and index is {searchIndex}")
customSearch()