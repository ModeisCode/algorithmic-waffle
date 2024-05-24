
def boyerMooreHorspool(search:str, text:str):
    values = {}
    index = 0
    l = len(search)

    for c in search:
        values[c] = l - index - 1
        index += 1

    values[search[-1]] = l  

    for k,v in values.items():
        print("key:" + k + " value:" + str(v))

    LAST = l - 1
    textIndex = 0
    searchPos = l - 1
    searchIndex = l - 1
    while True:
        if searchPos <= (len(text) - 1):
            if search[searchIndex] == text[searchPos - textIndex] and searchIndex == 0:
                print(text[searchPos - l + 1 : searchPos + 1])
                return (searchPos - l)
            elif search[searchIndex] == text[searchPos - textIndex]:
                textIndex += 1
                searchIndex -= 1
            else:
                searchPos += values.get(text[searchPos], l)
                textIndex = 0
                searchIndex = LAST
        else:
            return -1

search = "hello"
text = "abcabctruesdhellofhddfsgbl" # 6,10
i = boyerMooreHorspool(search=search,text=text)
print(i)
