# rows = 4
# for i in range(rows):
#     print("  "*(rows-i-1)+"* "*(2*i+4))
# for i in range(rows-2, -1, -1):
#     print("  "*(rows-i-1)+"* "*(2*i+4))


row = 5
for i in range(row):
    if i== 0 or i == row-1:
        print(("*")*row)
    else :
           print("*"+" "*(row-2)+"*")

# private
# rows = 4
# for i in range(rows):
#      if i >= 0 or i <= rows+2:
#          print("*"*i)