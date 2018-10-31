import collections as col

text_list = ['ABC','PQR','ABC','ABC','PQR','Mno','xyz','PQR','ABC','xyz']
my_counter = col.Counter()
for element in text_list:
    my_counter[element] += 1
    
print(my_counter)
print(my_counter.most_common(2))
