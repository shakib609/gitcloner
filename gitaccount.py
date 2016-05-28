import os
from gitaccounthelpers import getReposFromUrl, clone
from urllib.error import URLError, HTTPError


class GitAccount:
    def __init__(self, accountType, userName):
        self._userName = userName
        if not (accountType == 'user' or accountType == 'org'):
            raise ValueError('Invalid accountType argument: {}'.format(
                                                               accountType))
        self._accountType = accountType
        self._repoUrl = self.getRepoUrl()
        self._repos = getReposFromUrl(self._repoUrl)

    def getRepoUrl(self):
        urlPlaceholder = self._accountType + 's'
        url = 'https://api.github.com/{}/{}/repos'.format(
                                          urlPlaceholder, self._userName)
        return url

    def cloneRepos(self):
        try:
            os.mkdir(self._userName)
        except FileExistsError:
            print('{0} folder exists. Changing working directory to {0}'.
                  format(self._userName))
        except:
            print('Failed to create directory {}.'.format(self._userName))
            print('Make sure you have the right permissions.')
            raise

        os.chdir(self._userName)

        print('{} repositories to clone'.format(len(data)))
        print('Private repos have been excluded!')

        print('{} Repositories to be cloned!'.format(len(data)))
        for index, repo in enumerate(self._repos):
            print('%2d - %s' % (index + 1, repo['full_name']))

        for index, repo in enumerate(self._repos):
            print('Cloning {} - {}'.format(index + 1, repo['full_name']))
            clone(repo['clone_url'])

        print('All repositories have been cloned successfully to {}!'.format(
                                                    os.path.abspath('.')))
