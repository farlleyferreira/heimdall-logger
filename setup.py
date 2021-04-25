from setuptools import find_packages, setup

setup(
    name='heimdall-logger',
    packages=find_packages(),
    version='0.1.0',
    description='Asynchronous logging lib',
    long_description='',
    author='Farlley Ferreira',
    author_email='farlley@live.com',
    url='https://github.com/giovannifarlley/heimdall-logger',
    install_requires=['aiofiles', 'aiohttp'],
    license='MIT',
    keywords=['dev', 'log', 'async', 'aiologger', ''],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)