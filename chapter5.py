# dir: C:\Users\koh99\PycharmProjects\Algorithms
import collections

a=collections.defaultdict(int)
a['A']=5
a['B']=4
print(a)
print(a['C'])
a['C']+=1
print(a)


b=collections.defaultdict(str)
b['A']='a'
b['B']=1
print(b)


a=[1,2,3,4,5,5,5,6,6]
b=collections.Counter(a)
print(b)
print(type(b))
print(b.most_common(2))


a=collections.OrderedDict({'banana':3,'apple':4,'pear':1,'orange':2})
print(a)
print(type(a))
