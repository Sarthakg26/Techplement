import argparse
import string
import secrets

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type must be specified.")
        return None

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument("length", type=int, help="Password length")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-l", "--lowercase", action="store_true", help="Include lowercase letters")
    parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
    parser.add_argument("-s", "--special-chars", action="store_true", help="Include special characters")
    args = parser.parse_args()

    password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special_chars)
    if password:
        print("Generated password:", password)

if __name__ == "__main__":
    main()