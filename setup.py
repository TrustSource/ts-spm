from setuptools import setup

setup(
    name='ecs-spm-plugin',

    packages=['ecs_spm_plugin'],

    version='0.1.1',

    description='Swift package manager for TrustSource (open source code compliance)',

    author='EACG GmbH',

    license='MIT',

    url='https://github.com/eacg-gmbh/ecs-spm-plugin.git',

    download_url='',

    keywords=['scanning', 'dependencies', 'modules', 'ECS', 'Swift', 'TrustSource'],

    classifiers=[],

    install_requires=['ecs-python-client'],

    dependency_links=[
        'git+https://github.com/eacg-gmbh/ecs-python-client.git#egg=ecs-python-client-0.1.1'
    ],

    scripts=['ecs-spm-plugin'],

    entry_points={
        'console_scripts': ['ecs-spm-plugin=ecs_spm_plugin.cli:main'],
    }
)