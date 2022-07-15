name = input("Input a name: ") + " "

surname = input("Input a surname: ")

full_name = name + surname

print(full_name)

forbidden_list = ["a", "e", "i", "o", "u", "w"]

replaced_name = full_name.replace("a", "z")
replaced_name = replaced_name.replace("e", "z")
replaced_name = replaced_name.replace("i", "z")
replaced_name = replaced_name.replace("o", "z")
replaced_name = replaced_name.replace("u", "z")
replaced_name = replaced_name.replace("w", "z")

print(replaced_name)

reversed_full_name = full_name[::-1]

print(reversed_full_name)
