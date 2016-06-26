import sys
import configWriter


def queryYesNo(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".

    http://stackoverflow.com/questions/3041986/python-command-line-yes-no-input

    """
    valid = {"yes": True, "y": True, "ye": True, "1": True,
             "no": False, "n": False, "0": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


parentheses    = queryYesNo("Do you want parentheses?")
semicolons     = queryYesNo("Do you want semicolons?")
explicitTyping = queryYesNo("Do you want explicit typing?")
newLineBraces  = queryYesNo("Do you want new lines after opening curly braces?")

# TODO: Allow user to yet the keyword if the answer is no
varDim         = queryYesNo("Do you want keywords such as var/dim?")
if varDim: varDim = input("What do you want the keyword to be? ")
else: varDim = '0'

tabs = input("What size tabs do you want? ")

# TODO: Make this better looking
writer = configWriter.configWriter()

writer.setSetting('flags', 'parentheses',     ('0', '1')[parentheses   ])
writer.setSetting('flags', 'semicolons' ,     ('0', '1')[semicolons    ])
writer.setSetting('flags', 'explicit_typing', ('0', '1')[explicitTyping])
writer.setSetting('flags', 'new_line_braces', ('0', '1')[newLineBraces ])

writer.setSetting('variables', 'var/dim', varDim)
writer.setSetting('variables', 'tabs',    tabs)

writer.writeConfig()
