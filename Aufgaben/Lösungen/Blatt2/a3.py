my_name = "Aaron"
friends_name = "Tom"

example = ["Max", "Lara", "Kathrin", "Aaron", "Tom", "Sebastian"]     # should return True
example_2 = ["Max", "Lara", "Kathrin", "Tom", "Aaron", "Sebastian"]   # should return True
example_3 = ["Max", "Lara", "Kathrin", "Tom", "Sebastian", "Aaron"]   # should return False

my_list = example

length = len(my_list)

for (index, name) in enumerate(my_list):
    # if we are at the beginning of the list, there is nothing to check
    if index == 0:
        continue
    # Check if you are at the current position and your friend at the previous position
    if name == my_name and my_list[index - 1] == friends_name:
        print("Ja, die beiden Namen kommen hintereinander")
        break
    # Check if your friend is at the current position and you are at the previous position
    if name == friends_name and my_list[index - 1] == my_name:
        print("Ja, die beiden Namen kommen hintereinander")
        break
else:
    print("Nein, die beiden Namen kommen nicht hintereinander")