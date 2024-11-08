# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from setuptools import setup, find_packages

setup(
    name='task_manager',  # Name of your project
    version='0.1.0',  # Initial version
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[  # List of dependencies
        'pytest==8.3.3',  # Testing framework
        'behave==1.2.6'  # Behavior-driven development framework
    ],
    entry_points={  # Entry points for command line scripts
        'console_scripts': [
            'task-manager=task_manager.cli:main',  # Adjust according to your CLI entry point
        ],
    },
    author='Your Name',  # Your name
    author_email='your.email@example.com',  # Your email
    description='A task manager application',  # Short description of your project
    long_description=open('README.md').read(),  # Long description from README file
    long_description_content_type='text/markdown',  # Format of the long description
    url='https://github.com/MoisesGzz92/TaskManager_SW-testing',  # URL to your project repository
    classifiers=[  # Classifiers for the project
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
