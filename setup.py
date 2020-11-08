import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Warhammer-Shooting-Sim-Public-Alpha-JoeyTubesocks", # Replace with your own username
    version="0.1.0",
    author="Dan 'Joey Tubesocks' Clements",
    author_email="JoeyTubesocks@gmail.com",
    description="A shooting simulator for Warhammer 40k",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/radmojo/40kShootingSim",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
