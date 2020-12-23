import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Lord-Shiva", 
    version="0.1.8",
    author="Nethran Kumarasamy",
    author_email="ramanathank18@gmail.com",
    description="IT is the package.educational purpose",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nethra-coding/lord_shiva",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
