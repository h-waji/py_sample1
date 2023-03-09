list_obj = ["Miku", "Rin", "Len"]
vocalo1, vocalo2, volalo3 = list_obj
print(vocalo1, vocalo2, volalo3)

tuple_obj = ("miku", "rin", "len")
vocalo1, vocalo2, volalo3 = tuple_obj
print(vocalo1, vocalo2, volalo3)

str_obj = "ham"
char1, char2, char3 = str_obj
print(char1, char2, char3)

# ----- function and unpack -----
def total_and_average(values):
    total = 0
    for value in values:
        total = total + value

    num = len(values)
    average = total / num

    return (total, average) # タプルを返す

values = [100, 200, 20, 50, 90]
total, average = total_and_average(values)
print(values, "の合計は", total, "平均は", average, "です")
