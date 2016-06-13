#! /usr/bin/env python3
import argparse
from gitaccount import GitAccount


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

    account = GitAccount(accType, args.name)
    account.clone_repos()


if __name__ == '__main__':
    main()
