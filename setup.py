from setuptools import setup

setup(
    name = "AitTools",
    version = "0.1.0",
    description = "All the packages of Aitzaz Imtiaz with multiple commands.",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/AitTools",
    packages = ["aitformation"],
    entry_points = {
        'console_scripts': [
            'aitformation = aitformation.__main__:main'
        ]
    },
)
