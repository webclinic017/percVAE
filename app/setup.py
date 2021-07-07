import os
from setuptools import setup, find_packages

# load the README file and use it as the long_description for PyPI
with open('README.md', 'r') as f:
    readme = f.read()


def get_fucking_package_data(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

setup_path = os.path.realpath(__file__)
dir_path = os.path.join(os.path.dirname(setup_path), "fennekservice")

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
    name="fennekservice",
    description="The Fennek AI backend service",
    long_description=readme,
    long_description_content_type='text/markdown',
    version="0.1",
    author="Clemens,Emre,Fennek Fox",
    author_email="emre@fennek-ai.com",
    url="www.fennek-ai.com",
    packages=find_packages(),
    package_data={'': get_fucking_package_data(dir_path)}, # {'fennekservice': ['*.gin', 'models/samplevae/*', 'models/samplevae/clap_model/*', 'static/*']},
    include_package_data=True,
    python_requires=">=3.7.*",
    install_requires=['numpy', 'requests'],
    license="None / Proprietary",
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='package development template'
)
