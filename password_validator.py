import sys, os.path
from os import path
# store the received insert password.
user_password = ""
# store the file path.
path_file = ""
# var to check the size of the file.
check_file = ""


# return text from file.
def get_pass(path_to_file):
    """ received path to file & return text password from the file """

    with open(path_to_file) as f:
        file_password = f.readline()
        return file_password

# receive password from terminal.
if len(sys.argv) == 2:
    user_password = sys.argv[1]
# receive file path from the terminal.
elif len(sys.argv) > 2:
    path_file = sys.argv[2]
    # return the size of the file.
    check_file = os.stat(path_file).st_size
    # update the password from the file if found.
    if check_file > 0:
        user_password = get_pass(path_file)


def Password_Validator(passW):
    # 3 validated arguments.
    digit_num = lower_letter = capital_letter = False
    # error text messages.
    msg1 = "Capital letter is missing. !\n"
    msg2 = "Lower letter is missing. !\n"
    msg3 = "Digit number is missing. ! \n"
    # merge all the errors messages if found.
    wrong_pass_msg = ""
    # evaluate the password if is length > 10.
    if len(passW) >= 10:
        for letter in passW:
            # evaluate if char is Capital letter.
            if ord(letter) in range(65, 91):
                capital_letter = True
                msg1 = ""
            # evaluate if char is a digit number.
            elif ord(letter) in range(48, 58):
                digit_num = True
                msg3 = ""
            # evaluate if char is Lower letter.
            elif ord(letter) in range(97, 123):
                lower_letter = True
                msg2 = ""
        # reformat error massages if Errors found, print & return 1.
        if not capital_letter or not lower_letter or not digit_num:
            wrong_pass_msg = "\033[31mErrors:\n" + msg1 + msg2 + msg3
            print(wrong_pass_msg)
            return 1
        # success messages printed if password is validated, & return 0.
        else:
            print("\033[32m Test Pass: password is validated !")
            return 0
    # Error message if password not received, print Error & return 1.
    elif passW == "":
        print("\033[31mError: password is required!")
        return 1
    # Error message if password is too short, print Error & return 1.
    elif 0 < len(passW) < 10:
        print("\033[31m Error: password is too short!")
        return 1
Password_Validator(user_password)
