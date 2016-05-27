import os
from gitaccounthelpers import getReposFromUrl, clone
from urllib.error import URLError, HTTPError


class GitAccount:
    def __init__(accountType, userName):
        self._userName = userName
        if not (accountType == 'user' or accountType == 'org'):
            raise ValueError('Invalid accountType argument: {}'.format(
                                                               accountType))
        self._accountType = accountType
        self._repoUrl = self.getRepoUrl()
        self._repos = getReposFromUrl(self._repoUrl)

    def getRepoUrl():
        urlPlaceholder = self._accountType + 's'
        url = 'https://api.github.com/{}/{}/repos'.format(
                                          urlPlaceholder, self._userName)
        return url

    def cloneRepos():
        try:
            data = getReposFromUrl(self._repoUrl)
        except (URLError, HTTPError):
            print('Please check your internet connection and try again')
            sys.exit(1)

        data = [d for d in data if d['private'] is False]

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

        print('{} repositories to clone'.format(len(data)))
        print('Private repos have been excluded!')

        print('Repositories to be cloned!')
        for index, repo in enumerate(data):
            print('%2d - %s' % (index + 1, repo['full_name']))

        for index, repo in enumerate(data):
            print('Cloning {} - {}'.format(index + 1, repo['full_name']))
            clone(repo['clone_url'])

        print('All repositories have been cloned successfully to {}!'.format(
                                                    os.path.abspath('.')))
