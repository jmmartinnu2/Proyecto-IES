from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='package_name',
    version='0.0.1',
    author='Your Name',
    author_email='youremail@example.com',
    description='A brief description of your project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yourusername/package_name',
    packages=find_packages(),
    install_requires=["fastapi", "sqlalchemy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
