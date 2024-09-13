try:result=10/0
except ZeroDivisionError:print("you cant div")
else:print("div successful")
finally:print("this block runs no matter wht.")