#! /usr/bin/env python3
import sys
import subprocess
import os
import json
from urllib import request


def clone(url, repoName=None):
    '''Clones the git repository of url to the current directory
    Args:
        url:        git clone url of the repository
        repoName:   Name of the repo[defaults to None]
    '''
    subprocess.call(['git', 'clone', url])
    if repoName:
        print('{} cloned successfully!'.format(repoName))


def cloneRepos(name, accType):
    '''Clones all the repositories of the specified type into current directory
    Args:
        name:       user / organization name
        accType:    type of the requested account ['-u' or '-o']
'''
    if accType == '-u':
        accType = 'users'
    elif accType == '-o':
        accType = 'orgs'
    else:
        raise ValueError('accType argument must -u or -o')

    try:
        os.mkdir(name)
        os.chdir(name)
    except:
        print('Failed to create directory.')
        print('Make sure you have the right permissions and')
        print('There\'s no existing directory {}.'.format(name))
        raise

    url = 'https://api.github.com/' + accType + '/' + name + '/repos'

    try:
        data = request.urlopen(url)

    except:
        print('Please check your internet connection and try again')
        sys.exit(1)

    data = data.read().decode('UTF-8')

    data = [d for d in json.loads(data) if d['private'] is False]

    print('{} repositories to clone'.format(len(data)))
    print('Private repos have been excluded!')

    print('Repositories to be cloned!')

    for index, repo in enumerate(data):
        print('%2d - %s' % (index + 1, repo['full_name']))

    for repo in data:
        clone(repo['clone_url'], repo['full_name'])
    print('All repositories have been cloned successfully to {}!'.format(
                                                os.path.abspath('.')))


def main():
    if len(sys.argv) < 2:
        print('''Usage:
    gitcloner.py [OPTION] [NAME]

    OPTIONS:
        -u  - for user repositories
        -o  - for organization repositories
    NAME:
        Username or Organization Name
''')
        sys.exit(1)

    args = sys.argv[1:3]
    repoType, name = args
    cloneRepos(name, repoType)


if __name__ == '__main__':
    main()
