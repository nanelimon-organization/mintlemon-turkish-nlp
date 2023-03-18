from setuptools import setup, find_packages

setup(
    name="mintlemon-turkish-nlp",
    version = "0.1.18",
    description="Mint & Lemon Turkish NLP Library developed by Mint & Lemon Development Team.",
    author="Mint&Lemon",
    license="Apache License, Version 2.0",
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
    install_requires=["numpy>=1.20.0", "regex>=2021.4.4"],
    extras_require={"dev": ["yapf", "bumpver", "flake8", "coverage", "pytest"]},
)