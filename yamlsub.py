from parse_cmdline import *
from replacements import *

if __name__ == "__main__":

    arguments=parse_arguments()

    if arguments.type == 'yml':

        if str(arguments.filename).endswith('.yaml') or str(arguments.filename).endswith('.yml'):
            replace_yaml(arguments.field, arguments.original_value, arguments.value_to_replace, arguments.filename)
        else:
            print('Invalid file {} for file type={}'.format(arguments.filename, arguments.type))


    elif arguments.type == 'ini':

        if str(arguments.filename).endswith('.ini'):
            replace_ini(arguments.field, arguments.original_value, arguments.value_to_replace, arguments.filename)
        else:
            print('Invalid file {} for file type={}'.format(arguments.filename, arguments.type))


    elif arguments.type == 'prop':

        if str(arguments.filename).endswith('.properties'):
            replace_application_properties(arguments.field, arguments.original_value, arguments.value_to_replace, arguments.filename)
        else:
            print('Invalid file {} for file type={}'.format(arguments.filename, arguments.type))


    else:
        print('No substitution method for this file type ,for file: {}'.format(arguments.filename))