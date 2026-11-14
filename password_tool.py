import random
import string
import re
import sys

def check_password_strength():
    print("\n--- PASSWORD STRENGTH CHECKER ---")
    password = input("Enter a password to check: ")
    
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if len(password) >= 12:
        score += 1

    # Uppercase & Lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Numbers check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one number (0-9).")

    # Special characters check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Final Evaluation
    print(f"\n🔒 Strength Score: {score}/5")
    
    if score == 5:
        print("🟢 Status: EXTREMELY STRONG PASSWORD! 🚀\n")
    elif score >= 3:
        print("🟡 Status: MODERATE PASSWORD (Could be stronger).\n")
    else:
        print("🔴 Status: WEAK PASSWORD! Please improve it.\n")

    if feedback:
        print("💡 Recommendations:")
        for item in feedback:
            print(f"   {item}")
        print()

def generate_strong_password():
    print("\n--- STRONG PASSWORD GENERATOR ---")
    try:
        length = int(input("Enter desired password length (min 8): "))
        if length < 8:
            print("⚠️ Length should be at least 8 for good security. Setting default to 12.")
            length = 12
    except ValueError:
        print("❌ Invalid input! Defaulting length to 12.")
        length = 12

    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()"

    # Ensure at least one of each category
    char_list = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the length
    all_chars = lower + upper + digits + symbols
    for _ in range(length - 4):
        char_list.append(random.choice(all_chars))

    # Shuffle for randomness
    random.shuffle(char_list)
    secure_password = "".join(char_list)

    print(f"\n✨ Generated Secure Password: {secure_password}\n")

def main():
    while True:
        print("========================================")
        print(" 🔑 PASSWORD STRENGTH & GENERATOR TOOL  ")
        print("========================================")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == '1':
            check_password_strength()
        elif choice == '2':
            generate_strong_password()
        elif choice == '3':
            print("\nExiting... Stay secure! 👋\n")
            sys.exit()
        else:
            print("❌ Invalid choice! Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()