"""Setup for the ShipRocket Python Client App."""
from setuptools import setup

install_requires = [
    'django>=1.11.20',
    'django-admin-list-filter-dropdown==1.0.2',
]

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-django',
    'coverage',
]


setup(
    name='shiprocket-python-client',
    version='1.0.0',
    description='ShipRocket Python Client',
    author='Ankit Kumar',
    author_email='ankitkhadria1@gmail.com',
    url='https://github.com/ankitkhadria1/shiprocket-python-client',
    packages=['shiprocket'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Topic :: Security :: Cryptography",
        "Topic :: Communications",
    ],
    install_requires=install_requires,
    extras_require={
        'testing': tests_require
    },
)
