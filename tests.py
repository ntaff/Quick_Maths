from Python.Primality import *
import unittest


class testPrimality(unittest.TestCase):

    """Tests cases utilisés pour tester les fonctions des challenges du chapitre 'Guest'."""

    def test_fermat_witness(self):
        """Test le fonctionnement de la fonction 'fermat_witness'."""
        self.assertEqual(fermat_witness(), )
        
    def test_test_miller_rabin(self):
        """Test le fonctionnement de la fonction 'miller_rabin'."""
        self.assertEqual(miller_rabin(n,k), )
        
    def test_prime_in_range(self):
        """Test le fonctionnement de la fonction 'prime_in_range'."""
        self.assertEqual(prime_in_range(a,b), )
