def csRemoveDuplicateWords(input_str):
    old_list = input_str.split(' ')
    new_list = []
    index = 0
    for word in old_list:
        if (not word == for word in new_list):
            new_list.append(word)
            index += 1

    return new_list
# add 1st index to new list
# compare next index to words in new list
# if it does not match add to new list
# return new list

words = "alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta"
print(csRemoveDuplicateWords(words))