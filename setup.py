from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="wi-mote",
    version="1.0.0",
    description="Remote over Wifi!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Anujit Bahuleyan",
    author_email="anujithbahuleyan@gmail.com",
    url="https://github.com/JimboKearn/wi-mote",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
        "pyautogui",
        "qrcode-terminal",
        "pyalsaaudio"
    ],
    entry_points={
        "console_scripts": [
            "wi-mote=wi_mote.cli:main"
        ]
    }
)
