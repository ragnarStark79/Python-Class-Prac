from werkzeug.security import generate_password_hash, check_password_hash


hash_pass = generate_password_hash("password123")
print(hash_pass)
hash_pass_0 = generate_password_hash("password12")
print(hash_pass_0)
check = check_password_hash(hash_pass,hash_pass_0)
print(check)