from setuptools import setup,find_packages

setup(
    name = 'hijack_checker',
    version = '0.1',
    packages=find_packages(),
    author = 'Haystack',
    author_email = 'haystackinfosec@gmail.com',
    description = ("A simple library (and command line utility) for checking "
                   "to see if a subdomain is vulnerable to hijacking."),
    license = "Beerware",
    install_requires=[
        'dnspython3',
        'docopt'
    ],
    scripts = [
        "bin/hijack-checker",
    ]
)
