"""
Unit Tests for Encryption Utilities

This module contains unit tests for the password encryption utilities.
"""

import unittest
from encryption_utilities import passwordEncrypt

class TestEncryptionMethods(unittest.TestCase):
    """Test case for encryption methods."""

    def test_encrypt_password(self):
        """Test password encryption."""
        encryptedPassword = passwordEncrypt("XqffoZeo", 16)
        assert encryptedPassword == "NgvvePue"

    def test_decrypt_password(self):
        """Test password decryption (using negative key)."""
        encryptedPassword = passwordEncrypt("NgvvePue", -16)
        assert encryptedPassword == "XqffoZeo"


if __name__ == "__main__":
    unittest.main()
