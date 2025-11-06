math_exp = (12 - 2) * 10 + 1/4
print(math_exp)

s = 'hello'
print(f'print char e: {s[1]}')
print(f'reverse using slicing: {s[::-1]}')

print(f'print char o using neg index: {s[-1]}')
print(f'print char o using pos index: {s[len(s) - 1]}')

my_list = [0,0,0]
print(my_list)


list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(f'list3: {list3}')


list4 = [5,3,4,6,1]
list4.sort()
print(f'sorted list4: {list4}')

d = {'simple_key':'hello'}
print(f'grab hello: {d['simple_key']}')

d = {'k1':{'k2':'hello'}}
print(f'grab hello: {d['k1']['k2']}')

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(f'grab hello: {d['k1'][0]['nest_key'][1][0]}')

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(f'grab hello: {d['k1'][2]['k2'][1]['tough'][2][0]}')

list5 = [1,2,2,33,4,4,11,22,3,3,2]
uniq_nums = set(list5)
print(f'Unique numbers: {uniq_nums}')