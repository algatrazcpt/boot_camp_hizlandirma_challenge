k_input=[[1,'a',['cat'],2],[[[3],[7]],[8],'dog'],4,5]
k=[]

def flatten(lis):
    for item in lis:
        if type(item)==list:
            flatten(item)
        else:
            k.append(item)
    return k
print(flatten(k_input))
