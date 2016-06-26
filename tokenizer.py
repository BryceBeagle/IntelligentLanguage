def getWords():

    # Position of token [line, first character (inclusive), last character (exclusive)]
    lineNumber = 1

    for line in tester.readlines():

        startChar = 1
        endChar   = 1

        tempToken = ""

        # Iterate through each character
        for char in line:

            endChar += 1

            # Actions
            # ------------------------
            # Whitespace: Tokenize previous word if existent. Ignore whitespace
            # Parens    : Tokenize previous word if existent. Tokenize paren
            # Operators : Tokenize previous word if existent. Tokenize operator
            # Semicolon : Tokenize previous word if existent. Tokenize semicolon
            # New line  : Tokenize previous word if existent. Tokenize new line
            # Other     : Add character to token string

            # Whitespace (not including new line)
            if char in " \t":

                # Only add new token if there is one to add
                if tempToken != "":

                    words.append([tempToken, [lineNumber, startChar, endChar - 1]])

                    tempToken = ""

                # Move start position to current position last token
                startChar = endChar

            #
            elif char in "(){}+-*/=;\n":

                # Add previous token if there is one.
                # This is for situations where there is no space before the current character
                if tempToken != "":

                    words.append([tempToken, [lineNumber, startChar, endChar - 1]])

                    tempToken = ""

                    # Set token start position to end position of last token
                    startChar = endChar

                # Also add token for character
                words.append([char, [lineNumber, startChar, endChar]])

                startChar = endChar

            else:

                # Add character to tempToken string
                tempToken += char

        lineNumber += 1


def getTokens():

    for word in words:

        # tokenLocation = None
        tokenType  = None
        tokenValue = None

        if isNumber(word[0]):

            tokenType = 'NUMBER'
            tokenValue = float(word[0])

        elif isString(word[0]):

            tokenType = 'STRING'
            tokenValue = word[0]

        else:

            tokenTypeTemp = tokenTypes.get(word[0])

            if not tokenTypeTemp:

                tokenType = 'NAME'
                tokenValue = word[0]

            else:

                tokenType = tokenTypeTemp
                tokenValue = word[0]

        tokens.append([tokenType, tokenValue, word[1][0], word[1][1], word[1][2]])


def isNumber(test):

    try:

        float(test)
        return True, test

    except ValueError:

        return False


def isString(test):

    return '"' in test


tester = open('tester.java')

# Others are NUMBER, NAME, STRING
tokenTypes = {'for'    : 'FOR',
              'while'  : 'WHILE',
              'public' : 'ACCESS_MODIFIER',
              'private': 'ACCESS_MODIFIER',
              '('      : 'PAREN',
              ')'      : 'PAREN',
              '{'      : 'CURLY',
              '}'      : 'CURLY',
              'void'   : 'TYPE',
              'int'    : 'TYPE',
              'double' : 'TYPE',
              'String' : 'TYPE',
              'class'  : 'TYPE',
              '+'      : 'OPERATOR',
              '-'      : 'OPERATOR',
              '*'      : 'OPERATOR',
              '/'      : 'OPERATOR',
              '='      : 'EQUAL',
              ';'      : 'SEMICOLON',
              '\n'     : 'NEWLINE'
              }

words  = []
tokens = []

getWords()
getTokens()

print(words)
print(tokens)

file = open('testerOut.tkn', 'w')

for token in tokens:

    # Write tokens to file. Make sure \n's are formatted correctly
    file.write(", ".join(map(str, token[:])).replace("\n", "\\n") + "\n")

file.close()



