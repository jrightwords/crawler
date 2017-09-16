from setuptools import setup, find_packages

setup (
    name = "crawler",
    version = "1.0",
    description = "Web crawler only for 2 sites and variable search-depth",
    
    packages=find_packages(),
    install_requires=['BeautifulSoup'],
)
