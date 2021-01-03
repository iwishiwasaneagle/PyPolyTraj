import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypolytraj",
    version="0.1",
    author="Jan-Hendrik Ewers",
    author_email="jh.ewers@gmail.com",
    description="Polynomial Trajectory Generation",
    long_description="A package for Polynomial Trajectory Generation (quintic, multi-bounded, etc.)",
    long_description_content_type="text/markdown",
    url="https://github.com/iwishiwasaneagle/pypolytraj",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)