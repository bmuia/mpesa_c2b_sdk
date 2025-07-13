from setuptools import setup, find_packages

setup(
    name='mpesa_c2b_sdk',              
    version='0.1.1',                          
    description='A Python SDK for Safaricom Daraja C2B APIs', 
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',
    author='Belam Muia',
    author_email='belammuia0@gmail.com',
    url='https://github.com/bmuia/mpesa_c2b_sdk.git',
    packages=find_packages(),                
    install_requires=[
        'requests>=2.20.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
