from setuptools import setup, find_packages

setup(
    name='my-noren',  # Name of your new package
    version='0.1.0',  # Version of your new package
    packages=find_packages(),
    install_requires=[  # Dependencies if needed
        # 'dependency1',
        # 'dependency2',
    ],
    author='Abhishek',
    author_email='abhishek.gharat04@gmail.com',
    description='A modified version of the NorenRestApi package',
    url='https://github.com/builder35abhishek/my-noren.git',  # URL to your repository
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

