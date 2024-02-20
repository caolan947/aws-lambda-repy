from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'AWS Lambda repy description'
LONG_DESCRIPTION = 'AWS Lambda repy long description'

setup(
    name="repy",
    version=VERSION,
    author="caolan947 (Caolán Daly)",
    author_email="<caolan.day94@gmail.com>",
    description=DESCRIPTION,
     long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)