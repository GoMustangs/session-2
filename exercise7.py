text = input('please enter two teams and two scores: ')

def addnumbers(text):
    totalCount = 0
    for i in text:
        if i .isdigit()== True:
            count = int(i)
            totalCount = totalCount + count
    return totalCount
    
print(addnumbers(text))