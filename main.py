#!/Users/sunny/Desktop/Terminal_game/myenv/bin/python

from banner import banner
from passwordChecker import check_pwned_password
from passwordAuditor import audit_passwords as auditor
from phishing_detector import detect_phishing




def main_menu():
    banner()

    while True:
        

        choice = input("Select an operation (1-4): ")

        if choice == "1":
            password = input("\nEnter a password to check: ")
            check_pwned_password(password)
        elif choice == "2":
            auditor()
        elif choice == "3":
            detect_phishing()
        elif choice == "4":
            print("\n👋 Exiting.......Stay safe and secure.")
            break
        else:
            print("\nInvalid choice. Try again.")

        


if __name__ == "__main__":
    main_menu()