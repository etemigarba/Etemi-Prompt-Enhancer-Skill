#!/usr/bin/env python3
"""Setup script for etemi-prompt-enhancer (legacy support)."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="etemi-prompt-enhancer",
    version="1.0.0",
    author="Prof. Etemi Joshua Garba",
    author_email="joshua.garba@ethereal.ng",
    description="Transform rough prompts into production-ready six-part instructions with built-in validation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/etemigarba/etemi-prompt-enhancer",
    packages=find_packages(include=["scripts", "scripts.*"]),
    package_data={
        "": ["assets/*", "references/*", "examples/*"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "check-prompt=scripts.check_prompt:main",
        ],
    },
    project_urls={
        "Homepage": "https://github.com/etemigarba/etemi-prompt-enhancer",
        "Repository": "https://github.com/etemigarba/etemi-prompt-enhancer",
        "Issues": "https://github.com/etemigarba/etemi-prompt-enhancer/issues",
        "Documentation": "https://github.com/etemigarba/etemi-prompt-enhancer/wiki",
        "Changelog": "https://github.com/etemigarba/etemi-prompt-enhancer/blob/main/CHANGELOG.md",
    },
)