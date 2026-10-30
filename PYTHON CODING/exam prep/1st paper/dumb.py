# set = ()
# py = {1,2,3,4,5,5,4,3,2,2}
# pro = {"sum", 90 }
# do = []
# print(type(set))
# print(type(py))
# print(type(pro))
# print(type(do))
# print(py)

# s = {1,2,3,4,5,6}
# d = {3,4,5,6,7,8}
# print(s ^ d)
# stu = {}
# for i in range(3):
#     name = input()
#     age = int(input())
#     stu[name] = age

    
# print(stu)
def pal(word):
    return word == word[::-1]
word = input()
print(pal(word))