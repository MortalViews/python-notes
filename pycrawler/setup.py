from setuptools import setup, find_packages
setup(
    name='pycrawler',
    version='1.0.1',
    description=('A simple python cralwer'),
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    install_requires=['beautifulsoup4','SQLAlchemy'],
    entry_points={
            'console_scripts':['pycrawler=pycrawler.bin.cli:main']
            },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
