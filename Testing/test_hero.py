from hero.project.hero import Hero
import unittest

class HeroTests(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Slavi",10, 10.0,1.0)

    def test_hero_initialized(self):
        self.assertEqual ( self.hero.username, "Slavi" )
        self.assertEqual ( self.hero.level, 10 )
        self.assertEqual ( self.hero.health, 10.0 )
        self.assertEqual ( self.hero.damage, 1.0 )

    def test_battle_with_same_hero(self):
        enemy_hero=Hero("Slavi",5, 5.0,2.0)
        with self.assertRaises ( Exception ) as exp:
            self.hero.battle(enemy_hero)
        self.assertEqual ( exp.exception.args[0], 'You cannot fight yourself' )

    def test_hero_healt_below_zero(self):
        enemy_hero = Hero ( "Chochko", 5, 5.0, 2.0 )
        self.hero.health = 0
        self.assertRaises ( ValueError, self.hero.battle, enemy_hero )

    def test_enemy_hero_healt_below_zero(self):
        enemy_hero = Hero ( "Chochko", 5, 0, 2.0 )
        self.assertRaises ( ValueError, self.hero.battle, enemy_hero )

    def test_player_damage(self):
        player_damage = self.hero.damage * self.hero.level
        self.assertEqual ( player_damage, 10 )

    def test_enemy_hero_health(self):
        enemy_hero = Hero ( "Chochko", 5, 50.0, 2.0 )
        player_damage = self.hero.damage * self.hero.level
        self.assertEqual ( enemy_hero.health-player_damage, 40.0 )

    def test_healts_below_zero(self):
        enemy_hero = Hero ( "Chochko", 10, 10.0,1.0 )
        res=(self.hero.battle(enemy_hero))
        self.assertEqual (res , "Draw")

    def test_hero_win(self):
        enemy_hero = Hero ( "Chochko", 1, 1.0,1.0 )
        res = (self.hero.battle ( enemy_hero ))
        self.assertEqual ( res, "You win" )
        self.assertEqual ( self.hero.level, 11 )
        self.assertEqual ( self.hero.health, 14.0 )
        self.assertEqual ( self.hero.damage, 6.0 )

    def test_hero_lost(self):
        enemy_hero = Hero ( "Chochko", 100, 100.0,10.0 )
        res = (self.hero.battle ( enemy_hero ))
        self.assertEqual ( res, "You lose" )
        self.assertEqual ( enemy_hero.level, 101 )
        self.assertEqual ( enemy_hero.health, 95.0 )
        self.assertEqual ( enemy_hero.damage, 15.0 )

    def test_str_vehicle(self):
        self.assertEqual ( self.hero.__str__(), "Hero Slavi: 10 lvl\nHealth: 10.0\nDamage: 1.0\n" )

if __name__ == "__main__":
    unittest.main ()
