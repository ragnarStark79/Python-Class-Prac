def largestNum(num1, num2, num3: int) -> int:
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest
  
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = largestNum(num1, num2, num3)
print("The largest number is:", largest)

# check vowels or consonants
def checkVowelConsonant(char: str) -> str:
  vowels = "aeiouAEIOU"
  if char in vowels:
    return "Vowel"
  else:
    return "Consonant"
  
char = input("Enter a character: ")
result = checkVowelConsonant(char)
print(f"The character '{char}' is a {result}.")