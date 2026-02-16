# names = input("Enter Your Name: ")

# def main():
#     print(Capital(names))

# def Capital(names):
#     return f"Capital Version: {names.capitalize()}"

# if __name__ == "__main__":
#     main()



# html_data = "<h1>This is a heading</h1><p>This is a paragraph.</p>"
# start_index = html_data.find("<h1>") + len("<h1>")
# end_index = html_data.find("</h1>")
# heading_text = html_data[start_index:end_index]


# names = []

# with open("names.csv") as file:
#     for line in file:
#       name, age = line.rstrip().split(",")
#       student = {'name': name, 'age': age}
#       names.append(student)
      
# def get_names(student):
#     return (student['name'])
  
# for student in sorted(names, key=get_names):
#     print(f"{student['name'].capitalize()} is {student['age']} years old.")

# count the occurrence of a word in the sentence

def main():
    sentence = "Welcome to the world of titan. Tighten your seatbelts to enjoy this world further."
    return (to_count(sentence))

def to_count(sentence: str) -> str:
    return sentence.count('to')

if __name__ == "main":
    print(main())
