import setuptools
import ruslat

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="ruslat",
    version=ruslat.__version__,
    author=ruslat.__author__,
    description="Python converter for Russian Latin Alphabet",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ZetaFactorial/ruslat",
    license="MIT",
    keywords='transliteration romanization cyrillic latin russian',
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        'Natural Language :: Russian',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        'Topic :: Text Processing :: Linguistic',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        'Source': 'https://github.com/ZetaFactorial/ruslat',
        'Tracker': 'https://github.com/ZetaFactorial/ruslat/issues',
    },
    entry_points = {
        'console_scripts': [
            'ruslat=ruslat.command_line:main'
        ],
    }
)
