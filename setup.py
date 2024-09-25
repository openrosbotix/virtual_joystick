import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'virtual_joystick'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Patrick Weber',
    maintainer_email='paddy-daun@web.de',
    description='Qt based virtual joystick control',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vjoy_node = virtual_joystick.main:main'
        ],
    },
)
