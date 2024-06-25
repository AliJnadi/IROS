from setuptools import find_packages, setup

package_name = 'Hello_world'

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
    maintainer='ali',
    maintainer_email='a.jnadi@innopolis.university',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'HW_pub_node = Hello_world.hello_world_pub:main',
            'HW_sub_node = Hello_world.hello_world_sub:main'
        ],
    },
)
