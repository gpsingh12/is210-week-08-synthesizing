 #!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""Module 2."""

import authentication
import getpass

def login(username, maxattempts = 4):
    """Function takes two inputs from the users to input their username
       and maximum attempts.
       Arg:
           username(str): A string asking the user to input username.
           maxattempts(int): Maximum no. of attempts for the user.
        Return:
            returns True or False if user successfully authenticated
            before hitting maximum no. of failed attempts.
        Examples:
                >>>login('mike', 4)
                    Incorrect username or password. You have4attempts
                    Incorrect username or password. You have3attempts
                    Incorrect username or password. You have2attempts
                    Incorrect username or password. You have1attempts
                    Incorrect username or password. You have0attempts
                    False

    """
    authenticated = False
   #maxattempts = 4
    
    prompt = 'Please enter your password: '
    userinput = "Incorrect username or password. You have" ' {} '  "attempts"
    
    counter = 0
    while counter <= maxattempts:
        password = getpass.getpass(prompt)
        message = authentication.authenticate(username, password)
        if message:
            authenticated = True
            break
        else:
            
            print userinput.format(maxattempts - counter )
            counter += 1

    return authenticated
    
