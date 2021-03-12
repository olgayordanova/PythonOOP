def vowels(my_string):
   for ch in my_string:
        if ch.lower () in "aeioyu":
            yield ch


my_string = vowels ( 'Abcedifuty0o' )
for char in my_string:
    print ( char )