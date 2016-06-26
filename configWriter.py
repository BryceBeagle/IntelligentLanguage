import configparser


class configWriter():

    config = configparser.ConfigParser()

    # TODO: What does this do?
    def __init__(self):

        self.createSection('flags')
        self.setSetting('flags', 'parentheses'    , '1')
        self.setSetting('flags', 'semicolons'     , '1')
        self.setSetting('flags', 'explicit_typing', '0')
        self.setSetting('flags', 'new_line_braces', '0')

        # self.setProperty('flags', 'alignment'  , '1')

        self.createSection('variables')
        self.setSetting('variables', 'var/dim',    '0')
        self.setSetting('variables', 'tab_length', '4')

        self.writeConfig()


    def createSection(self, section):

        self.config[section] = {}


    def setSetting(self, section, setting, value):

        self.config[section][setting] = value


    def writeConfig(self):

        with open('IntelligentLanguage.cfg', 'w') as configfile:
            self.config.write(configfile)
