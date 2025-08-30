def check_hex(string1):
    string1_lower = string1.lower()
    for i in string1_lower:
        if i in ["a", "b", "c", "d", "e", "f", "#"] and [f"{0:10}"]:
            continue
        else:
            print("No")
            quit()
    if not string1[0] == "#" :
        print(No")
    elif not len(string1) == 7:
        print("No")
    else:
        print("Yes")

string_user = input("vard kon = ")
check_hex(string_user)
