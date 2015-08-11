from setuptools import setup, find_packages

requires = [
    ]

test_requires = [
    'mock',
    'nose',
    'coverage'
    ]

setup(name='python-unittest-skeleton',
      version='0.01',
      description='Example project skeleton',
      long_description='',
      classifiers=[
          "Programming Language :: Python",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.4"
          ],
      author='',
      author_email='',
      url='',
      keywords='unittest tox nose coverage',
      packages=find_packages(),
      zip_safe=False,
      test_suite='tests',
      install_requires=requires,
      extras_require={'testing': test_requires},
      )
