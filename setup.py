from setuptools import setup, find_packages

setup(
    name='example_package_mimis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here, e.g.,
        # 'some_package>=1.0.4',
    ],
    author='Your Name',  # Add your name
    author_email='your.email@example.com',  # Add your email
    description='A description of your package',  # Add a short description
    url='https://github.com/username/repository',  # Add the URL of your repository
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
