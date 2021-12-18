import unittest
import main
import pygame


class MyTestCase(unittest.TestCase):
    def test_something(self):
        main.start_game()
        assert pygame.mixer.music.get_busy()

    def test_lose(self):
        main.hero.rect.topleft = 100, 450
        main.wall1.rect.topleft = 100, 450
        assert main.check_lose()

    def test_no_lose(self):
        main.hero.rect.topleft = 200, 450
        main.wall1.rect.topleft = 400, 450
        assert not main.check_lose()

    def test_speed(self):
        gr = grdelta = 20
        wa = wallspeed = 20
        score = 500
        grdelta, wallspeed = main.change_speed(score, grdelta, wallspeed)
        assert (gr != grdelta) and (wa != wallspeed)


if __name__ == '__main__':
    unittest.main()
