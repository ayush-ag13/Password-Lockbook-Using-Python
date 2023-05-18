import random


def generate_password():
    '''Defining the function password generater which will return strong password which must
     contain all the characters(upper and lower case both), numbers and symbols'''

    uc = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    lc = 'qwertyuiopasdfghjklzxcvbnm'
    n = '1234567890'
    s = '!@#$%^&()'
    mix = uc+lc+n+s
    password = ''
    # For loop for generating random password upto the length 6
    for i in range(6):
        a = mix[random.randint(0, len(mix)-1)]
        password += a
    '''For all combination of characters, symbols and numbers in the password
    we separated picking the random elements from each sets(characters, symbols etc) and then add them'''
    a = uc[random.randint(0, len(uc)-1)]
    password += a
    a = lc[random.randint(0, len(lc)-1)]
    password += a
    a = n[random.randint(0, len(n)-1)]
    password += a
    a = s[random.randint(0, len(s)-1)]
    password += a
    l = list(password)
    # After adding them we shuffle them and we get strong password
    random.shuffle(l)
    password = ''.join(l)

    return password


def search(website_name):
    '''This will look up that the website you want to add or search already exist in the stored data
    or not.'''

    file = open("datasheet.txt", "r")
    read1 = file.read()

    flag = 0
    k = read1.split()
    l = []
    for i in range(len(k)):
        if k[i] == website_name:  

            #if the website's name found in the database , then it will return 1 and the password of that website in a list
            #such that l[0] = 1 and l[1] = password
    
            flag = 1
            l.append(1)
            l.append(k[i + 1])
            return l

    if flag == 0:
        #if website name not found in the database then it will return 0 in list ; l[0] = 0
        l.append(0)
        return l


# Only 3 attempts are allowed for user to input their password so we defined attempts= 3
attempts = 3

'''While loop for the no of attempts by the user
if number of attempts exceeds then 3 then loop exists'''

while (attempts > 0):
    attempts -= 1

    password_input = input("Hi there! Enter password to continue : ")

    if password_input == 'iitropar':  # Here we are defining the password = iitropar for all the user as default if he/she wants to search or add their Websites
        print('')
        print("Welcome to Password Lockbook.")
        print(
            "Do you want to search password of a saved website or want to add a new website and password?\n(Press 'A' to Add or 'S' to search) ")
        input1 = input()
        
       # Here we have given two inputs for users first for adding their websites and second if it is already exist then they can search their websites
        if input1 == 'A' or input1 == 'a':  # If input= a or A then users can add their websites
            website = input(
                "Enter website name to add (in 'xyz.com' format): ")
            # For opening the file name "datasheet"
            file = open("datasheet.txt", "a")

            if search(website)[0] == 1:

                print(
                    "An account in this website already exists\nDo you want to show me the password? (Y or N)")

                #If the websites is already exist in the datasheet
                #, then users have options they can search their alreadys exist websites password
                input2 = str(input())

                if input2 == 'y' or input2 == 'Y':  # If input = y or Y then the function name "search" search the password of already exist website
                    print('Your password for this website is : ',
                          search(website)[1])
                    break

                elif input2 == 'n' or input2 == 'N':
                    break

            else:
                
                # If the website is not exist then we add the new website in the file
                file.write(website)
                file.write("\n")
                # Here we have given a choice to users that they can generate their own password or we can provide them strong password
                password = input("\nEnter password (press 0 if you want to use a strong automated password):\n")

                if password == "0":  # If input = 0 then we provide them new password
                    
                    # Calling the function generate_password for generating strong password
                    strong_automated_password_1 = generate_password()
                    
                    print("Your Automated strong password is",
                          strong_automated_password_1)
                    
                    # Storing the generated pasword in the file
                    file.write(strong_automated_password_1)
                    file.write("\n")
                    print('Information stored successfully.')
                    break

                else:

                    # Storing the password input by the user
                    file.write(password)
                    file.write("\n")
                    print('Information stored successfully.')
                    break

                
        # If input = S or s then user can search their already exists websites in the form xyz.com
        elif input1 == 'S' or input1 == 's':
            search_website = input(
                "Enter your site name to get the password (in 'xyz.com' format): ")
            file = open("datasheet.txt", "a")
            # Calling the function search for confirming the websites is exists or not
            if search(search_website)[0] == 1:
                # If the website is exist then searching the password of that website by function search
                print('Your password for this website is : ',
                      search(search_website)[1])
                break

            # If the website searched by the user is not exists then the users have options that they can add their website
            else:
                print(
                    "No account in this website exists\nDo you want to add it? (Y or N)")
                input3 = str(input())
                '''If the user chooses Y or y then again the same process happened 
                1)The website is added to the file 
                2)Again the users have two choice first they can generate their own password and second we provide them new strong password
                3)The generated password is added to the file
                '''
                if input3 == 'y' or input3 == 'Y':
                    file.write(search_website)
                    file.write("\n")
                    password2 = input(
                        "\nEnter password (press 0 if you want to use a strong automated password):\n")

                    if password2 == "0":  # If user input = 0 then we provide them strong password
                        strong_automated_password_2 = generate_password()
                        print("Your Automated strong password is",
                              strong_automated_password_2)
                        # Storing the password in the file
                        file.write(strong_automated_password_2)
                        file.write("\n")
                        print('Information stored successfully.')
                        break

                    else:
                        # Storing the password generated by user in the file
                        file.write(password2)
                        file.write("\n")
                        print('Information stored successfully.')
                        break

                elif input3 == 'n' or input3 == 'N':
                    break

                file.close()

    else:
        if attempts>0:
            # If number of attempts exceeds then the loop exists
            print("wrong password! \ntry again,", attempts, "more attempts left")
        else:
            print("wrong again , come back later.")
