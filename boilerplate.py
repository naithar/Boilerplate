#!/usr/bin/python

def help(parameters = None): # help for scrypt
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

def parse(arguments):
    print 'parsing {0}'.format(arguments)
    return {}

def main(args):
    print __name__
    print args

    if '--help' in args:
        args.remove('--help')
        help(args)
    elif '-h' in args:
        args.remove('-h')
        help(args)
    elif args[0] == 'run':
        filename = args[1] #should contain .bp new file name drops .bp
        newFilename = ''
        parameters = parse(args[2:]) # -p, --parameters
        run(filename, newFilename, parameters)
    else:
        print 'Can not parse commandline'
        help()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
