from parser import suite
import unittest

class Dog:
    def run(self):
        return "running"
    
    def eat(self):
        return "eating"


class TestDogMethods(unittest.TestCase):
    dog = Dog()

    def test_run(self):
        self.assertEqual(self.dog.run(), 'running')
    
    def test_eat(self):
        self.assertEqual(self.dog.eat(), 'eating')



if __name__ == '__main__':
    unittest.main()

   