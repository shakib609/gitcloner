# gitcloner
Clone all repos of a user or organization with this command line python script.

# Usage
```./gitcloner.py [-u | -o] [NAME]```

Valid OPTIONS:
- `-u` [For user account] [DEFAULT]
- `-o` [For organization]

NAME:
- name of the user or organization. eg. shakib609, google etc.

# Example
- Clone all repos from my account
```
./gitcloner.py shakib609
```
- Clone all repos from Google
```
./gitcloner.py -o google
```

# Requirements
The only requirement of this script is *python3*. All modules used in the script are available in the Python Standard Library.
