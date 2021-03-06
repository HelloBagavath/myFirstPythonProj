from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

    setup(
        name="myfirstpythonproj",
        version="0.0.2",
        author="Bagavath singh  ",
        author_email="s.bagavath@gmail.com",
        description="Who knows what it does?? !!",
        long_description=readme,
        long_description_content_type="text/markdown",
        url="https://github.com/your_package/homepage/",
        packages=find_packages(),
        install_requires=requirements,
        classifiers=[
            "Programming Language :: Python :: 3.6",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
