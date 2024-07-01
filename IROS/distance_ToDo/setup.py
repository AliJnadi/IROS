from setuptools import find_packages, setup
# from glob import glob
# import os

package_name = 'distance'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ali',
    maintainer_email='a.jnadi@innopolis.university',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        # TODO: Add your nodes to console_scripte
        'console_scripts': [
            'pos_pub_node = ??',
            'cart_dis_node = ??',
            'res_disp_node = ??'
        ],
    },
)