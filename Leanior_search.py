pos=-1
def Search(list,n):
    i=0
    while i <len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False

list=[5,8,3,4,9,2,3]
n=3
if Search(list,n):
    print ("Found",pos+1)
else:
    print("Not found")