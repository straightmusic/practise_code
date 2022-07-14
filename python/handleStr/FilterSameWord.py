def filterSameWord(str):
    newstr=""
    for c in str:
        try:
            newstr.index(c)
        except:
            newstr+=c
    return newstr


if __name__ == '__main__':
    f = open("handleStr\\input.txt", "r", encoding="utf-8")
    str = f.read()
    f.close()

    newstr = filterSameWord(str)

    f = open("handleStr\\output.txt", "w", encoding="utf-8")
    str = f.write(newstr)
    f.close()
