vocaloid = ("Hatsune", "Miku")
print(vocaloid)
print(vocaloid[1])

value1 = (1, 2, 3)
value2 = (1, 2, 4)
print(value1 < value2)

# タプルオブジェクトは値を変更できない
# vocaloid[1] = "Rin" # => Error
vocaloid = ("Kagamine", "Rin")
print(vocaloid)
