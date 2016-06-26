import configparser

config = configparser.ConfigParser()
config.read('IntelligentLanguage.cfg')

def configSectionMap(section):

    dictionary = {}
    options = config.options(section)

    for option in options:

        try:

            dictionary = {config.get(section, option)}

        except:

            print("Exception on %s!" % option)
            dictionary[option] = None

    return dictionary

