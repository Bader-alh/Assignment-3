import setuptools 

with open('README.md', 'r') as f: 
    long_description = f.read() 
setuptools.setup( 
    name='naive_bayes', #there werent quotations but naive bayes is string, nor variable like in instruct version
    version='0.0.1', 
    author='Bader Alhodithi', 
    author_email='Ba783@georgetown.edu', 
    description='Naive Bayes text classification', 
    long_description=long_description, 
    long_description_content_type='text/markdown', 
    packages=setuptools.find_packages(), 
    python_requires='>=3.6', 
    extras_requre={"dev": ["pytest", "flake8", "autopep8"]}, #i think should be require without the s (error with it)
) 