print("Hello")
val = array('i', [1, 2, 3, 4, 5])
new = array(val.typecode, (a*2 for a in val))
print(new)
