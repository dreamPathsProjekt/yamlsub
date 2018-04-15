from setuptools import setup, find_packages

setup(
    name="yamlsub",
    version="0.1",
    packages=find_packages(),


    install_requires=[
        "yaml"
    ],

    # package_data={
    #     # If any package contains *.txt or *.rst files, include them:
    #     '': ['*.txt', '*.rst'],
    #     # And include any *.msg files found in the 'hello' package, too:
    #     'hello': ['*.msg'],
    # },

    # metadata for upload to PyPI
    author="Ioannis Dritsas",
    author_email="dream.paths.projekt@gmail.com",
    description="Easily substitute values in .yaml files",
    license="MIT",
    keywords="",
    # url="http://example.com/HelloWorld/",
)
