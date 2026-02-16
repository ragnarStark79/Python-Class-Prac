# html_data = "<h1>Hello there</h1>"
# startwith = html_data.find(">") + 1
# endwith = html_data.find("</")
# print(html_data[startwith:endwith].strip())



# check password strength


def check_password(password: str) -> str:
    has_len = len(password) >= 8
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if has_len and has_lower and has_upper and has_digit and has_special:
        return "Strong Password"
    return "Weak Password"


password = "asdfkAA@sfddGJHJHJjsdf2#%13"
print(check_password(password))