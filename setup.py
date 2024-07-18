from setuptools import setup, find_packages

setup(
    name='winutils',
    version='0.1',
    packages=find_packages(),
    author='SelfCode',
    author_email='https://t.me/selfcode_dev',
    description='Утилиты для работы с Windows',
    url='https://github.com/SelfC0de/winutils',
    install_requires=[
        'psutil'
    ]
)
