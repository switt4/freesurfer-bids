import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="freesurfer-bids",
    version="0.1.0",
    author="Ali Khan",
    author_email="alik@robarts.ca",
    description="Snakemake BIDS app for FS 7.1 recon-all, uses the snakebids package for running snakemake workflow as bids app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akhanf/freesurfer-bids",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={'console_scripts': [
        'freesurfer-bids=run:main'
    ]},
    install_requires=[
        "snakebids<=0.5",
        "SQLAlchemy<=0.9"
    ],
    python_requires='>=3.7'
)
