# def twodigit(num):
#     if 10 <= num <= 99:
#         return "The number is a two-digit number."
#     else:
#         return "The number is not a two-digit number."
      
# number = int(input("Enter a number: "))
# result = twodigit(number)
# print(result)


def twodigitbylength(num: int) -> str:
  if len(str(abs(num))) == 2:
    return "Two digit number"
  else:
    return "Not a two digit number"
  
twodigitnum = int(input("Enter a number: "))
result = twodigitbylength(twodigitnum)
print(result)