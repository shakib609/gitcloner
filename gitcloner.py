#! /usr/bin/env python3
import sys
import subprocess
import os
import json
import re
import argparse
from urllib import request
from urllib.error import URLError, HTTPError


def urlToPytype(url):
    '''Turn the url provided into one of python data types
    Args:
        url: api url
    Returns:
        Returns the python data
    '''
    try:
        req_data = request.urlopen(url).read().decode('UTF-8')
    except:
        raise
    data = json.loads(req_data)

    return data


def getReposFromUrl(baseUrl):
    '''Get repos from a baseUrl
    Args:
        baseUrl: base url of the user/organization repos
            eg: https://api.github.com/users/shakib609/repos

    Returns:
        Returns an array containing all the repo info of the user/organization
    '''
    perPage = 100
    page = 1
    repos = []

    while True:
        url = baseUrl + '?per_page={0}&page={1}'.format(perPage, page)
        try:
            apiData = urlToPytype(url)
        except:
            raise
        repos.extend(apiData)

        print('{} repos fetched..'.format(len(repos)))
        if len(apiData) == 100:
            page += 1
        else:
            break
    return repos


def clone(url):
    '''Clones the git repository of url to the current directory
    Args:
        url:        git clone url of the repository
    '''
    repoFolderRegex = re.compile(r'.*/(.*?)\.git')
    folderName = repoFolderRegex.search(url).group(1)

    if os.path.exists(folderName):
        print('{} folder exists skipping this repo.\n'.format(folderName))
        return

    subprocess.call(['git', 'clone', url])
    print()


def cloneRepos(name, accType):
    '''Clones all the repositories of the specified type into current directory
    Args:
        name:       user / organization name
        accType:    type of the requested account ['-u' or '-o']
'''
    if accType == 'user' or accType == 'org':
        accType += 's'
    else:
        raise ValueError('accType argument must -u or -o')

    url = 'https://api.github.com/' + accType + '/' + name + '/repos'

    try:
        data = getReposFromUrl(url)

    except (URLError, HTTPError):
        print('Please check your internet connection and try again')
        sys.exit(1)

    data = [d for d in data if d['private'] is False]

    print('{} repositories to clone'.format(len(data)))
    print('Private repos have been excluded!')

    print('Repositories to be cloned!')

    try:
        os.mkdir(name)
    except FileExistsError:
        print('{0} folder exists. Changing working directory to {0}'.
              format(name))
    except:
        print('Failed to create directory {}.'.format(name))
        print('Make sure you have the right permissions.')
        raise

    os.chdir(name)

    for index, repo in enumerate(data):
        print('%2d - %s' % (index + 1, repo['full_name']))

    for index, repo in enumerate(data):
        print('Cloning {} - {}'.format(index + 1, repo['full_name']))
        clone(repo['clone_url'])

    print('All repositories have been cloned successfully to {}!'.format(
                                                os.path.abspath('.')))


def main():
    parser = argparse.ArgumentParser(
             prog='gitcloner',
             description='Clone all the repositories from a github user/org\naccount to the current directory')
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-u', '--user', help='For user accounts [DEFAULT]',
                   action='store_true')
    group.add_argument('-o', '--org', help='For organization accounts',
                       action='store_true')
    parser.add_argument('name', help='name of the user / organization')

    args = parser.parse_args()

    if not(args.user or args.org):
        args.user = True
        print('Default account type is user account')

    if args.user:
        print('Username: {}'.format(args.name))
        accType = 'user'
    else:
        print('Organization: {}'.format(args.name))
        accType = 'org'

    cloneRepos(args.name, accType)


if __name__ == '__main__':
    main()
