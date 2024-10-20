from setuptools import setup, find_packages

setup(
    name='deebee',
    version='0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'deebee = deebee.__main__:main', 
        ],
    },
    install_requires=[
        'Flask>=2.0.0', 
        'argparse',
    ],
    extras_require={
        'dev': ['pytest', 'black'],
    },
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
