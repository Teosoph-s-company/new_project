from setuptools import setup, find_packages

setup(
    name="personal_assistent",
    version="1.0.0",
    author="Teosoph's company (Teosoph, Tatsiana, Violet)",
    email="teosoph@hotmail.com, tt1846641@gmail.com, violettalozova@gmail.com",
    entry_points={
        "console_scripts": [
            "event_agency=personal_assistent.new_project:main",
            "mytest=personal_assistent.test:main",
        ]
    },
    packages=find_packages(),
    include_package_data=True,
    description="This script is intelligence bot assistent for the event's agency",
    license="MIT License",
)
