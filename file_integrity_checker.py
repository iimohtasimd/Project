import hashlib    # It is used to create hash value
import os         # It check file and folder exist 

HASH_FILE = "hashes.txt"


# Generate SHA-256 hash
def generate_hash(filename):
    hasher = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()


# Save file hash
def save_hash(filename):
    file_hash = generate_hash(filename)

    with open(HASH_FILE, "a") as f:
        f.write(filename + ":" + file_hash + "\n")

    print("✅ File registered successfully!")


# Check file integrity
def check_integrity(filename):
    if not os.path.exists(HASH_FILE):
        print("❌ No database found!")
        return

    with open(HASH_FILE, "r") as f:
        lines = f.readlines()

    for line in lines:
        saved_file, saved_hash = line.strip().split(":")

        if saved_file == filename:
            current_hash = generate_hash(filename)

            if current_hash == saved_hash:
                print("🟢 File is SAFE. No changes detected.")
            else:
                print("🔴 File has been MODIFIED!")

            return

    print("❌ File not registered!")


# Main Menu
while True:
    print("\n===== FILE INTEGRITY CHECKER =====")
    print("1. Register File")
    print("2. Check File Integrity")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file = input("Enter file name: ")

        if os.path.exists(file):
            save_hash(file)
        else:
            print("❌ File not found!")

    elif choice == "2":
        file = input("Enter file name: ")

        if os.path.exists(file):
            check_integrity(file)
        else:
            print("❌ File not found!")

    elif choice == "3":
        print("Exiting... Goodbye 👋")
        break

    else:
        print("❌ Invalid choice!")
