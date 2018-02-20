import os

from setuptools import setup

package_name = "brochure"
current_directory_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(current_directory_path, package_name, 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(name=package_name,
      description="Show basic information about an enterprise to potential clients.",
      version=version,
      include_package_data=True,
      test_suite="tests",
      packages=[
          package_name,
          "{}.commands".format(package_name),
          "{}.value_fetchers".format(package_name),
          "{}.values".format(package_name),
          "{}_contract_tests".format(package_name),
          "{}_reference_implementations".format(package_name),
      ],
      author="Green Light Software, LLC",
      author_email="admin@greenlight.software",
      license="MIT",
      url="https://github.com/GreenLightSoftware/{}".format(package_name))
