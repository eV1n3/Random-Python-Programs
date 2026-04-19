# Imports
import hashlib

# Methods
def main():
    encoded_string = input("Encoded SHA1 string: ")
    clean_encoded_string = encoded_string.strip().lower()

    with open("rockyou.txt") as password_list:
        for password in password_list:
            encoded_password = sha1_encoder(password.strip())
            
            if clean_encoded_string == encoded_password:
                print(f"Password has been found: {password}")
                return
        
        print("Password not found")

def sha1_encoder(text):
    sha1_cipher_text = hashlib.sha1(text.encode()).hexdigest()

    return sha1_cipher_text
    

# Main Statement
if __name__ == "__main__":
    main()