from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_test_walk(self):
        runner1 = Runner('Vladimir')
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_test_run(self):
        runner2 = Runner('Maxim')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_test_challenge(self):
        runner1 = Runner('Vladimir')
        runner2 = Runner('Maxim')
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()