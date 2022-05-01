'''


    #
    ###
    #####
    #######
    #########
    ###########
    #############
    ###############
    #################
    ###################
    #####################
    #######################                            ###
    #########################                       ######
    ###########################                 ##########
    #############################            #############
    ###############################      #################
    ################################# ####################
    ################################   ###################
    #############################        #################
    ##########################             ###############
    ######################                   #############
    ###################                        ###########
    ################                             #########
    ############                                   #######
    #########                                        #####
    ######                                             ###
    ##                                                   #


                Quetzal-sama Secret Maker


'''

import random
import sys

class Console:
    def __init__(self):
        try:
            from rich.console import Console as RichConsole
            self.console = RichConsole()
            self.rich_available = True
        except ImportError:
            self.rich_available = False
            self.rich_tags = ['[bold]', '[italic]', '[reverse]', '[dim]', '[underline]', '[blink]', '[strike]', '[invert]', '[reset]', '[/bold]', '[/italic]', '[/reverse]', '[/dim]', '[/underline]', '[/blink]', '[/strike]', '[/invert]', '[/reset]']
    def print(self, text, style, justify):
        if self.rich_available:
            self.console.print(text, style=style, justify=justify)
        else:
            for tag in self.rich_tags:
                text = text.replace(tag, '')
            print(text)
    def input(self, text):
        if self.rich_available:
            return self.console.input(text)
        else:
            return input(text)
    def space(self, spaces):
        self.print("{}".format(' '+('\n'*(spaces-1))), style='', justify='left')
    def write(self, text):
        text = str(text)
        text = 'Message: ' + text.replace('\n', '\nMessage: ')
        self.print("{}".format(text), style='', justify='left')
    def info(self, text):
        text = str(text)
        text = 'Info: ' + text.replace('\n', '\nInfo: ')
        self.print("{}".format(text), style='cyan', justify='left')
    def warning(self, text):
        text = str(text)
        text = 'Warning: ' + text.replace('\n', '\nWarning: ')
        self.print("[dim][italic]{}[/dim][/italic]".format(text), style='yellow', justify='left')
    def error(self, text):
        text = str(text)
        text = 'Error: ' + text.replace('\n', '\nError: ')
        self.print("[bold][reverse]{}[/reverse][/bold]".format(text), style='red', justify='left')
    def success(self, text):
        text = str(text)
        text = 'Success: ' + text.replace('\n', '\nSuccess: ')
        self.print("[bold]{}[/bold]".format(text), style='green', justify='left')
    def question(self, text):
        text = str(text)
        text = 'Question: ' + text.replace('\n', '\nQuestion: ')
        self.print("[bold]{}[/bold]".format(text), style='magenta', justify='left')
        return self.input('> ')
    def version_italic(self, text):
        text = str(text)
        self.print("[italic]{}[/italic]".format(text), style='', justify='center')
    def version_italic_bold(self, text):
        text = str(text)
        self.print("[bold][italic]{}[/italic][/bold]".format(text), style='', justify='center')
    def version_reverse(self, text):
        text = str(text)
        self.print("[reverse]{}[/reverse]".format(text), style='', justify='center')
    def version_natural(self, text):
        text = str(text)
        self.print("{}".format(text), style='', justify='center')
    def help_natural(self, text, tabs):
        text = str(text)
        self.print("{}{}".format('   '*tabs, text), style='', justify='left')
    def help_italic(self, text, tabs):
        text = str(text)
        self.print("{}[italic]{}[/italic]".format('   '*tabs, text), style='', justify='left')
    def help_reverse(self, text, tabs):
        text = str(text)
        self.print("{}[reverse]{}[/reverse]".format('   '*tabs, text), style='', justify='left')
    def help_bold(self, text, tabs):
        text = str(text)
        self.print("{}[bold]{}[/bold]".format('   '*tabs, text), style='', justify='left')
    def help_italic_bold(self, text, tabs):
        text = str(text)
        self.print("{}[italic][bold]{}[/bold][/italic]".format('   '*tabs, text), style='', justify='left')

