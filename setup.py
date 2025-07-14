from setuptools import setup, find_packages

setup(
    name='arcus-python-client',
    version='1.0.2', # version updated
    packages=find_packages(),
    description='Arcus python client forked to be installable via pip.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/brido4125/arcus-python-client',
    author='brido4125',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    keywords='arcus cache client',
)
