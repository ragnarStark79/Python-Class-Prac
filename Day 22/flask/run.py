from werkzeug.security import generate_password_hash, check_password_hash

hash_password = generate_password_hash("admin123")
print(hash_password)

print(check_password_hash(hash_password, "admin123"))
print(check_password_hash(hash_password, "admin124"))