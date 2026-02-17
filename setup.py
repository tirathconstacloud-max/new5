from setuptools import setup, find_packages

# Note: 'version' ko hooks.py ke app_version se match hona chahiye
with open("my_universal_auth/hooks.py", "r") as f:
    for line in f:
        if "app_version" in line:
            version = line.split("=")[1].strip().replace('"', "").replace("'", "")
            break

setup(
    name="my_universal_auth",
    version=version,
    description="Universal OAuth for Multiple Sites",
    author="Your Name",
    author_email="yash@yopmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
)