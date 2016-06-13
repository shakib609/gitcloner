import subprocess
import json
import re
import os
import sys
from urllib import request
from urllib.parse import urlencode
from urllib.error import URLError, HTTPError


def fetch_api_data(url):
    """Turn the api data of the url provided into one of python data types
    Args:
        url: api url
    Returns:
        Returns the python data
    """
    with request.urlopen(url) as req:
        req_data = req.read().decode('UTF-8')
    return json.loads(req_data)


def get_repos_from_url(baseUrl):
    """Get repos from a baseUrl
    Args:
        baseUrl: base url of the user/organization repos
            eg: https://api.github.com/users/shakib609/repos

    Returns:
        Returns an array containing all the repo info of the user/organization
    """
    params = {
        'per_page': 100,
        'page': 1
    }
    repos = []

    while True:
        url = baseUrl + '?%s' % urlencode(params)
        try:
            apiData = fetch_api_data(url)
        except (URLError, HTTPError):
            print('Please Check your internet connection and try again!')
            sys.exit()
        repos.extend(apiData)
        print('{} repos fetched.'.format(len(repos)))
        if len(apiData) == params['per_page']:
            params['page'] += 1
        else:
            return [repo for repo in repos if not repo['private']]


def clone(url):
    """Clones the git repository of url to the current directory
    Args:
        url:        git clone url of the repository
    """
    repoFolderRegex = re.compile(r'.*/(.*?)\.git')
    folderName = repoFolderRegex.search(url).group(1)

    if os.path.exists(folderName):
        print('{} has been cloned successfully before!'.format(folderName))
        print('Skipping this repo.\n')
        return

    subprocess.call(['git', 'clone', url])
    print()
