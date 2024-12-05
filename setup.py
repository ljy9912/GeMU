from setuptools import setup, find_packages

setup(
    name="GeMU",  # Package name
    version="0.0.3",  # Version number
    packages=find_packages(),  # Find all the packages
    install_requires=[],  # List of dependencies (if any)
    description="Activation function GeMU implemented based on PyTorch",  # Short description
    long_description=open('README.md').read(),  # Long description
    long_description_content_type="text/markdown",  # Format of README
    author="Jiayun Li",  # Author name
    author_email="lijiayun22@mails.tsinghua.edu.cn",  # Author email
    url="https://github.com/ljy9912/GeMU",  # URL to repo or documentation
    classifiers=[  # PyPI classifiers
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
