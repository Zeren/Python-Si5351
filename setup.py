from setuptools import setup

setup(
    name='Python-Si5351',
    version='0.1.0',
    packages=['Si5351'],
    url='https://github.com/Zeren/Python-Si5351',
    license='Creative Commons Zero v1.0 Universal',
    author='Jan Spacil',
    author_email='zeren.yuufana@gmail.com',
    description='Python library for Si5351',
    install_requires=['smbus2', 'numpy']
)
