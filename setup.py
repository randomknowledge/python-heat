# coding=utf-8
from setuptools import setup


setup(
    name="python-heat",
    author="Florian Finke",
    author_email="flo@randomknowledge.org",
    version='0.0.1',
    packages=['heatmap'],
    package_data={'heatmap': ['data/**/*']},
    url='https://github.com/randomknowledge/python-heat',
    include_package_data=True,
    license='MIT',
    description='A simple heatmap generator',
    long_description=open('Readme.md').read(),
    zip_safe=False,
    install_requires=[
        'PIL==1.1.7',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
