# import yaml, pprint, os
import replacements
import argparse

def parse_arguments():
    parser=argparse.ArgumentParser(description='Substite environment variables, user input or secrets to a file')
    parser.add_argument('field', type=str)
    parser.add_argument('original_value', type=str)
    parser.add_argument('value_to_replace', type=str)
    parser.add_argument('filename', type=str)
    parser.add_argument('-t', '--type', type=str, choices=['ini', 'prop', 'yml'], default='yml', help='the type of target file (default: %(default)s)')

    args = parser.parse_args()
    return args

# read from:
# export ADMIN_PASS='#/\a!()$;asd'
# export ADMIN_PASS=http://test:8081

# os.environ auto escapes env.variables
# get_env = os.environ['ADMIN_PASS']

# yaml applies single quotes around env variable with single quotes, plain value when plain value supplied
# replacements.replace_yaml('image', 'xxx', get_env, './docker-stack-preprod.yml')

# application.properties work unescaped, write 'value' as value to file
# replacements.replace_application_properties('logging.file', 'xxx', get_env, './application.properties')

# replacements.replace_ini('admin_password', 'xxx', get_env, './grafana.ini')

