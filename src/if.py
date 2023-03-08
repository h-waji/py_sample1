score = 80

if score >= 80:
    print("インデントは半角スペース 4 文字！")
else:
    print("残念")

input_data = input("何か入力してください")

if input_data.isdecimal():
    print(input_data," は数字です")
elif input_data.isalpha():
    print(input_data, " はアルファベットです")
else:
    print(input_data, "は数字とアルファベットではありません")
