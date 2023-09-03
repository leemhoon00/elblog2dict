from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text(encoding='utf-8')

setup(
    name='elblog2dict',
    version='1.0.1',
    description='Utility for parsing and extracting data from ELB logs',
    author='leemhoon00',
    author_email='leemhoon000@gmail.com',
    url='https://github.com/leemhoon00/elblog2dict',
    install_requires=[],
    packages=find_packages(exclude=['.git', '.gitignore', '*.gz', 'test.py']),
    keywords=['elb', 'log', 'parser', 'elblog2dict', 'regular expression'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown'
)