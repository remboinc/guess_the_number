string = input().lower().replace(',',' ').replace('.',' ').split()
my_dict = {}
for word in string:
    if word in my_dict:
        continue
    amount = string.count(word)
    my_dict.update({word: amount}) 
    print(word, ':', amount)

