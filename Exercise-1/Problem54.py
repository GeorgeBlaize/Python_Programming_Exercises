
# Python Program to Sort a Dictionary by Value

dt={5:4, 1:6, 6:3}

sorted_dt={key: value for key,value in sorted(dt.items(),key=lambda item:[1])}

print(sorted_dt)
