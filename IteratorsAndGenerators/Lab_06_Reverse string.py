def reverse_text (my_str):
    for c in reversed(my_str):
        yield c


for char in reverse_text("step"):
    print(char, end='')
