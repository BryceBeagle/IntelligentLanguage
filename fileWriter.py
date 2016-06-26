def tokenPrint(currentToken):

    pass

def spacePrint(currentToken, nextToken):

    pass


import configparser

testerConf = open('testerOut.tkn')
testerUser = open('generatedJava.java', 'w')

config = configparser.ConfigParser()
config.read('IntelligentLanguage.cfg')

indentLevel = 0

parentheses    =     config.getboolean('flags'    , 'parentheses'    )
semicolons     =     config.getboolean('flags'    , 'semicolons'     )
explicitTyping =     config.getboolean('flags'    , 'explicit_typing')
newLineBraces  =     config.getboolean('flags'    , 'new_line_braces')
varDim         =     config.get       ('variables', 'var/dim'        )
tabLength      = int(config.get       ('variables', 'tab_length'     ))

outputString = ""
for line in testerConf.readlines():

    token = line.split(', ')

    nextType = None

    if token[0] == 'ACCESS_MODIFIER':

        outputString += token[1] + " "

    elif token[0] == 'TYPE':

        if explicitTyping:

            outputString += token[1] + " "

        else:

            if token[1] == 'int':

                nextType = 'int'

            elif token[1] == 'double':

                nextType = 'double'

            else:

                outputString += token[1] + " "

    elif token[0] == 'NUMBER':

        if nextType is None:

            outputString += token[1] + " "

        else:

            if nextType == 'int':

                outputString += token[1]

            elif nextType == 'double':

                if '.' in token[1]:

                    outputString += token[1]

                else:

                    outputString += token[1] + "."

            nextType = None

    elif token[0] == 'NAME':

        outputString += token[1] + " "

    elif token[0] == 'CURLY':

        if token[1] == '{':

            if newLineBraces:

                outputString += "\n"
                outputString += (" " * tabLength * indentLevel) + token[1]

            else:

                outputString += " " + token[1] + "\n"
                outputString += (" " * tabLength * indentLevel)

            indentLevel += 1

        else:

            indentLevel -= 1

            # Remove tab from end of string. We need to shift left
            outputString = outputString[:-tabLength]

            outputString += token[1] + "\n"
            outputString += (" " * tabLength * indentLevel)

    elif token[0] == 'PAREN':

        outputString += token[1]

    elif token[0] == 'OPERATOR':

        outputString += " " + token[1] + " "

    elif token[0] == 'EQUAL':

        outputString += " " + token[1] + " "

    elif token[0] == 'SEMICOLON':

        if semicolons:

            outputString += token[1]

    elif token[0] == 'NEWLINE':

        outputString += "\n"
        outputString += " " * tabLength * indentLevel

    elif token[0] == 'FOR':

        outputString += token[1] + " "

    elif token[0] == 'WHILE':

        outputString += token[1] + " "

    elif token[0] == 'STRING':

        outputString += token[1] + " "

testerUser.write(outputString)


