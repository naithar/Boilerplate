#!/usr/bin/python

def help(parameters): # help for scrypt
    print 'python boilderplate scrypt'
    print 'help for {0}'.format(parameters)

def run(filename, toFilename, parameters = None): # perform file formatting
    string = ''
    with open(filename, "r") as original:
        string = original.read()
        original.close()

    print 'Original file content:'
    print string

    print 'Parameters:'
    print parameters

    newString = string.format(**parameters)
    print 'Formated file content:'
    print newString

    with open(toFilename, "w") as new:
        new.write(newString)
        new.close()

def main(args):
    print __name__
    print args

    if '--help' in args:
        args.remove('--help')
        help(args)
    elif '-h' in args:
        args.remove('-h')
        help(args)



if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
