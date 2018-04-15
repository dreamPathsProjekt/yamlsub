import yaml, pprint, os
import replacements

# with open('./docker-stack-preprod.yml') as file:
#     data = yaml.load(file)

# found = list(find_key('name', data))

# found_key = list(get_key('image', data))

# replace_key('image', 'sixeyed/password-web:v2', 'something', data)

# pprint.pprint(data)
# print("\n\n")
# # pprint.pprint(list(new_data))

# with open('./docker-stack-preprod.yml', 'w') as file:
#     yaml.dump(data, file)
get_env = os.environ['ADMIN_PASS']
# replacements.replace_yaml('image', 'sixeyed/password-web:v2', get_env, './docker-stack-preprod.yml')
replacements.replace_application_properties('logging.file', 'testvalue', get_env, './application.properties')
# !$^%)(\a

replacements.replace_ini('admin_password', 'xxx', get_env, './grafana.ini')

