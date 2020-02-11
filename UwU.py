### UWU MATH OPERATIONS ###
###  BY: @NEON_ORANGE   ###
###  February 11, 2020  ###

class bcolors:
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    BLUE = '\033[34m'
    WHITE = '\033[37m'


print(bcolors.GREEN + "\n***         --------------------         ***\n")
print(bcolors.BLUE + "***   Welcome to the UwU Math Calculator   ***\n")

options = input("Enter 1 for addition.\nEnter 2 for subtraction.\nEnter 3 for multiplication.\n"
                "Enter 4 for division.\nEnter 5 for fraction multiplication.\n")
options = int(options)

if options == 1:
    print(bcolors.RED + "~uwu~ Welcome to addition! ~uwu~\n")
    value1 = input("Enter the first number here:\n")
    value2 = input("Enter the second number here:\n")
    v1 = int(value1)
    v2 = int(value2)
    print(bcolors.RED + "Here's your answer!\n")
    print(v1 + v2)
    print(bcolors.RED + "Baiiii~ see you soon ~")
    print(bcolors.GREEN + "\n***         --------------------         ***\n")
elif options == 2:
    print(bcolors.YELLOW + "~owo~ Welcome to subtraction! ~owo~\n")
    value1 = input("Enter the first number here:\n")
    value2 = input("Enter the second number here:\n")
    v1 = int(value1)
    v2 = int(value2)
    print(bcolors.YELLOW + "Here's your answer!\n")
    print(v1 - v2)
    print(bcolors.YELLOW + "Baiiii~ see you soon ~")
    print(bcolors.GREEN + "\n***         --------------------         ***\n")
elif options == 3:
    print(bcolors.GREEN + "~desu~ Welcome to multiplication! ~desu~\n")
    value1 = input("Enter the first number here:\n")
    value2 = input("Enter the second number here:\n")
    v1 = int(value1)
    v2 = int(value2)
    print(bcolors.GREEN + "Here's your answer!\n")
    print(v1 * v2)
    print(bcolors.GREEN + "Baiiii~ see you soon ~")
    print(bcolors.GREEN + "\n***         --------------------         ***\n")
elif options == 4:
    print(bcolors.MAGENTA + "~ara~ Welcome to division! ~ara~\n")
    value1 = input("Enter the first number here:\n")
    value2 = input("Enter the second number here:\n")
    v1 = int(value1)
    v2 = int(value2)
    print(bcolors.MAGENTA + "Here's your answer!\n")
    print(v1 / v2)
    print(bcolors.MAGENTA + "Baiiii~ see you soon ~")
    print(bcolors.GREEN + "\n***         --------------------         ***\n")
elif options == 5:
    print(bcolors.CYAN + "~aiya~ Welcome to fractions! ~aiya~\n")
    value1 = input("Enter the first numerator here:\n")
    value2 = input("Enter the first denominator here:\n")
    value3 = input("Enter the second numerator here:\n")
    value4 = input("Enter the second denominator here:\n")
    v1 = int(value1)
    v2 = int(value2)
    v3 = int(value3)
    v4 = int(value4)
    print(bcolors.CYAN + "Here's your answer!")
    print(v1 / v2)
    print(bcolors.CYAN + "Baiiii~ see you soon ~\n")
    print(bcolors.GREEN + "\n***         --------------------         ***\n")
else:
    print(bcolors.WHITE + "NANI!!!\nIs your brain smooth?")
    print(bcolors.GREEN + "\n***         --------------------         ***\n")





