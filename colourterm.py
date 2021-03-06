#--------------------------------------------------------------------------------------------------

terminalFormats = {
'HEADER': '\033[95m',
'OKBLUE': '\033[94m',
'OKGREEN': '\033[92m',
'WARNING': '\033[93m',
'FAIL': '\033[91m',
'ENDC': '\033[0m',
'BOLD': '\033[1m',
'ITALIC': '\033[3m',
'UNDERLINE': '\033[4m'}

#--------------------------------------------------------------------------------------------------

def tform(string, format):
    return str(terminalFormats[format]+string+terminalFormats['ENDC'])

#--------------------------------------------------------------------------------------------------