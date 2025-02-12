
# funtions go here

def yes_no(question):

    """checks user response a question is yes / no (y/n), returns 'yes' or 'no' """


    while True:

        response = input(question).lower()

        # make sure user says yes or no
        if response == "yes" or response == "y":
            return "Yes"
        elif response == "no" or response == "n":
           return "no"
        else:
            print(" pls enter Yes or no")

# main routine

want_intrustions = yes_no("do you want to see the instrutions?").lower()
want_coffee = yes_no("do you want coffee?")


print("we're done")


