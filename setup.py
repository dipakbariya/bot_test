from setuptools import setup, find_packages

setup(
    name="dipakbariya_timechecker",
    version="0.0.1",
    author="Edipakbariya308",
    author_email="dipakbariya308@gmail.com",
    url="https://bit.ly/edeediong-resume",
    description="An application that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["timechecker = src.main:main"]},
)