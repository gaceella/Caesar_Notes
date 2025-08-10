# --- Caesar Cipher Encryption Function ---
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# --- Caesar Cipher Decryption Function ---
def decrypt(text, shift):
    return encrypt(text, -shift)

# --- Save the Encrypted Note to a File ---
def save_note(filename, encrypted_text):
    with open(filename, "w") as file:
        file.write(encrypted_text)

# --- Load the Encrypted Note from a File ---
def load_note(filename):
    with open(filename, "r") as file:
        return file.read()

# --- Main Program ---
def main():
    print("🛡️ Welcome to Secure Notes App")
    print("1. Write and Save Encrypted Note")
    print("2. Load and Decrypt Note")
    
    choice = input("Choose 1 or 2: ")

    shift = int(input("Enter Caesar Cipher shift number (e.g., 3): "))
    filename = input("Enter file name to save/load note (e.g., note.txt): ")

    if choice == "1":
        note = input("Write your secret note:\n")
        encrypted = encrypt(note, shift)
        save_note(filename, encrypted)
        print("✅ Your note has been encrypted and saved!")

    elif choice == "2":
        try:
            encrypted = load_note(filename)
            decrypted = decrypt(encrypted, shift)
            print("\n🔓 Your decrypted note is:")
            print(decrypted)
        except FileNotFoundError:
            print("❌ Sorry File not found. Please make sure the name is correct.")

    else:
        print("❌ Sorry Invalid choice. Please choose 1 or 2.")

# --- Start the app ---
main()

