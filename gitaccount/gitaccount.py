import os
from gitaccount.gitaccounthelpers.gitaccounthelpers import get_repos_from_url, clone


class GitAccount:
    def __init__(self, account_type, userName):
        self._userName = userName
        if not (account_type == 'user' or account_type == 'org'):
            raise ValueError('Invalid accountType argument: {}'.format(
                                                               account_type))
        self._account_type = account_type
        self._repo_url = self.get_repo_url()
        self._repos = get_repos_from_url(self._repo_url)

    def get_repo_url(self):
        urlPlaceholder = self._account_type + 's'
        url = 'https://api.github.com/{}/{}/repos'.format(
                                          urlPlaceholder, self._userName)
        return url

    def clone_repos(self):
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

        print('{} repositories to clone'.format(len(self._repos)))
        print('Private repos have been excluded!')

        for index, repo in enumerate(self._repos):
            print('%2d - %s' % (index + 1, repo['full_name']))

        for index, repo in enumerate(self._repos):
            print('Cloning {} - {}'.format(index + 1, repo['full_name']))
            clone(repo['clone_url'])

        print('All repositories have been cloned successfully to {}!'.format(
                                                    os.path.abspath('.')))
