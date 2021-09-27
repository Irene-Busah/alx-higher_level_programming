#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    my_index = 0
    try:
        for i in my_list:
            if x > my_index:
                print("{}".format(my_list[my_list]), end='')
                my_index += 1
        print()
    except TypeError:
        pass
    finally:
        return my_index
