def reverseString():
    l = input('Enter a string')
    l =[x for x in l]
    for i in range(int(len(l)/2)):
        l[i] , l[-1*(i+1)] = l[-1*(i+1)],l[i]
    #print (l)
    return ''.join(l)
#l="911"
#print(reverseString())
#a,b=b,a

# def test_reverseString1():
#     l=[]
#     assert l==reverseString(l)
# def test_reverseString2():
#     l=[1]
#     assert l==reverseString(l)
# def test_reverseString3():
#     l=[1,2]
#     assert [2,1]==reverseString(l)
# def test_reverseString4():
#     l=[1.5,2,'a']
#     assert ['a',2,1.5]==reverseString(l)