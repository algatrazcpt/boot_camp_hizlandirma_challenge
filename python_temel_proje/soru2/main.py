def listele(lis):
    lis.reverse()
    for item in lis:
        if type(item)==list:
            listele(item)
    return lis
deger=[[1,2,3],[4,5]]


print(listele(deger))