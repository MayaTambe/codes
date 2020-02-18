
'''def FisrtLast():
    color_list=["Red","Green","White","Black"]
    First=color_list[0]
    print("The first color is:",First)
    Last=color_list[-1]
    print("The Last color is:",Last)
    return
FisrtLast()'''
def FisrtLast():
    list=[]
    elements=int(input("Enter the number elements:"))

    for i in range(0,elements):
        value=(input("Enter the elements:"))
        list.append(value)
    print("The List is:",list)

    First=list[0]
    print("The first color is:",First)
    Last=list[-1]
    print("The Last color is:",Last)
    return
FisrtLast()


