# rows = 4
# col = 4
# for i in range(rows):
#     print(" "*(rows-i-1)+"*"*(2*i+4))
#     for j in range(col):
#         print(" "*(col+j)+"*"*(2*j-4))
        

# rows = 4
# for i in range(rows):
#     print(" "*(rows-i-1)+"*"*(2*i+4))
#     # for j in range(rows):
#     #     print(" "*(rows+j+1)+"*"*(2*j+4))
#     # for j in range(rows):
#     #     print(" "*(rows+j)+"*"*(2*j-2))
    # for j in range(8 , rows-1+2):
    #     print(" "*(rows-j-1)+"*"*(2*j+4))


rows = 5
for i in range(rows):
    print(" "*(rows-i-1)+"*"*(2*i+1))
for i in range(rows-2, -1, -1):
    print(" "*(rows-i-1)+"*"*(2*i+1))



        
