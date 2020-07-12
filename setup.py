import setuptools

setuptools.setup(
    name="xNIU",
    version="0.1.0",
    description="Interface for NIU (小牛电动车) API",
    author="Maxime Pagnoulle (马驰)",
    author_email="me@maxpag.eu",
    url="https://github.com/MaxPag/xNIU",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
)
