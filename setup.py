from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='cs.editabletagline',
      version=version,
      description="A simple package providing a editable tagline for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone viewlet tagline',
      author='Lur Ibargutxi',
      author_email='libargutxi@codesyntax.com',
      url='http://github.com/codesyntax/cs.editabletagline',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
