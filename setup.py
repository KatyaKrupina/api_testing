import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='api_testing',
    platforms='macos',
    version='0.0.1',
    author='krupina',
    author_email='katya.palikus@gmail.com',
    description='test package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/KatyaKrupina/api_testing',
    packages=['api_testing'],
    keywords='sample tests',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    zip_safe=False,
    python_requires='>3.5',
    install_requires=[
        'jsonschema==3.2.0',
        'requests==2.24.0',
        'pytest==5.4.1'
    ]
)
