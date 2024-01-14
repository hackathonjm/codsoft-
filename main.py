import secrets
import string 


def generate_password(length=12, include_uppercase=True, include_digits=True, include_symbols=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password



def main():
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, include_uppercase, include_digits, include_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()
