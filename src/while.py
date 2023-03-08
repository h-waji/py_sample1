text = ""

while text != "採用":
    text = input("採用 と入力してください: ")
    print(text, "と入力されました")

print("お疲れ様でした")

# ----- break, continue -----
counter = 1
while counter <= 5:
    text = input("数字を入力してください")

    if text == '':
        print("入力が無効です")
        continue

    if text == '999':
        print("中断します")
        break

    number = int(text)
    print(counter, "回目:", number * number)
    counter += 1

print("終了しました")
