from setuptools import setup, find_packages
setup(
    name='django-contact',
    version=__import__('contact').get_version(limit=3),
    description='A Django application to handle contact form',
    author='Guillaume Esquevin',
    author_email='guillaume.esquevin@platypus-creation.com',
    url='http://code.google.com/p/django-contact/',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools']
)
