# YamlSub

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

- [YamlSub](#yamlsub)
  - [Description](#description)
  - [Requirements](#requirements)
  - [Packages](#packages)
  - [Installation](#installation)
    - [Using virtualenv](#using-virtualenv)
    - [Install using setuptools](#install-using-setuptools)
    - [Create executable](#create-executable)
  - [Usage](#usage)
    - [Examples](#examples)
      - [Substitution in `.yml` files](#substitution-in-yml-files)
  - [Notes](#notes)

## Description

This command line tool is for all those use-cases when you need to substitute __in-place__ values inside `.yml`, `application.properties` and `.ini` files.

For example, you may need to include environment variables, secrets or configuration specific values to different environments, applications running in Docker etc.

Usually configuration management is performed by substituting dummy values, using arcane `sed` sequences or `awk` functions that are, sometimes, not re-usable enough.

The __yamlsub__ cmd line tool tries to simplify this process and in future versions attempt to include more filetype usecases and target substitution patterns that take into account filetype-specific intricacies.

As of version: 0.1 the tool supports value substitution for `.yml` or `.yaml` files, `application.properties` files and a currently, experimental feature to replace values inside `.ini` files.

## Requirements

This tool has been tested with **python version: 3.5** on **Ubuntu: 16.04**

To see your distro release and Python version:

```Shell
lsb_release -a

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.4 LTS
Release:        16.04
Codename:       xenial
```

Python version:

```Shell
user@server:~ $ python3 --version
Python 3.5.2
```

## Packages

- [PyYaml](https://pypi.python.org/pypi/pyaml)
- [PyInstaller](https://pypi.python.org/pypi/PyInstaller/3.3.1)

[setup.py](./setup.py)

```Python
setup(
    name="yamlsub",
    version="0.1",
    packages=find_packages(),


    install_requires=[
        "pyaml",
        "pyinstaller"
    ],

    # metadata for upload to PyPI
    author="Ioannis Dritsas",
    author_email="dream.paths.projekt@gmail.com",
    description="Easily substitute values in .yaml files",
    license="MIT",
    keywords="",
)
```

## Installation

Clone this repository:

```Shell
git clone https://github.com/dreamPathsProjekt/yamlsub
```

### Using virtualenv

Cd to repo folder and activate virtalenv

```Shell
cd yamlsub
source bin/activate
```

With virtualenv activated:

```Shell
(yamlsub) user@server:~/yamlsub (master)$ python yamlsub.py -h


usage: yamlsub.py [-h] [-t {ini,prop,yml}]
                  field original_value value_to_replace filename

Substite environment variables, user input or secrets to a file

positional arguments:
  field
  original_value
  value_to_replace
  filename

optional arguments:
  -h, --help            show this help message and exit
  -t {ini,prop,yml}, --type {ini,prop,yml}
                        the type of target file (default: yml)

```

### Install using setuptools

```Shell
python3 setup.py install
```

### Create executable

If you want to install the yamlsub tool as an executable script:

```Shell
(yamlsub) user@server:~/yamlsub (master)$ pyinstaller yamlsub.py
```

Deactivate virtualenv and find executable in `dist/yamlsub` folder:

```Shell
(yamlsub) user@server:~/yamlsub (master)$ deactivate
user@server:~/yamlsub (master)$ cd dist/yamlsub/

user@server:~/yamlsub/dist/yamlsub (master)$ ./yamlsub -h
```

## Usage

```Bash
usage: yamlsub [-h] [-t {ini,prop,yml}]
               field original_value value_to_replace filename

Substite environment variables, user input or secrets to a file

positional arguments:
  field
  original_value
  value_to_replace
  filename

optional arguments:
  -h, --help            show this help message and exit
  -t {ini,prop,yml}, --type {ini,prop,yml}
                        the type of target file (default: yml)
```

### Examples

#### Substitution in `.yml` files

Scenario: we have a Docker Stack file that we need to substitute the image field in the `password-web` service but not in the service named `password-api`

Original file `docker-compose.yml`:

```YAML
  password-api:
    deploy:
      endpoint_mode: dnsrr
      placement:
        constraints: [node.platform.os == windows]
      replicas: 4
    image: sixeyed/password-api:v3
    networks: {analytics-net: null, dmz-net: null}
  password-web:
    deploy:
      placement:
        constraints: [node.platform.os == linux, node.role == worker]
      replicas: 6
    environment: {'PasswordApi:Url': 'http://api.sixeyed.com'}
    image: sixeyed/password-web:v4
    networks: {dmz-net: null}
```

Usage:

```Shell
python3 yamlsub.py <field> <current value> <replacement value> <file> -t yml
```

```Bash
python3 yamlsub.py image sixeyed/password-web:v4 sixeyed/something-else:v1 <path-to>/docker-compose.yml

# Or by using installed executable
<path-to-dist-folder>/yamlsub image sixeyed/password-web:v4 sixeyed/something-else:v1 <path-to>/docker-compose.yml
```

Final `docker-compose.yml` file:

```YAML
  password-api:
    deploy:
      endpoint_mode: dnsrr
      placement:
        constraints: [node.platform.os == windows]
      replicas: 4
    image: sixeyed/password-api:v3
    networks: {analytics-net: null, dmz-net: null}
  password-web:
    deploy:
      placement:
        constraints: [node.platform.os == linux, node.role == worker]
      replicas: 6
    environment: {'PasswordApi:Url': 'http://api.sixeyed.com'}
    image: sixeyed/something-else:v1
    networks: {dmz-net: null}
```

As you see from the above scenario, values are not substituted for both `image` fields, but only for the specified `original_value`.

```YAML
  image: original_value
```

## Notes

- For `.yml` files all `null` values are replaced with `None` in the returned Python `dict` as of __PyYaml__ specifications of `yaml.load()` and `yaml.dump()`. The opposite is also true (`None` values are written as `null` in the output `yaml` file).

`replace_yaml` function implementation using `PyYaml` package:

```Python
import yaml
from helpers import find_key, get_key, replace_key, replace_property, escape_dquotes, escape_url_encode


def replace_yaml(field, original_value, replacement_value, filename):

    replacement_value=escape_url_encode(replacement_value)

    with open(filename) as file:
        data = yaml.load(file)

    replace_key(field, original_value, replacement_value, data)

    with open(filename, mode='w') as file:
        yaml.dump(data, file)
```