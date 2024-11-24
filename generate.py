import secrets
import string

# Generate a random secure secret key with mixed Uppercase, lowercase, and numbers
characters = string.ascii_letters + string.digits  
random_key = ''.join(secrets.choice(characters) for _ in range(20))  

# Format the key
formatted_key = f"{random_key[:6]}-{random_key[6:9]}-{random_key[9:13]}-{random_key[13:21]}"
print(f"Your formatted secret key: {formatted_key}")
