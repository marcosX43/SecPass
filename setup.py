from setuptools import setup,find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='secpass',
    version='0.1.0',
    py_modules=['secpass'],
    install_requires= ["cryptography==43.0.1", "pytest==8.3.3", "typer==0.12.5", "typing_extensions==4.12.2"],
    packages=find_packages(),
    author='Anurag',
    author_email='kvanurag39@gmail.com',
    entry_points={
        'console_scripts': [
            'secpass=secpass.__main__:main',  # Command to execute your main() function
        ],
    }
)