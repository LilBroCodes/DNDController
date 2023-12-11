from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = "DND Controller library using pygame"
LONG_DESCRIPTION = "Library using pygame that lets you create custom dnd campaigns, with custom Character classes. "

setup(
    name="dnd_controller",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="LilBroCodes",
    author_email="lilbrocodes@gmail.com",
    packages=find_packages(),
    install_requires=["pygame"],
    keywords=["DND", "Pygame", "Game controller"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