class main_info:
    def __init__(self):
        self.version = '1.2'
        self.author = 'Quetzal-sama'
        self.name = 'Secret Maker'
        self.description = 'A simple password generator'
        self.contributors = 'Ismael P. Santana'
        self.license = 'None'
        self.link = 'https://password.kaspersky.com/'
        self.logo = [
            '▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '█████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '███████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '█████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '███████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '█████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '███████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '█████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '███████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '█████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',
            '███████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██',
            '█████████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█████',
            '███████████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█████████',
            '█████████████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▓████████████',
            '███████████████████████████████▓▒▒▒▒▒▓▓███████████████',
            '█████████████████████████████████▓▓███████████████████',
            '███████████████████████████████▓▓▒▓███████████████████',
            '████████████████████████████▓▒▒▒▒▒▒▒▓█████████████████',
            '█████████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▓███████████████',
            '█████████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█████████████',
            '██████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███████████',
            '███████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█████████',
            '███████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███████',
            '████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█████',
            '█████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███',
            '▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓',
        ]
        self.console = Console()
    def about(self):
        if True:
            self.console.space(1)
            for i in self.logo:
                # i = i.replace('', "")
                # i = i.replace('▒', " ‎")
                # i = i.replace('▓', "▓")
                # i = i.replace('█', "█")
                self.console.version_natural(i)
        self.console.space(1)
        self.console.version_reverse(self.name)
        self.console.version_italic_bold('by ' + self.author)
        self.console.version_italic(self.description  + ' v' + self.version)
        # self.console.version_italic('Contributors: ' + self.contributors)
        # self.console.version_italic('License: ' + self.license)
        self.console.space(1)
    def help(self):
        # Usage:
        #   secmaker <length> <options>
        # Options:
        #   -n --numbers <numbers> : Add numbers to the password
        #   -s --symbols <symbols> : Add symbols to the password
        #   -c --capital <capital> : Add capital letters to the password
        #   -l --lower <lower> : Add lower letters to the password
        #   -a --all : Add all stuff to the password
        #   -p --password <password> : Use a password instead of a random one
        #   -h --help : Show this help
        #   -v --version : Show the version
        # Notes:
        #   --numbers, --symbols, --capital, --lower, --all and --password are optional
        #   --all is the default option if none is specified
        #   --password is used to use a password instead of a random one, the length won't be ignored
        #   --numbers, --symbols, --capital and --lower length are optional
        #   if you want to check if the password is strong, use the following link: {link}
        #   the default length is 14
        # Third-party libraries:
        #   rich : Show colors and other fancy stuff
        #   pyperclip : Copy to clipboard
        self.console.help_bold('Usage:', 1)
        self.console.help_italic_bold('secmaker <length> <options>', 2)
        self.console.space(1)
        self.console.help_bold('Options:', 1)
        self.console.help_natural('-n --numbers <numbers> : Add numbers to the password', 2)
        self.console.help_natural('-c --capital <capital> : Add capital letters to the password', 2)
        self.console.help_natural('-l --lower <lower> : Add lower letters to the password', 2)
        self.console.help_natural('-s --symbols <symbols> : Add symbols to the password', 2)
        self.console.help_natural('-a --all : Add all stuff to the password, except symbols', 2)
        self.console.help_natural('-p --password <password> : Use a password instead of a random one', 2)
        self.console.help_natural('-h --help : Show this help', 2)
        self.console.help_natural('-v --version : Show the version', 2)
        self.console.space(1)
        self.console.help_bold('Notes:', 1)
        self.console.help_natural('--numbers, --symbols, --capital, --lower, --all and --password are optional', 2)
        self.console.help_natural('--all is the default option if none is specified', 2)
        self.console.help_natural('--password is used to use a password instead of a random one, the length won\'t be ignored', 2)
        self.console.help_natural('--numbers, --symbols, --capital and --lower length are optional', 2)
        self.console.help_natural('the default length is 14', 2)
        self.console.help_natural('if you want to check if the password is strong, use the following link: ' + self.link, 2)
        self.console.space(1)
        self.console.help_bold('Third-party libraries:', 1)
        self.console.help_natural('rich : Show colors and other fancy stuff', 2)
        self.console.help_natural('pyperclip : Copy to clipboard', 2)

