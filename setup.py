from setuptools import setup, find_packages

setup(
    name='ipayroll_sdk',
    packages=find_packages(),
    version='0.0.1',
    description='',
    author='Adrien',
    author_email='adrien@ipayroll.co.nz',
    url='',
    download_url='',
    keywords=['ipayroll', 'rest', 'client', 'pypi', 'package'],  # arbitrary keywords
    install_requires=[
        'requests_oauthlib',
        'booby',
        'requests==2.8.0'
    ],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    )
    # ,
    # entry_points={
    #     'console_scripts': [
    #         # 'hello_world = package_archetype.hello_world:print_hello_world'
    #     ]},
)
