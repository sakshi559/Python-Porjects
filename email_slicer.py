
email = input(f"Enter your email:\n")
if '@' and '.com' not in email:
    print("Enter correct email")
    quit()

else:
    username = email.split(chr(64))
    print("Username: ", username[0])
    print("domain: ", username[1])

