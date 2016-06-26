# gitcloner

Clone all repos of a user or organization with this command line python script.

## Usage

```gitcloner [-h] [-u | -o] [-c | -p] name```

### `options`:
- `-u` or `--user` [For user account] [DEFAULT]
- `-o` or `--org` [For organization]
- `-c` or `--clone` [For cloning to `name`] [DEFAULT]
- `-p` or `--pull` [Update Existing Repos in `name`]
- `-h` or `--help` [Help]

### `name`:
- name of the user or organization. eg. shakib609, google etc.

## Example

- Clone all repos from my account
```sh
gitcloner shakib609
```

- Clone all repos from Google
```sh
gitcloner -o google
```

- Clone from my account and pull updates
```sh
gitcloner shakib609
gitcloner -p shakib609
```

## Installation

Install using setup.py file provided
```sh
git clone https://github.com/shakib609/gitcloner.git && cd gitcloner
[sudo] python3 setup.py install
```

## Requirements

- `git`
- `python3`
