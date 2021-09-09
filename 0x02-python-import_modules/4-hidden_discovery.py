#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    not_so_hidden = dir(hidden_4)
    for s in not_so_hidden:
        if s[0] != '_' and s[1] != '_':
            print(s)