def __main__():
    # Create a console object
    console = Console()
    # Create an info object
    info = main_info()
    # Get the arguments
    args = sys.argv
    # Possible options
    full_options = ['--numbers', '--symbols', '--capital', '--lower', '--all', '--password', '--help', '--version']
    short_options = ['-n', '-s', '-c', '-l', '-a', '-p', '-h', '-v']
    # Replace the full options with the short ones
    for i in range(len(full_options)):
        if full_options[i] in args:
            args[args.index(full_options[i])] = short_options[i]
    # Check if the user wants to see the help
    if '-h' in args:
        info.help()
        sys.exit()
    # Check if the user wants to see the version
    if '-v' in args:
        info.about()
        sys.exit()
    # Check if length is specified
    try:
        if not args[1] in short_options:
            # Try to convert the length to an integer
            try:
                length = int(args[1])
            except Exception:
                # Error
                console.error('The length must be an number')
                sys.exit()
        else:
            # Warning
            console.warning('The length is not specified, using the default length of 14')
            # Set the length to 14
            length = 14
    except Exception:
        # Warning
        console.warning('The length is not specified, using the default length of 14')
        # Set the length to 14
        length = 14
    # Check if the user wants to use a password instead of a random one
    if '-p' in args:
        # Check if the password is specified
        try:
            if not args[args.index('-p') + 1] in short_options:
                # Try to convert the password to a string
                try:
                    password = str(args[args.index('-p') + 1])
                except Exception:
                     # Force an Exception
                    raise Exception
        except Exception:
            # Error
            console.error('The password is not specified')
            sys.exit()
    else:
        password = ''
    # Start numbers with 0
    numbers = 0
    # Check if the user wants to add numbers to the password
    if '-n' in args:
        # Check if the numbers are specified
        try:
            if not args[args.index('-n') + 1] in short_options:
                # Try to convert the numbers to an integer
                try:
                    numbers = round(int(args[args.index('-n') + 1]))
                except Exception:
                    # Error
                    console.error('The numbers must be an number')
                    sys.exit()
            else:
                # Force an Exception
                raise Exception
        except Exception:
            # Warning
            console.warning('The numbers are not specified')
    # Start symbols with -1
    symbols = -1
    # Check if the user wants to add symbols to the password
    if '-s' in args:
        # Check if the symbols are specified
        try:
            if not args[args.index('-s') + 1] in short_options:
                # Try to convert the symbols to an integer
                try:
                    symbols = round(int(args[args.index('-s') + 1]))
                except Exception:
                    # Error
                    console.error('The symbols must be an number')
                    sys.exit()
            else:
                # Force an Exception
                raise Exception
        except Exception:
            # Warning
            console.warning('The symbols are not specified')
            # Set the symbols to 0
            symbols = 0
    # Start capital with 0
    capital = 0
    # Check if the user wants to add capital letters to the password
    if '-c' in args:
        # Check if the capital letters are specified
        try:
            if not args[args.index('-c') + 1] in short_options:
                # Try to convert the capital letters to an integer
                try:
                    capital = round(int(args[args.index('-c') + 1]))
                except Exception:
                    # Error
                    console.error('The capital letters must be an number')
                    sys.exit()
            else:
                # Force an Exception
                raise Exception
        except Exception:
            # Warning
            console.warning('The capital letters are not specified')
    # Start lower with 0
    lower = 0
    # Check if the user wants to add lower letters to the password
    if '-l' in args:
        # Check if the lower letters are specified
        try:
            if not args[args.index('-l') + 1] in short_options:
                # Try to convert the lower letters to an integer
                try:
                    lower = round(int(args[args.index('-l') + 1]))
                except Exception:
                    # Error
                    console.error('The lower letters must be an number')
                    sys.exit()
            else:
                # Force an Exception
                raise Exception
        except Exception:
            # Warning
            console.warning('The lower letters are not specified')
    # Check if the user wants to add all stuff to the password
    if '-a' in args:
        all_stuff = True
    else:
        all_stuff = False
    # Check if nothing is specified
    if not all_stuff:
        # Set all stuff to True
        all_stuff = True
        # Check numbers, symbols, capital and lower
        if not numbers and not symbols and not capital and not lower:
            # Warning
            console.warning('Nothig is specified, using the default options')
    # Check if all stuff is specified
    if all_stuff:
        # Set numbers, symbols, capital and lower with the spaces variable
        spaces = 4
        digits = length
        # Check numbers
        if not numbers == 0:
            digits = digits - numbers
            spaces = spaces - 1
        # Check symbols
        if not symbols == 0:
            digits = digits - symbols
            spaces = spaces - 1
        # Check capital
        if not capital == 0:
            digits = digits - capital
            spaces = spaces - 1
        # Check lower
        if not lower == 0:
            digits = digits - lower
            spaces = spaces - 1
        # Check spaces
        if not spaces == 0:
            # Check numbers
            if numbers == 0:
                numbers = digits / spaces
            # Check symbols
            if symbols == 0:
                symbols = digits / spaces
            # Check capital
            if capital == 0:
                capital = digits / spaces
            # Check lower
            if lower == 0:
                lower = digits / spaces
    # Force integer
    numbers = round(numbers)
    symbols = round(symbols)
    capital = round (capital)
    lower = round(lower)
    # Define lowercase characters
    all_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Define uppercase characters
    all_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # Define numbers
    all_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Define symbols
    all_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '<', '>', ',', '.', '?']
    # Check if the user wants to use a password instead of a random one
    if password != '':
        # Check if the password lenght is less than the length
        if len(password) < length:
            # Warning
            console.warning('The password is shorter than the length, duplicating the password')
            # Duplicate the password
            while len(password) < length:
                password = password + password[random.randint(0, len(password)):(random.randint(0, len(password)))]
        # Chech if the password lenght is greater than the length
        if len(password) > length:
            # Warning
            console.warning('The password is longer than the length, cutting the password')
            # Cut the password
            password = password[:length]
        # Change the password to list
        password = list(password)
        # Replace password parts with random characters
        for i in range(numbers):
            # Force loop
            loops = 0
            while loops < numbers:
                # Shuffle the numbers
                random.shuffle(all_numbers)
                # Find a number in the password
                if all_numbers[i] in password:
                    # Replace the number with a random number
                    password[password.index(all_numbers[i])] = random.choice(all_numbers)
                    # Break the loop
                    break
                else:
                    # Increase the loop
                    loops += 1
        for i in range(symbols):
            # Force loop
            loops = 0
            while loops < symbols * 2:
                # Shuffle the symbols
                random.shuffle(all_symbols)
                # Find a symbol in the password
                if all_symbols[i] in password:
                    # Replace the symbol with a random symbol
                    password[password.index(all_symbols[i])] = random.choice(all_symbols)
                    # Break the loop
                    break
                else:
                    # Increase the loop
                    loops += 1
        for i in range(capital):
            # Force loop
            loops = 0
            while loops < capital * 2:
                # Shuffle the capital letters
                random.shuffle(all_uppercase)
                # Find a capital letter in the password
                if all_uppercase[i] in password:
                    # Set the capital letter to lowercase
                    password[password.index(all_uppercase[i])] = all_uppercase[i].lower()
                    # Break the loop
                    break
                else:
                    # Increase the loop
                    loops += 1
        for i in range(lower):
            # Force loop
            loops = 0
            while loops < lower * 2:
                # Shuffle the lower letters
                random.shuffle(all_lowercase)
                # Find a lower letter in the password
                if all_lowercase[i] in password:
                    # Set the lower letter to uppercase
                    password[password.index(all_lowercase[i])] = all_lowercase[i].upper()
                    # Break the loop
                    break
                else:
                    # Increase the loop
                    loops += 1
        # Convert the password to a string
        password = ''.join(password)
        # Print the success message
        console.success('The password was updated successfully')
    else:
        # Generate a random password
        password = ''
        # Generate the numbers
        for i in range(numbers):
            # Shuffle the numbers
            random.shuffle(all_numbers)
            # Add a number
            password += all_numbers[0]
        # Generate the symbols
        for i in range(symbols):
            # Shuffle the symbols
            random.shuffle(all_symbols)
            # Add a symbol
            password += all_symbols[0]
        # Generate the capital letters
        for i in range(capital):
            # Shuffle the capital letters
            random.shuffle(all_uppercase)
            # Add a capital letter
            password += all_uppercase[0]
        # Generate the lower letters
        for i in range(lower):
            # Shuffle the lower letters
            random.shuffle(all_lowercase)
            # Add a lower letter
            password += all_lowercase[0]
        # Check if the password is less than the length
        if len(password) < length:
            # Duplicate the password
            while len(password) < length:
                password = password + password[random.randint(0, len(password)):(random.randint(0, len(password)))]
        # Check if the password is greater than the length
        if len(password) > length:
            # Cut the password
            password = password[:length]
        # Shuffle the password
        password = list(password)
        random.shuffle(password)
        # Convert the password to a string
        password = ''.join(password)
        # Cut the password
        password = password[:length]
        # Print the success message
        console.success('The password was generated successfully')

    # Print the password
    console.help_italic(password, 1)

    # Try to copy the password to the clipboard
    try:
        import pyperclip
    except Exception:
        # Error
        console.error('The password could not be copied to the clipboard')
    else:
        # Copy the password to the clipboard
        pyperclip.copy(password)
        # Print the success message
        console.success('The password was copied to the clipboard')

# Main function
try:
    __main__()
except Exception:
    # Print the error message
    sys.exit('\n    :(\n    An fatal error has occurred\n    Please check the code and try again\n')