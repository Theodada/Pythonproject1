# Question: in my_list = ["fat", "cat", "pot", "kettle", "love", "smart"]
# print out all the items that ends with "t" and put them in a new list
# Answer: We will use list comprehension on the list to create new list
# and according to the conditions expected.

my_list = ["fat", "cat", "pot", "kettle", "love", "smart"]
new_list = [word for word in my_list if word.endswith("t")]
print(new_list)