from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='heimdall-logger',    
    version='0.1.1',
    description='Asynchronous logging lib',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    packages=find_packages(),
    python_requires=">=3.8"
)