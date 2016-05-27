#! /usr/bin/env python3
import sys
from gitaccount import GitAccount


def main():
    if len(sys.argv) < 2:
        print("""Usage:
    gitcloner.py [OPTION] [NAME]

    OPTIONS:
        -u  - for user repositories
        -o  - for organization repositories
    NAME:
        Username or Organization Name
""")
        sys.exit(1)

    args = sys.argv[1:3]
    repoType, name = args
    if repoType == '-u':
        repoType = 'user'
    elif repoType == '-o':
        repoType = 'org'
    else:
        raise ValueError()

    account = GitAccount(repoType, name)
    account.cloneRepos()


if __name__ == '__main__':
    main()
