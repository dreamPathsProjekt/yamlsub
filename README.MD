# YamlSub v:0.1

## Description

## Requirements

This tool has been tested with **python:3.5** on **Ubuntu:16.04**

To see your Distro release and Python version:

```Shell
lsb_release -a

# Python version
users@server:~ $ python3 --version
Python 3.5.2
```

## Packages

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
user@server:~/yamlsub (master)$cd dist/yamlsub/

user@server:~/yamlsub/dist/yamlsub (master)$ ./yamlsub -h


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