# gitcloner

Clone all repos of a user or organization with this command line python script.

## Usage

```gitcloner [-h] [-u | -o] name```

Valid OPTIONS:
- `-u` [For user account] [DEFAULT]
- `-o` [For organization]
- `-h` [Help]

`name`:
- name of the user or organization. eg. shakib609, google etc.

## Example

- Clone all repos from my account
```
gitcloner shakib609
```

- Clone all repos from Google
```
gitcloner -o google
```

## Installation

Install using setup.py file provided
```sh
git clone https://github.com/shakib609/gitcloner.git
[sudo] python3 setup.py install
```

## Requirements

- `git`
- `python3`
