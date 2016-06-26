import configWriter
import configParser
import stylizer

#TODO: Implement config.boolean
parens     = configParser.configSectionMap('Flags')['Parens']
semicolons = configParser.configSectionMap('Flags')['Semicolons']
varDim     = configParser.configSectionMap('Flags')['Var/Dim']



if parens == '0':
    stylizer.parensOff()

if semicolons == '0':
    stylizer.semicolonsOff()

if varDim != '0':
    stylizer.varDimOn(varDim)