values = ['あ', 'い', 'う', 'え', 'お']
print(values)

values.insert(0, '亜')
print(values)

values[5] = '尾'
print(values)

del values[0]
print(values[len(values)-1])
