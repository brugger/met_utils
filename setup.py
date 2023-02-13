import os
from setuptools import setup
import json
import glob

def readme():
    with open('readme.md') as f:
        return f.read()

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.endswith("~"):
                continue
            paths.append(os.path.join(path, filename))
    print( paths )
    return paths

def get_version():
    with open('version.json') as json_file:
        data = json.load(json_file)

    return "{}.{}.{}".format( data['major'], data['minor'], data['patch'])

def get_requirements():

    file_handle = open('requirements.txt', 'r')
    data = file_handle.read()
    file_handle.close()

    return data.split("\n")

def scripts(directory='bin/*') -> list:
    return glob.glob( directory )

setup(name='met_utils',
      version= get_version(),
      description='python lib for met-api',
      url='https://github.com:brugger/met_utils.git',
      author='Kim Brugger',
      author_email='kbr@brugger.dk',
      packages=['met_utils'],
      license='MIT',
      install_requires=get_requirements(),
      classifiers=[
        'License :: MIT License',
        'Programming Language :: Python :: 3'
        ],
      include_package_data=True,
      zip_safe=False)
