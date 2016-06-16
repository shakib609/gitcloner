from distutils.core import setup

files = ['gitaccounthelpers/*']

setup(
    name='gitcloner',
    version='1.0',
    description='Clone all git repos',
    author='Shakib Hossain',
    author_email='shakib609@hotmail.com',
    url='https://github.com/shakib609/gitcloner',
    packages=['gitaccount'],
    package_data={'gitaccount': files},
    scripts=['gitcloner'],
    long_description='''Use this script to clone all the public git repos of any
user or organization of Github'''
)
