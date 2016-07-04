import os
from gitaccount.gitaccounthelpers.gitaccounthelpers import get_repos_from_url, clone, pull, already_cloned


class GitAccount:
    """GitAccount class provides clone_repos and update_repos methods"""
    def __init__(self, account_type, userName):
        self._userName = userName
        if not (account_type == 'user' or account_type == 'org'):
            raise ValueError('Invalid accountType argument: {}'.format(
                                                               account_type))
        self._account_type = account_type
        self._repo_url = self._get_repo_url()

    def _get_repo_url(self):
        urlPlaceholder = self._account_type + 's'
        url = 'https://api.github.com/{}/{}/repos'.format(
                                          urlPlaceholder, self._userName)
        return url

    def get_repos(self):
        self._repos = get_repos_from_url(self._repo_url)
        return self._repos

    def clone_repos(self):
        repos = self.get_repos()
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

        print('{} repositories to clone'.format(len(repos)))
        print('Private repos have been excluded!')

        for index, repo in enumerate(repos, start=1):
            print('%2d - %s' % (index, repo['full_name']))
        print() # Empty line print to improve readability

        for index, repo in enumerate(repos, start=1):
            print('Cloning {} - {}'.format(index, repo['full_name']))
            clone(repo['clone_url'])

        print('All repositories have been cloned successfully to {}!'.format(
                                                    os.path.abspath('.')))
        # Back to default directory after getting result
        os.chdir('..')


    def get_already_cloned(self):
        self._already_cloned = already_cloned(self._userName)
        return self._already_cloned


    def pull_repos(self):
        already_cloned = self.get_already_cloned()
        try:
            os.chdir(self._userName)
        except FileNotFoundError:
            print('You have not cloned any repositories from {} yet'.format(
                                                            self._userName))
            print('Follow app instructions and clone first!')
            return
        except:
            raise

        print('{} repos to pull/update\n'.format(len(already_cloned)))

        for index, reponame in enumerate(already_cloned, start=1):
            print('{} - {}'.format(index, reponame))
            pull(reponame)
        os.chdir('..')

