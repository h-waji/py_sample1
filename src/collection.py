dict_obj = {"dog": "犬", "cat": "猫", "hamster": "ハムスター"}
print("辞書の要素数:", len(dict_obj))

tuple_obj = (1, 2, 3)
print("タプルの要素数:", len(tuple_obj))

list_obj = [1, 2, 3, 4]
print("リストの要素数:", len(list_obj))

str_obj = "12345"
print("文字列の長さ:", len(str_obj))

# ----- in 演算子 -----
list_obj = ["Miku", "Rin", "Len"]
print("Miku" in list_obj) # => True

print(2 in tuple_obj) # => True

key = "hamster"
if (key in dict_obj):
    print(key, "は", dict_obj[key], "です")

str_obj = "Hajimemashite Sekai"
print("j" in str_obj) # => True
# 文字列の場合、一連の文字を指定して検索できる
print("Sekai" in str_obj) # => True

# ----- for -----
for item in list_obj:
    print(item.upper())

for char in str_obj:
    print(char.upper())

for english in dict_obj:
    print(english, "は", dict_obj[english], "です")
