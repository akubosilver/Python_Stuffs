d = {'simple key':'hello'}
print(d['simple key'])

d1 = {'k1':{'k2':'hello'}}
print(d1['k1']['k2'])

d2 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}
print(d2['k1'][0]['nest_key'][1][0])

d3 = {'k': [1,2,{'k2':['this is tricky', {'tough':[1,2,['hello']]}]}]}
print(d3['k'][2]['k2'][1]['tough'][2][0])

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1': 4}]

answer = l_one[2][0] >= l_two[2]['k1']
print(answer)

#square of number = number ** 2
#square root of number  = number ** 0.5
#normal dictionaries are mapping not sequence

my_list = [0]
print(my_list * 3)