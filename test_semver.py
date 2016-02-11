import unittest

from semver import Version, valid

INVALID_VERSIONS = ['1.2.3.4', '1', None]
VALID_VERSIONS = {
        '1.2.3'             : (1, 2, 3),
        '4.11.6'            : (4, 11, 6),
        '4.2.0'             : (4, 2, 0),
        '1.5.19'            : (1, 5, 19),
        '2.0.11-alpha'      : (2, 0, 11),
        '0.1.7+amd64'       : (0, 1, 7),
        '0.10.7+20141005'   : (0, 10, 7),
        '2.0.12+i386'       : (2, 0, 12),
        '20.1.1+i386'       : (20, 1, 1),
        '0.1.2-rc1.3.4'     : (0, 1, 2)}

EQUALITY_COMPS = [
        ('1.2.3', '1.2.3', '=='),
        ('1.2.3', '1.2.4', '!='),
        ('0.10.7+20141005', '2.0.12+i386', '!='),
        ('2.0.12+i386', '2.0.12+i386', '==')
]

SATISFIES = {
        '==1.2.3': [ '1.2.3-rc1', '1.2.3-rc1.3.4'],
        '!=1.2.3': ['0.1.3+1', '1.2.4', '1.4.6+build4.5'],
        '<1.2.3': [ '1.2.2', '1.2.2-rc1', '0.1.2-rc1.3.4', '0.1.2+build4'],
        '<=1.2.3': [ '1.2.3', '1.2.2', '1.2.2-rc1', '0.1.2-rc1.3.4', '0.1.2+build4'],
        '>1.2.3': [ '1.2.4', '1.2.4-rc1', '2.3.4-rc1.3.4', '10.1.2+build4'],
        '>=1.2.3': [ '1.2.3', '1.2.4', '1.2.4-rc1', '2.3.4-rc1.3.4', '10.1.2+build4'],
        '~>1.2.3': ['1.2.4', '1.2.9-rc4'],
        '~>1.2': ['1.2.5', '1.4.6+build4.5', '1.10.100']
}

class VersionTest(unittest.TestCase):

    def test_successful_parse(self):
        for version, result in VALID_VERSIONS.items():
            self.assertTupleEqual(Version.parse(version), result, "{} should be equal to {}.".format(version, result))

    def test_parse_should_return_tuple(self):
        for version, result in VALID_VERSIONS.items():
            self.assertIsInstance(Version.parse(version), tuple, "{} should be a tuple type.".format(version))

    def test_parse_tuple_should_contain_ints(self):
        for version in VALID_VERSIONS.keys():
            for i in Version.parse(version):
                self.assertIsInstance(i, int, "{} in {} should be in integer.".format(i, version))

    def test_failed_parse(self):
        for version in INVALID_VERSIONS:
            self.assertRaises(ValueError, Version.parse, version)

    def test_invalid_versions(self):
        for version in INVALID_VERSIONS:
            self.assertFalse(valid(version), "{} should NOT be a valid version.".format(version))

    def test_valid_versions(self):
        for version in VALID_VERSIONS.keys():
            self.assertTrue(valid(version), "{} should be a valid version".format(version))

    def test_equal(self):
        for v in EQUALITY_COMPS:
            version1 = Version(v[0])
            version2 = Version(v[1])
            if v[2] == '==':
                self.assertTrue(version1 == version2, "{} should be equal to {}.".format(version1, version2))
            else:
                self.assertFalse(version1 == version2, "{} should NOT be equal to {}.".format(version1, version2))

    def test_not_equal(self):
        for v in EQUALITY_COMPS:
            version1 = Version(v[0])
            version2 = Version(v[1])
            if v[2] == '!=':
                self.assertTrue(version1 != version2, "{} should be equal to {}.".format(version1, version2))
            else:
                self.assertFalse(version1 != version2, "{} should NOT be equal to {}.".format(version1, version2))

    def test_greater_than(self):
        self.assertTrue(Version('1.2.4') > Version('1.2.3'))
        self.assertTrue(Version('3.10.7+20141005') > Version('2.0.12+i386'))

        self.assertFalse(Version('2.3.4') > Version('3.2.1'))
        self.assertFalse(Version('2.10.7+20141005') > Version('3.0.12+i386'))

    def test_greater_than_or_equals(self):
        self.assertTrue(Version('1.2.3') >= Version('1.2.3'))
        self.assertTrue(Version('3.10.7+20141005') >= Version('2.0.12+i386'))

        self.assertFalse(Version('1.2.3') >= Version('11.2.3'))
        self.assertFalse(Version('2.10.7+20141005') > Version('3.0.12+i386'))

    def test_less_than(self):
        self.assertTrue(Version('1.2.3') < Version('1.2.4'))
        self.assertTrue(Version('2.0.12+i386') < Version('3.10.7+20141005'))

        self.assertFalse(Version('3.2.1') < Version('2.2.4'))
        self.assertFalse(Version('3.0.12+i386') < Version('1.10.7+20141005'))

    def test_less_than_or_equals(self):
        self.assertTrue(Version('1.2.3') <= Version('1.2.3'))
        self.assertTrue(Version('2.0.12+i386') <= Version('3.10.7+20141005'))

        self.assertFalse(Version('3.2.1') <= Version('2.2.4'))
        self.assertFalse(Version('3.0.12+i386') <= Version('2.10.7+20141005'))

    def test_pessimistic(self):
        for requirement, version_list in SATISFIES.items():
            for v in version_list:
                self.assertTrue(Version(v).satisfies(requirement), "{} should satify {} requirement.".format(v, requirement))

if __name__ == '__main__':
    unittest.main()
