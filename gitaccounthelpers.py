import subprocess
import json
import re
from urllib import request
import os
from urllib.parse import urlencode


def jsonToPytype(url):
    """Turn the data of the url provided into one of python data types
    Args:
        url: api url
    Returns:
        Returns the python data
    """
    try:
        req_data = request.urlopen(url).read().decode('UTF-8')
    except:
        raise
    data = json.loads(req_data)

    return data


def getReposFromUrl(baseUrl):
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
            apiData = jsonToPytype(url)
        except:
            raise
        repos.extend(apiData)
        print('{} repos fetched.'.format(len(repos)))
        if len(apiData) == 100:
            params['page'] += 1
        else:
            break
    return repos


def clone(url):
    """Clones the git repository of url to the current directory
    Args:
        url:        git clone url of the repository
    """
    repoFolderRegex = re.compile(r'.*/(.*?)\.git')
    folderName = repoFolderRegex.search(url).group(1)

    if os.path.exists(folderName):
        print('{} folder exists skipping this repo.\n'.format(folderName))
        return

    subprocess.call(['git', 'clone', url])
    print()
