from setuptools import setup, find_packages

def get_long_description():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

setup(
    name="mintlemon-turkish-nlp",
    version = "0.2.5",
    description="Mint & Lemon Turkish NLP Library developed by Mint & Lemon Development Team.",
    author="Mint&Lemon",
    license="Apache License, Version 2.0",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Teknofest-Nane-Limon/mintlemon-turkish-nlp",
    project_urls={
        "Tracker": "https://github.com/Teknofest-Nane-Limon/mintlemon-turkish-nlp/issues",
        "Documentation": "https://mintlemon-turkish-nlp.readthedocs.io",
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    packages=find_packages(),
    package_data={"mintlemon": ["data/*"]},
    include_package_data=True,
    install_requires=[
        "numpy>=1.20.0",    
        "regex>=2021.4.4",    
        "zeyrek>=0.1.3",    
        "nltk>=3.8.1",    
        "pandas>=1.3.4",    
        "scikit-learn>=1.2.0",
    ],
    extras_require={"dev": ["yapf", "bumpver", "flake8", "coverage", "pytest"]},
)
