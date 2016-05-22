#! /usr/bin/env python3
import requests
import sys
import subprocess
import os


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

    data = requests.get(url)

    if not data.ok:
        print('Please check your internet connection and try again')
        print('Request returned: {}'.format(data.status_code))
        sys.exit(1)

    # data = json.loads(data.text)

    data = [d for d in data.json() if d['private'] is False]

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

    repoType = sys.argv[1]
    name = sys.argv[2]
    cloneRepos(name, repoType)


if __name__ == '__main__':
    main()
