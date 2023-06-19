from setuptools import setup, find_packages

setup(
    name='elblog2dict',
    version='0.0.2',
    description='temp',
    author='leemhoon00',
    author_email='leemhoon000@gmail.com',
    url='',
    install_requires=[],
    packages=find_packages(exclude=['.git', '.gitignore', '*.gz', 'test.py']),
    keywords=['elb'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license='MIT'
)