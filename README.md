# gitcloner
Clone all repos of a user or organization with this command line python script.

## Usage
```./gitcloner.py [-u | -o] [NAME]```

Valid OPTIONS:
- `-u` [For user account] [DEFAULT]
- `-o` [For organization]

NAME:
- name of the user or organization. eg. shakib609, google etc.

## Example
- Clone all repos from my account
```
./gitcloner.py shakib609
```
- Clone all repos from Google
```
./gitcloner.py -o google
```

##Installation
- With `curl`
```
sudo curl -L https://github.com/shakib609/gitcloner/releases/download/1.0/gitcloner -o /usr/local/bin/gitcloner
sudo chmod a+rx /usr/local/bin/gitcloner
```
- With `wget`
```
sudo wget https://github.com/shakib609/gitcloner/releases/download/1.0/gitcloner -O /usr/local/bin/gitcloner
sudo chmod a+rx /usr/local/bin/gitcloner
```

# Requirements
- `git`
- `python3`
