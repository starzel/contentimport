from setuptools import setup

setup(
    name='contentimport',
    version='0.1',
    description='Custom import based on collective.exportimport',
    url='https://github.com/starzel/contentimport',
    author='Philip Bauer',
    author_email='bauer@starzel.de',
    license='GPL version 2',
    packages=['contentimport'],
    include_package_data=True,
    zip_safe=False,
    entry_points={'z3c.autoinclude.plugin': ['target = plone']},
    install_requires=[
        "setuptools",
        "collective.exportimport",
        "beautifulsoup4",
        ],
    )
