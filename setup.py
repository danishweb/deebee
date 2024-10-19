from setuptools import setup, find_packages

setup(
    name='deebee',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'deebee = deebee.__main__:main', 
        ],
    },
    install_requires=['Flask'],
)

