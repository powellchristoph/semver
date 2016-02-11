"""Python library that will compare two semantic version strings""" 

__author__ = "Chris Powell <powellchristoph@gmail.com>"
__version__ = "0.1.0"

import re

version_pattern = re.compile('^(\d+)\.(\d+)\.?(\d+)?(?:-([0-9a-zA-Z.-]+))?(?:\+([0-9a-zA-Z.-]+))?$', re.VERBOSE)
req_pattern = re.compile(r'^(<|<=|==|>=|>|!=|~>|!=)(\d.*)$')

class Version():
    def __init__(self, version):
        self.version = self.parse(version)
        self.major, self.minor, self.patch = self.version

    @classmethod
    def parse(cls, version):
        """Parses version defined by http://semver.org/"""
    
        if not version:
            raise ValueError("no version given")
    
        match = version_pattern.match(version)
        if not match:
            raise ValueError("invalid version {}".format(version))
    
        major, minor, patch = match.group(1, 2, 3)
        patch = 0 if not patch else patch
        return tuple(map(int, [major, minor, patch]))

    def satisfies(self, requirement):
        """Returns True if the version is satifies the requirement"""
        if not requirement:
            raise ValueError("no requirements given")

        match = req_pattern.match(requirement)
        if not match:
            raise ValueError("invalid requirement{}".format(version))

        operator, version = match.group(1, 2)
        parsed_version = self.parse(version)

        if operator == '==':
            return self.version == parsed_version
        elif operator == '>':
            return self.version > parsed_version
        elif operator == '>=':
            return self.version >= parsed_version
        elif operator == '<':
            return self.version < parsed_version
        elif operator == '<=':
            return self.version <= parsed_version
        elif operator == '!=':
            return self.version != parsed_version
        elif operator == '~>':
            if self.version < parsed_version:
                return False

            major, minor, patch = parsed_version

            if patch == 0:
                limit = (major + 1, 0, 0)
            else:
                limit = (major, minor + 1, 0)

            return (parsed_version < self.version < limit)
        else:
            raise ValueError("unknown operator {} in {}".format(operator, requirement))

    def __str__(self):
        return "{}.{}.{}".format(self.major, self.minor, self.patch)

    def __repr__(self):
        return "Version({})".format(str(self))

    def __eq__(self, other):
        return self.version == other.version

    def __gt__(self, other):
        return self.version > other.version

    def __ge__(self, other):
        return self.version >= other.version

    def __lt__(self, other):
        return self.version < other.version

    def __le__(self, other):
        return self.version <= other.version

    def __ne__(self, other):
        return self.version != other.version

    meets = satisfies

def valid(version):
    """Returns True if valid version."""
    try:
        Version.parse(version)
        return True
    except ValueError:
        return False
