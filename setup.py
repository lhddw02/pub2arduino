from setuptools import find_packages, setup

package_name = 'pub2arduino_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi4bjazzy',
    maintainer_email='lhddw02@gmail.com',
    description='Serial Communication Test between Arduino and Pi ROS',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sender = pub2arduino_py.pub_func:main', 
            'receiver = pub2arduino_py.sub_func:main', 
        ],
    },
)
