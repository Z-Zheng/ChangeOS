from setuptools import find_packages, setup

install_requires = [
    'numpy',
    'Pillow',
    'scikit-image',
    'torch',
    'torchvision'
]
setup(
    name='changeos',
    version='0.2',
    description='ChangeOS SDK',
    keywords='Remote Sensing, '
             'Earth Vision, '
             'Deep Learning, '
             'Building Damage Assessment, '
             'Change Detection',
    packages=find_packages(exclude=[]),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
    url='https://github.com/Z-Zheng/ChangeOS',
    author='Zhuo Zheng',
    author_email='zhengzhuo@whu.edu.cn',
    license='',
    setup_requires=[],
    tests_require=[],
    install_requires=install_requires,
    zip_safe=False)
