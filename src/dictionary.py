english_words = {"apple": "りんご", "orange": "みかん", "peach": "もも"}
print(english_words)
print(len(english_words))

empty_dict = {}
print(empty_dict)

print(english_words["peach"])

dict_obj = {}
dict_obj["dog"] = "犬"

print(dict_obj["dog"])

del dict_obj["dog"]
print(dict_obj)

# ----- in 演算子 -----
print("apple" in english_words)
print("dog" in english_words)

# ----- key in dict -----
key = input("英単語を入力してください")

if key in english_words:
    print(english_words[key])
else:
    print("登録されていません")
