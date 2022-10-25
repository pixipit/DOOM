from Custum_Components.EnemyManager import Wave, Level
from enemy_etalons import EnemyEtalons
from game import Game


class LevelHolder:
    @staticmethod
    def get_levels():
        return [LevelHolder.lvl1(), LevelHolder.lvl2(),
                LevelHolder.lvl3(), LevelHolder.lvl4()]

    @staticmethod
    def lvl1():
        enemies = EnemyEtalons(Game.game.speed, Game.game.speed).enemies
        wave_boss = Wave([[enemies["Zdenda"], 1]])
        wave1 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 0],
                      [enemies["Vondra"], 0], [enemies["Rasek"], 0],
                      [enemies["Herman"], 0], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 0],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 4],
                      ])
        wave2 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 0],
                      [enemies["Vondra"], 0], [enemies["Rasek"], 0],
                      [enemies["Herman"], 2], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 2],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 4],
                      ])
        wave3 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 0],
                      [enemies["Vondra"], 0], [enemies["Rasek"], 1],
                      [enemies["Herman"], 5], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 4], [enemies["Hrabalova"], 4],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 4],
                      ])
        wave4 = Wave([[enemies["Velich"], 5], [enemies["Jura"], 0],
                      [enemies["Vondra"], 0], [enemies["Rasek"], 5],
                      [enemies["Herman"], 2], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 2],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 4],
                      ])
        wave5 = Wave([[enemies["Velich"], 10], [enemies["Jura"], 0],
                      [enemies["Vondra"], 0], [enemies["Rasek"], 2],
                      [enemies["Herman"], 5], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 0],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 6],
                      ], [2.0, 4.0])
        return Level([wave1, wave2, wave3, wave4, wave_boss, wave5])

    @staticmethod
    def lvl2():
        enemies = EnemyEtalons(Game.game.speed, 1.5 * Game.game.speed).enemies

        wave_boss = Wave([[enemies["Klickova"], 1]])
        wave1 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 0],
                      [enemies["Vondra"], 4], [enemies["Rasek"], 0],
                      [enemies["Herman"], 0], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 0],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ])
        wave2 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 2],
                      [enemies["Vondra"], 4], [enemies["Rasek"], 2],
                      [enemies["Herman"], 2], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 2],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 10],
                      ])
        wave3 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 4],
                      [enemies["Vondra"], 4], [enemies["Rasek"], 1],
                      [enemies["Herman"], 2], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 4], [enemies["Hrabalova"], 4],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 10],
                      ])
        wave4 = Wave([[enemies["Velich"], 10], [enemies["Jura"], 2],
                      [enemies["Vondra"], 5], [enemies["Rasek"], 2],
                      [enemies["Herman"], 2], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 3],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 10],
                      ])
        wave5 = Wave([[enemies["Velich"], 10], [enemies["Jura"], 2],
                      [enemies["Vondra"], 10], [enemies["Rasek"], 2],
                      [enemies["Herman"], 5], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 0],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ], [2.0, 4.0])
        return Level([wave1, wave2, wave3, wave4, wave_boss, wave5])

    @staticmethod
    def lvl3():
        enemies = EnemyEtalons(Game.game.speed, 2 * Game.game.speed).enemies

        wave_boss = Wave([[enemies["Sykora"], 1]])
        wave1 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 2],
                      [enemies["Vondra"], 4], [enemies["Rasek"], 0],
                      [enemies["Herman"], 0], [enemies["Jedlicka"], 2],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 0],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ])
        wave2 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 4],
                      [enemies["Vondra"], 4], [enemies["Rasek"], 2],
                      [enemies["Herman"], 5], [enemies["Jedlicka"], 4],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 2],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ])
        wave3 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 8],
                      [enemies["Vondra"], 4], [enemies["Rasek"], 1],
                      [enemies["Herman"], 5], [enemies["Jedlicka"], 8],
                      [enemies["Velich2"], 4], [enemies["Hrabalova"], 4],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ])
        wave4 = Wave([[enemies["Velich"], 5], [enemies["Jura"], 10],
                      [enemies["Vondra"], 5], [enemies["Rasek"], 10],
                      [enemies["Herman"], 15], [enemies["Jedlicka"], 16],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 8],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ])
        wave5 = Wave([[enemies["Velich"], 10], [enemies["Jura"], 2],
                      [enemies["Vondra"], 10], [enemies["Rasek"], 2],
                      [enemies["Herman"], 5], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 0],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ], [2.0, 4.0])
        return Level([wave1, wave2, wave3, wave4, wave_boss, wave5])

    @staticmethod
    def lvl4():
        enemies = EnemyEtalons(Game.game.speed, 3 * Game.game.speed).enemies

        wave_boss = Wave([[enemies["budai"], 1]])
        wave1 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 2],
                      [enemies["Vondra"], 4], [enemies["Rasek"], 0],
                      [enemies["Herman"], 0], [enemies["Jedlicka"], 2],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 0],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ])
        wave2 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 4],
                      [enemies["Vondra"], 4], [enemies["Rasek"], 2],
                      [enemies["Herman"], 5], [enemies["Jedlicka"], 4],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 2],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ])
        wave3 = Wave([[enemies["Velich"], 4], [enemies["Jura"], 8],
                      [enemies["Vondra"], 4], [enemies["Rasek"], 1],
                      [enemies["Herman"], 5], [enemies["Jedlicka"], 8],
                      [enemies["Velich2"], 4], [enemies["Hrabalova"], 4],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ])
        wave4 = Wave([[enemies["Velich"], 5], [enemies["Jura"], 10],
                      [enemies["Vondra"], 5], [enemies["Rasek"], 10],
                      [enemies["Herman"], 15], [enemies["Jedlicka"], 16],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 8],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ])
        wave5 = Wave([[enemies["Velich"], 10], [enemies["Jura"], 2],
                      [enemies["Vondra"], 10], [enemies["Rasek"], 2],
                      [enemies["Herman"], 5], [enemies["Jedlicka"], 0],
                      [enemies["Velich2"], 5], [enemies["Hrabalova"], 0],
                      [enemies["Zdenda"], 0], [enemies["Sykora"], 0],
                      [enemies["Klickova"], 0], [enemies["Zelenka"], 0],
                      [enemies["Studenkova"], 0], [enemies["Lopocha"], 5],
                      ], [2.0, 4.0])
        return Level([wave1, wave2, wave3, wave4, wave_boss, wave5])
