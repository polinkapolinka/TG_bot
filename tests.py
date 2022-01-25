import unittest
import aiogram
import datetime

import main as main


class BotTest(unittest.TestCase):

    def test_searc(self):
        self.assertEqual(("Cap", "Ter", "name"), main.searc([31, 12, 2021], "name"))
        self.assertEqual(("Sgr", "Ign", "name"), main.searc([1, 12, 2021], "name"))
        self.assertEqual(("Cap", "Ter", "Полина"), main.searc([1, 1, 2], "Полина"))
        self.assertEqual(("Cap", "Ter", "Кирилл"), main.searc([2, 1, 2], "Кирилл"))
        self.assertEqual(("Cap", "Ter", "Соня"), main.searc([3, 1, 2], "Соня"))
        self.assertEqual(("Cap", "Ter", "Полина"), main.searc([4, 1, 2], "Полина"))
        self.assertEqual(("Cap", "Ter", "Кирилл"), main.searc([5, 1, 2], "Кирилл"))
        self.assertEqual(("Cap", "Ter", "Рандомное Имя"), main.searc([6, 1, 2], "Рандомное Имя"))
        self.assertEqual(("Cap", "Ter", "Маша"), main.searc([7, 1, 2], "Маша"))
        self.assertEqual(("Cap", "Ter", "Кирилл"), main.searc([8, 1, 2], "Кирилл"))
        self.assertEqual(("Cap", "Ter", "Лиза"), main.searc([9, 1, 2], "Лиза"))
        self.assertEqual(("Cap", "Ter", "Кирилл"), main.searc([10, 1, 2], "Кирилл"))
        self.assertEqual(("Cap", "Ter", "Дима"), main.searc([11, 1, 2], "Дима"))
        self.assertEqual(("Cap", "Ter", "Соня"), main.searc([12, 1, 2], "Соня"))
        self.assertEqual(("Cap", "Ter", "Соня"), main.searc([13, 1, 2], "Соня"))
        self.assertEqual(("Cap", "Ter", "Полина"), main.searc([14, 1, 2], "Полина"))
        self.assertEqual(("Cap", "Ter", "Кирилл"), main.searc([15, 1, 2], "Кирилл"))
        self.assertEqual(("Cap", "Ter", "Рандомное Имя"), main.searc([16, 1, 2], "Рандомное Имя"))
        self.assertEqual(("Cap", "Ter", "Софья А"), main.searc([17, 1, 2], "Софья А"))
        self.assertEqual(("Cap", "Ter", "Рандомное Имя"), main.searc([18, 1, 2], "Рандомное Имя"))
        self.assertEqual(("Cap", "Ter", "Соня"), main.searc([19, 1, 2], "Соня"))
        self.assertEqual(("Cap", "Ter", "Соня"), main.searc([20, 1, 2], "Соня"))
        self.assertEqual(("Aqr", "Air", "Дима"), main.searc([21, 1, 2], "Дима"))
        self.assertEqual(("Aqr", "Air", "Дима"), main.searc([22, 1, 2], "Дима"))
        self.assertEqual(("Aqr", "Air", "Софья А"), main.searc([23, 1, 2], "Софья А"))
        self.assertEqual(("Aqr", "Air", "Маша"), main.searc([24, 1, 2], "Маша"))
        self.assertEqual(("Aqr", "Air", "Полина"), main.searc([25, 1, 2], "Полина"))
        self.assertEqual(("Aqr", "Air", "Лиза"), main.searc([26, 1, 2], "Лиза"))
        self.assertEqual(("Aqr", "Air", "Соня"), main.searc([27, 1, 2], "Соня"))
        self.assertEqual(("Aqr", "Air", "Маша"), main.searc([28, 1, 2], "Маша"))
        self.assertEqual(("Aqr", "Air", "Софья А"), main.searc([29, 1, 2], "Софья А"))
        self.assertEqual(("Aqr", "Air", "Полина"), main.searc([30, 1, 2], "Полина"))
        self.assertEqual(("Aqr", "Air", "Рандомное Имя"), main.searc([31, 1, 2], "Рандомное Имя"))
        self.assertEqual(("Aqr", "Air", "Кирилл"), main.searc([1, 2, 2], "Кирилл"))
        self.assertEqual(("Aqr", "Air", "Кирилл"), main.searc([2, 2, 2], "Кирилл"))
        self.assertEqual(("Aqr", "Air", "Полина"), main.searc([3, 2, 2], "Полина"))
        self.assertEqual(("Aqr", "Air", "Дима"), main.searc([4, 2, 2], "Дима"))
        self.assertEqual(("Aqr", "Air", "Полина"), main.searc([5, 2, 2], "Полина"))
        self.assertEqual(("Aqr", "Air", "Соня"), main.searc([6, 2, 2], "Соня"))
        self.assertEqual(("Aqr", "Air", "Лиза"), main.searc([7, 2, 2], "Лиза"))
        self.assertEqual(("Aqr", "Air", "Полина"), main.searc([8, 2, 2], "Полина"))
        self.assertEqual(("Aqr", "Air", "Соня"), main.searc([9, 2, 2], "Соня"))
        self.assertEqual(("Aqr", "Air", "Кирилл"), main.searc([10, 2, 2], "Кирилл"))
        self.assertEqual(("Aqr", "Air", "Полина"), main.searc([11, 2, 2], "Полина"))
        self.assertEqual(("Aqr", "Air", "Софья А"), main.searc([12, 2, 2], "Софья А"))
        self.assertEqual(("Aqr", "Air", "Лиза"), main.searc([13, 2, 2], "Лиза"))
        self.assertEqual(("Aqr", "Air", "Катя Скрицкая"), main.searc([14, 2, 2], "Катя Скрицкая"))
        self.assertEqual(("Aqr", "Air", "Рандомное Имя"), main.searc([15, 2, 2], "Рандомное Имя"))
        self.assertEqual(("Aqr", "Air", "Софья А"), main.searc([16, 2, 2], "Софья А"))
        self.assertEqual(("Aqr", "Air", "Кирилл"), main.searc([17, 2, 2], "Кирилл"))
        self.assertEqual(("Aqr", "Air", "Катя Скрицкая"), main.searc([18, 2, 2], "Катя Скрицкая"))
        self.assertEqual(("Aqr", "Air", "Рандомное Имя"), main.searc([19, 2, 2], "Рандомное Имя"))
        self.assertEqual(("Psc", "Aqu", "Катя Скрицкая"), main.searc([20, 2, 2], "Катя Скрицкая"))
        self.assertEqual(("Psc", "Aqu", "Полина"), main.searc([21, 2, 2], "Полина"))
        self.assertEqual(("Psc", "Aqu", "Софья А"), main.searc([22, 2, 2], "Софья А"))
        self.assertEqual(("Psc", "Aqu", "Рандомное Имя"), main.searc([23, 2, 2], "Рандомное Имя"))
        self.assertEqual(("Psc", "Aqu", "Софья А"), main.searc([24, 2, 2], "Софья А"))
        self.assertEqual(("Psc", "Aqu", "Лиза"), main.searc([25, 2, 2], "Лиза"))
        self.assertEqual(("Psc", "Aqu", "Полина"), main.searc([26, 2, 2], "Полина"))
        self.assertEqual(("Psc", "Aqu", "Кирилл"), main.searc([27, 2, 2], "Кирилл"))
        self.assertEqual(("Psc", "Aqu", "Соня"), main.searc([28, 2, 2], "Соня"))
        self.assertEqual(("Psc", "Aqu", "Дима"), main.searc([1, 3, 2], "Дима"))
        self.assertEqual(("Psc", "Aqu", "Софья А"), main.searc([2, 3, 2], "Софья А"))
        self.assertEqual(("Psc", "Aqu", "Катя Скрицкая"), main.searc([3, 3, 2], "Катя Скрицкая"))
        self.assertEqual(("Psc", "Aqu", "Софья А"), main.searc([4, 3, 2], "Софья А"))
        self.assertEqual(("Psc", "Aqu", "Полина"), main.searc([5, 3, 2], "Полина"))
        self.assertEqual(("Psc", "Aqu", "Полина"), main.searc([6, 3, 2], "Полина"))
        self.assertEqual(("Psc", "Aqu", "Полина"), main.searc([7, 3, 2], "Полина"))
        self.assertEqual(("Psc", "Aqu", "Софья А"), main.searc([8, 3, 2], "Софья А"))
        self.assertEqual(("Psc", "Aqu", "Полина"), main.searc([9, 3, 2], "Полина"))
        self.assertEqual(("Psc", "Aqu", "Маша"), main.searc([10, 3, 2], "Маша"))
        self.assertEqual(("Psc", "Aqu", "Лиза"), main.searc([11, 3, 2], "Лиза"))
        self.assertEqual(("Psc", "Aqu", "Катя Скрицкая"), main.searc([12, 3, 2], "Катя Скрицкая"))
        self.assertEqual(("Psc", "Aqu", "Полина"), main.searc([13, 3, 2], "Полина"))
        self.assertEqual(("Psc", "Aqu", "Софья А"), main.searc([14, 3, 2], "Софья А"))
        self.assertEqual(("Psc", "Aqu", "Маша"), main.searc([15, 3, 2], "Маша"))
        self.assertEqual(("Psc", "Aqu", "Соня"), main.searc([16, 3, 2], "Соня"))
        self.assertEqual(("Psc", "Aqu", "Дима"), main.searc([17, 3, 2], "Дима"))
        self.assertEqual(("Psc", "Aqu", "Катя Скрицкая"), main.searc([18, 3, 2], "Катя Скрицкая"))
        self.assertEqual(("Psc", "Aqu", "Софья А"), main.searc([19, 3, 2], "Софья А"))
        self.assertEqual(("Psc", "Aqu", "Маша"), main.searc([20, 3, 2], "Маша"))
        self.assertEqual(("Ari", "Ign", "Дима"), main.searc([21, 3, 2], "Дима"))
        self.assertEqual(("Ari", "Ign", "Полина"), main.searc([22, 3, 2], "Полина"))
        self.assertEqual(("Ari", "Ign", "Дима"), main.searc([23, 3, 2], "Дима"))
        self.assertEqual(("Ari", "Ign", "Полина"), main.searc([24, 3, 2], "Полина"))
        self.assertEqual(("Ari", "Ign", "Дима"), main.searc([25, 3, 2], "Дима"))
        self.assertEqual(("Ari", "Ign", "Лиза"), main.searc([26, 3, 2], "Лиза"))
        self.assertEqual(("Ari", "Ign", "Маша"), main.searc([27, 3, 2], "Маша"))
        self.assertEqual(("Ari", "Ign", "Кирилл"), main.searc([28, 3, 2], "Кирилл"))
        self.assertEqual(("Ari", "Ign", "Маша"), main.searc([29, 3, 2], "Маша"))
        self.assertEqual(("Ari", "Ign", "Лиза"), main.searc([30, 3, 2], "Лиза"))
        self.assertEqual(("Ari", "Ign", "Маша"), main.searc([31, 3, 2], "Маша"))
        self.assertEqual(("Ari", "Ign", "Маша"), main.searc([1, 4, 2], "Маша"))
        self.assertEqual(("Ari", "Ign", "Катя Скрицкая"), main.searc([2, 4, 2], "Катя Скрицкая"))
        self.assertEqual(("Ari", "Ign", "Дима"), main.searc([3, 4, 2], "Дима"))
        self.assertEqual(("Ari", "Ign", "Кирилл"), main.searc([4, 4, 2], "Кирилл"))
        self.assertEqual(("Ari", "Ign", "Соня"), main.searc([5, 4, 2], "Соня"))
        self.assertEqual(("Ari", "Ign", "Софья А"), main.searc([6, 4, 2], "Софья А"))
        self.assertEqual(("Ari", "Ign", "Софья А"), main.searc([7, 4, 2], "Софья А"))
        self.assertEqual(("Ari", "Ign", "Дима"), main.searc([8, 4, 2], "Дима"))
        self.assertEqual(("Ari", "Ign", "Рандомное Имя"), main.searc([9, 4, 2], "Рандомное Имя"))
        self.assertEqual(("Ari", "Ign", "Софья А"), main.searc([10, 4, 2], "Софья А"))
        self.assertEqual(("Ari", "Ign", "Соня"), main.searc([11, 4, 2], "Соня"))
        self.assertEqual(("Ari", "Ign", "Соня"), main.searc([12, 4, 2], "Соня"))
        self.assertEqual(("Ari", "Ign", "Катя Скрицкая"), main.searc([13, 4, 2], "Катя Скрицкая"))
        self.assertEqual(("Ari", "Ign", "Лиза"), main.searc([14, 4, 2], "Лиза"))
        self.assertEqual(("Ari", "Ign", "Соня"), main.searc([15, 4, 2], "Соня"))
        self.assertEqual(("Ari", "Ign", "Маша"), main.searc([16, 4, 2], "Маша"))
        self.assertEqual(("Ari", "Ign", "Кирилл"), main.searc([17, 4, 2], "Кирилл"))
        self.assertEqual(("Ari", "Ign", "Лиза"), main.searc([18, 4, 2], "Лиза"))
        self.assertEqual(("Ari", "Ign", "Кирилл"), main.searc([19, 4, 2], "Кирилл"))
        self.assertEqual(("Ari", "Ign", "Лиза"), main.searc([20, 4, 2], "Лиза"))
        self.assertEqual(("Tau", "Ter", "Рандомное Имя"), main.searc([21, 4, 2], "Рандомное Имя"))
        self.assertEqual(("Tau", "Ter", "Лиза"), main.searc([22, 4, 2], "Лиза"))
        self.assertEqual(("Tau", "Ter", "Катя Скрицкая"), main.searc([23, 4, 2], "Катя Скрицкая"))
        self.assertEqual(("Tau", "Ter", "Катя Скрицкая"), main.searc([24, 4, 2], "Катя Скрицкая"))
        self.assertEqual(("Tau", "Ter", "Полина"), main.searc([25, 4, 2], "Полина"))
        self.assertEqual(("Tau", "Ter", "Маша"), main.searc([26, 4, 2], "Маша"))
        self.assertEqual(("Tau", "Ter", "Дима"), main.searc([27, 4, 2], "Дима"))
        self.assertEqual(("Tau", "Ter", "Софья А"), main.searc([28, 4, 2], "Софья А"))
        self.assertEqual(("Tau", "Ter", "Лиза"), main.searc([29, 4, 2], "Лиза"))
        self.assertEqual(("Tau", "Ter", "Рандомное Имя"), main.searc([30, 4, 2], "Рандомное Имя"))
        self.assertEqual(("Tau", "Ter", "Дима"), main.searc([1, 5, 2], "Дима"))
        self.assertEqual(("Tau", "Ter", "Софья А"), main.searc([2, 5, 2], "Софья А"))
        self.assertEqual(("Tau", "Ter", "Софья А"), main.searc([3, 5, 2], "Софья А"))
        self.assertEqual(("Tau", "Ter", "Рандомное Имя"), main.searc([4, 5, 2], "Рандомное Имя"))
        self.assertEqual(("Tau", "Ter", "Рандомное Имя"), main.searc([5, 5, 2], "Рандомное Имя"))
        self.assertEqual(("Tau", "Ter", "Софья А"), main.searc([6, 5, 2], "Софья А"))
        self.assertEqual(("Tau", "Ter", "Лиза"), main.searc([7, 5, 2], "Лиза"))
        self.assertEqual(("Tau", "Ter", "Катя Скрицкая"), main.searc([8, 5, 2], "Катя Скрицкая"))
        self.assertEqual(("Tau", "Ter", "Соня"), main.searc([9, 5, 2], "Соня"))
        self.assertEqual(("Tau", "Ter", "Маша"), main.searc([10, 5, 2], "Маша"))
        self.assertEqual(("Tau", "Ter", "Маша"), main.searc([11, 5, 2], "Маша"))
        self.assertEqual(("Tau", "Ter", "Катя Скрицкая"), main.searc([12, 5, 2], "Катя Скрицкая"))
        self.assertEqual(("Tau", "Ter", "Рандомное Имя"), main.searc([13, 5, 2], "Рандомное Имя"))
        self.assertEqual(("Tau", "Ter", "Маша"), main.searc([14, 5, 2], "Маша"))
        self.assertEqual(("Tau", "Ter", "Соня"), main.searc([15, 5, 2], "Соня"))
        self.assertEqual(("Tau", "Ter", "Лиза"), main.searc([16, 5, 2], "Лиза"))
        self.assertEqual(("Tau", "Ter", "Рандомное Имя"), main.searc([17, 5, 2], "Рандомное Имя"))
        self.assertEqual(("Tau", "Ter", "Рандомное Имя"), main.searc([18, 5, 2], "Рандомное Имя"))
        self.assertEqual(("Tau", "Ter", "Соня"), main.searc([19, 5, 2], "Соня"))
        self.assertEqual(("Tau", "Ter", "Маша"), main.searc([20, 5, 2], "Маша"))
        self.assertEqual(("Tau", "Ter", "Кирилл"), main.searc([21, 5, 2], "Кирилл"))
        self.assertEqual(("Gem", "Air", "Катя Скрицкая"), main.searc([22, 5, 2], "Катя Скрицкая"))
        self.assertEqual(("Gem", "Air", "Кирилл"), main.searc([23, 5, 2], "Кирилл"))
        self.assertEqual(("Gem", "Air", "Софья А"), main.searc([24, 5, 2], "Софья А"))
        self.assertEqual(("Gem", "Air", "Кирилл"), main.searc([25, 5, 2], "Кирилл"))
        self.assertEqual(("Gem", "Air", "Маша"), main.searc([26, 5, 2], "Маша"))
        self.assertEqual(("Gem", "Air", "Катя Скрицкая"), main.searc([27, 5, 2], "Катя Скрицкая"))
        self.assertEqual(("Gem", "Air", "Маша"), main.searc([28, 5, 2], "Маша"))
        self.assertEqual(("Gem", "Air", "Рандомное Имя"), main.searc([29, 5, 2], "Рандомное Имя"))
        self.assertEqual(("Gem", "Air", "Дима"), main.searc([30, 5, 2], "Дима"))
        self.assertEqual(("Gem", "Air", "Рандомное Имя"), main.searc([31, 5, 2], "Рандомное Имя"))
        self.assertEqual(("Gem", "Air", "Дима"), main.searc([1, 6, 2], "Дима"))
        self.assertEqual(("Gem", "Air", "Соня"), main.searc([2, 6, 2], "Соня"))
        self.assertEqual(("Gem", "Air", "Полина"), main.searc([3, 6, 2], "Полина"))
        self.assertEqual(("Gem", "Air", "Катя Скрицкая"), main.searc([4, 6, 2], "Катя Скрицкая"))
        self.assertEqual(("Gem", "Air", "Кирилл"), main.searc([5, 6, 2], "Кирилл"))
        self.assertEqual(("Gem", "Air", "Кирилл"), main.searc([6, 6, 2], "Кирилл"))
        self.assertEqual(("Gem", "Air", "Рандомное Имя"), main.searc([7, 6, 2], "Рандомное Имя"))
        self.assertEqual(("Gem", "Air", "Соня"), main.searc([8, 6, 2], "Соня"))
        self.assertEqual(("Gem", "Air", "Лиза"), main.searc([9, 6, 2], "Лиза"))
        self.assertEqual(("Gem", "Air", "Дима"), main.searc([10, 6, 2], "Дима"))
        self.assertEqual(("Gem", "Air", "Катя Скрицкая"), main.searc([11, 6, 2], "Катя Скрицкая"))
        self.assertEqual(("Gem", "Air", "Лиза"), main.searc([12, 6, 2], "Лиза"))
        self.assertEqual(("Gem", "Air", "Катя Скрицкая"), main.searc([13, 6, 2], "Катя Скрицкая"))
        self.assertEqual(("Gem", "Air", "Соня"), main.searc([14, 6, 2], "Соня"))
        self.assertEqual(("Gem", "Air", "Маша"), main.searc([15, 6, 2], "Маша"))
        self.assertEqual(("Gem", "Air", "Соня"), main.searc([16, 6, 2], "Соня"))
        self.assertEqual(("Gem", "Air", "Кирилл"), main.searc([17, 6, 2], "Кирилл"))
        self.assertEqual(("Gem", "Air", "Лиза"), main.searc([18, 6, 2], "Лиза"))
        self.assertEqual(("Gem", "Air", "Маша"), main.searc([19, 6, 2], "Маша"))
        self.assertEqual(("Gem", "Air", "Дима"), main.searc([20, 6, 2], "Дима"))
        self.assertEqual(("Gem", "Air", "Кирилл"), main.searc([21, 6, 2], "Кирилл"))
        self.assertEqual(("Cnc", "Aqu", "Кирилл"), main.searc([22, 6, 2], "Кирилл"))
        self.assertEqual(("Cnc", "Aqu", "Рандомное Имя"), main.searc([23, 6, 2], "Рандомное Имя"))
        self.assertEqual(("Cnc", "Aqu", "Соня"), main.searc([24, 6, 2], "Соня"))
        self.assertEqual(("Cnc", "Aqu", "Катя Скрицкая"), main.searc([25, 6, 2], "Катя Скрицкая"))
        self.assertEqual(("Cnc", "Aqu", "Лиза"), main.searc([26, 6, 2], "Лиза"))
        self.assertEqual(("Cnc", "Aqu", "Рандомное Имя"), main.searc([27, 6, 2], "Рандомное Имя"))
        self.assertEqual(("Cnc", "Aqu", "Лиза"), main.searc([28, 6, 2], "Лиза"))
        self.assertEqual(("Cnc", "Aqu", "Софья А"), main.searc([29, 6, 2], "Софья А"))
        self.assertEqual(("Cnc", "Aqu", "Полина"), main.searc([30, 6, 2], "Полина"))
        self.assertEqual(("Cnc", "Aqu", "Лиза"), main.searc([1, 7, 2], "Лиза"))
        self.assertEqual(("Cnc", "Aqu", "Дима"), main.searc([2, 7, 2], "Дима"))
        self.assertEqual(("Cnc", "Aqu", "Соня"), main.searc([3, 7, 2], "Соня"))
        self.assertEqual(("Cnc", "Aqu", "Соня"), main.searc([4, 7, 2], "Соня"))
        self.assertEqual(("Cnc", "Aqu", "Катя Скрицкая"), main.searc([5, 7, 2], "Катя Скрицкая"))
        self.assertEqual(("Cnc", "Aqu", "Дима"), main.searc([6, 7, 2], "Дима"))
        self.assertEqual(("Cnc", "Aqu", "Дима"), main.searc([7, 7, 2], "Дима"))
        self.assertEqual(("Cnc", "Aqu", "Маша"), main.searc([8, 7, 2], "Маша"))
        self.assertEqual(("Cnc", "Aqu", "Катя Скрицкая"), main.searc([9, 7, 2], "Катя Скрицкая"))
        self.assertEqual(("Cnc", "Aqu", "Полина"), main.searc([10, 7, 2], "Полина"))
        self.assertEqual(("Cnc", "Aqu", "Кирилл"), main.searc([11, 7, 2], "Кирилл"))
        self.assertEqual(("Cnc", "Aqu", "Маша"), main.searc([12, 7, 2], "Маша"))
        self.assertEqual(("Cnc", "Aqu", "Маша"), main.searc([13, 7, 2], "Маша"))
        self.assertEqual(("Cnc", "Aqu", "Маша"), main.searc([14, 7, 2], "Маша"))
        self.assertEqual(("Cnc", "Aqu", "Дима"), main.searc([15, 7, 2], "Дима"))
        self.assertEqual(("Cnc", "Aqu", "Лиза"), main.searc([16, 7, 2], "Лиза"))
        self.assertEqual(("Cnc", "Aqu", "Полина"), main.searc([17, 7, 2], "Полина"))
        self.assertEqual(("Cnc", "Aqu", "Рандомное Имя"), main.searc([18, 7, 2], "Рандомное Имя"))
        self.assertEqual(("Cnc", "Aqu", "Маша"), main.searc([19, 7, 2], "Маша"))
        self.assertEqual(("Cnc", "Aqu", "Лиза"), main.searc([20, 7, 2], "Лиза"))
        self.assertEqual(("Cnc", "Aqu", "Полина"), main.searc([21, 7, 2], "Полина"))
        self.assertEqual(("Cnc", "Aqu", "Софья А"), main.searc([22, 7, 2], "Софья А"))
        self.assertEqual(("Leo", "Ign", "Соня"), main.searc([23, 7, 2], "Соня"))
        self.assertEqual(("Leo", "Ign", "Полина"), main.searc([24, 7, 2], "Полина"))
        self.assertEqual(("Leo", "Ign", "Кирилл"), main.searc([25, 7, 2], "Кирилл"))
        self.assertEqual(("Leo", "Ign", "Маша"), main.searc([26, 7, 2], "Маша"))
        self.assertEqual(("Leo", "Ign", "Маша"), main.searc([27, 7, 2], "Маша"))
        self.assertEqual(("Leo", "Ign", "Маша"), main.searc([28, 7, 2], "Маша"))
        self.assertEqual(("Leo", "Ign", "Рандомное Имя"), main.searc([29, 7, 2], "Рандомное Имя"))
        self.assertEqual(("Leo", "Ign", "Дима"), main.searc([30, 7, 2], "Дима"))
        self.assertEqual(("Leo", "Ign", "Полина"), main.searc([31, 7, 2], "Полина"))
        self.assertEqual(("Leo", "Ign", "Катя Скрицкая"), main.searc([1, 8, 2], "Катя Скрицкая"))
        self.assertEqual(("Leo", "Ign", "Рандомное Имя"), main.searc([2, 8, 2], "Рандомное Имя"))
        self.assertEqual(("Leo", "Ign", "Кирилл"), main.searc([3, 8, 2], "Кирилл"))
        self.assertEqual(("Leo", "Ign", "Катя Скрицкая"), main.searc([4, 8, 2], "Катя Скрицкая"))
        self.assertEqual(("Leo", "Ign", "Дима"), main.searc([5, 8, 2], "Дима"))
        self.assertEqual(("Leo", "Ign", "Рандомное Имя"), main.searc([6, 8, 2], "Рандомное Имя"))
        self.assertEqual(("Leo", "Ign", "Катя Скрицкая"), main.searc([7, 8, 2], "Катя Скрицкая"))
        self.assertEqual(("Leo", "Ign", "Кирилл"), main.searc([8, 8, 2], "Кирилл"))
        self.assertEqual(("Leo", "Ign", "Маша"), main.searc([9, 8, 2], "Маша"))
        self.assertEqual(("Leo", "Ign", "Лиза"), main.searc([10, 8, 2], "Лиза"))
        self.assertEqual(("Leo", "Ign", "Кирилл"), main.searc([11, 8, 2], "Кирилл"))
        self.assertEqual(("Leo", "Ign", "Полина"), main.searc([12, 8, 2], "Полина"))
        self.assertEqual(("Leo", "Ign", "Софья А"), main.searc([13, 8, 2], "Софья А"))
        self.assertEqual(("Leo", "Ign", "Рандомное Имя"), main.searc([14, 8, 2], "Рандомное Имя"))
        self.assertEqual(("Leo", "Ign", "Кирилл"), main.searc([15, 8, 2], "Кирилл"))
        self.assertEqual(("Leo", "Ign", "Соня"), main.searc([16, 8, 2], "Соня"))
        self.assertEqual(("Leo", "Ign", "Полина"), main.searc([17, 8, 2], "Полина"))
        self.assertEqual(("Leo", "Ign", "Лиза"), main.searc([18, 8, 2], "Лиза"))
        self.assertEqual(("Leo", "Ign", "Лиза"), main.searc([19, 8, 2], "Лиза"))
        self.assertEqual(("Leo", "Ign", "Дима"), main.searc([20, 8, 2], "Дима"))
        self.assertEqual(("Leo", "Ign", "Софья А"), main.searc([21, 8, 2], "Софья А"))
        self.assertEqual(("Vir", "Ter", "Катя Скрицкая"), main.searc([22, 8, 2], "Катя Скрицкая"))
        self.assertEqual(("Vir", "Ter", "Полина"), main.searc([23, 8, 2], "Полина"))
        self.assertEqual(("Vir", "Ter", "Соня"), main.searc([24, 8, 2], "Соня"))
        self.assertEqual(("Vir", "Ter", "Соня"), main.searc([25, 8, 2], "Соня"))
        self.assertEqual(("Vir", "Ter", "Лиза"), main.searc([26, 8, 2], "Лиза"))
        self.assertEqual(("Vir", "Ter", "Рандомное Имя"), main.searc([27, 8, 2], "Рандомное Имя"))
        self.assertEqual(("Vir", "Ter", "Катя Скрицкая"), main.searc([28, 8, 2], "Катя Скрицкая"))
        self.assertEqual(("Vir", "Ter", "Катя Скрицкая"), main.searc([29, 8, 2], "Катя Скрицкая"))
        self.assertEqual(("Vir", "Ter", "Соня"), main.searc([30, 8, 2], "Соня"))
        self.assertEqual(("Vir", "Ter", "Рандомное Имя"), main.searc([31, 8, 2], "Рандомное Имя"))
        self.assertEqual(("Vir", "Ter", "Соня"), main.searc([1, 9, 2], "Соня"))
        self.assertEqual(("Vir", "Ter", "Рандомное Имя"), main.searc([2, 9, 2], "Рандомное Имя"))
        self.assertEqual(("Vir", "Ter", "Маша"), main.searc([3, 9, 2], "Маша"))
        self.assertEqual(("Vir", "Ter", "Рандомное Имя"), main.searc([4, 9, 2], "Рандомное Имя"))
        self.assertEqual(("Vir", "Ter", "Соня"), main.searc([5, 9, 2], "Соня"))
        self.assertEqual(("Vir", "Ter", "Рандомное Имя"), main.searc([6, 9, 2], "Рандомное Имя"))
        self.assertEqual(("Vir", "Ter", "Полина"), main.searc([7, 9, 2], "Полина"))
        self.assertEqual(("Vir", "Ter", "Кирилл"), main.searc([8, 9, 2], "Кирилл"))
        self.assertEqual(("Vir", "Ter", "Кирилл"), main.searc([9, 9, 2], "Кирилл"))
        self.assertEqual(("Vir", "Ter", "Рандомное Имя"), main.searc([10, 9, 2], "Рандомное Имя"))
        self.assertEqual(("Vir", "Ter", "Соня"), main.searc([11, 9, 2], "Соня"))
        self.assertEqual(("Vir", "Ter", "Катя Скрицкая"), main.searc([12, 9, 2], "Катя Скрицкая"))
        self.assertEqual(("Vir", "Ter", "Софья А"), main.searc([13, 9, 2], "Софья А"))
        self.assertEqual(("Vir", "Ter", "Софья А"), main.searc([14, 9, 2], "Софья А"))
        self.assertEqual(("Vir", "Ter", "Катя Скрицкая"), main.searc([15, 9, 2], "Катя Скрицкая"))
        self.assertEqual(("Vir", "Ter", "Лиза"), main.searc([16, 9, 2], "Лиза"))
        self.assertEqual(("Vir", "Ter", "Софья А"), main.searc([17, 9, 2], "Софья А"))
        self.assertEqual(("Vir", "Ter", "Полина"), main.searc([18, 9, 2], "Полина"))
        self.assertEqual(("Vir", "Ter", "Катя Скрицкая"), main.searc([19, 9, 2], "Катя Скрицкая"))
        self.assertEqual(("Vir", "Ter", "Маша"), main.searc([20, 9, 2], "Маша"))
        self.assertEqual(("Vir", "Ter", "Соня"), main.searc([21, 9, 2], "Соня"))
        self.assertEqual(("Vir", "Ter", "Катя Скрицкая"), main.searc([22, 9, 2], "Катя Скрицкая"))
        self.assertEqual(("Vir", "Ter", "Катя Скрицкая"), main.searc([23, 9, 2], "Катя Скрицкая"))
        self.assertEqual(("Lib", "Air", "Лиза"), main.searc([24, 9, 2], "Лиза"))
        self.assertEqual(("Lib", "Air", "Кирилл"), main.searc([25, 9, 2], "Кирилл"))
        self.assertEqual(("Lib", "Air", "Катя Скрицкая"), main.searc([26, 9, 2], "Катя Скрицкая"))
        self.assertEqual(("Lib", "Air", "Катя Скрицкая"), main.searc([27, 9, 2], "Катя Скрицкая"))
        self.assertEqual(("Lib", "Air", "Лиза"), main.searc([28, 9, 2], "Лиза"))
        self.assertEqual(("Lib", "Air", "Лиза"), main.searc([29, 9, 2], "Лиза"))
        self.assertEqual(("Lib", "Air", "Соня"), main.searc([30, 9, 2], "Соня"))
        self.assertEqual(("Lib", "Air", "Софья А"), main.searc([1, 10, 2], "Софья А"))
        self.assertEqual(("Lib", "Air", "Маша"), main.searc([2, 10, 2], "Маша"))
        self.assertEqual(("Lib", "Air", "Дима"), main.searc([3, 10, 2], "Дима"))
        self.assertEqual(("Lib", "Air", "Дима"), main.searc([4, 10, 2], "Дима"))
        self.assertEqual(("Lib", "Air", "Софья А"), main.searc([5, 10, 2], "Софья А"))
        self.assertEqual(("Lib", "Air", "Дима"), main.searc([6, 10, 2], "Дима"))
        self.assertEqual(("Lib", "Air", "Соня"), main.searc([7, 10, 2], "Соня"))
        self.assertEqual(("Lib", "Air", "Рандомное Имя"), main.searc([8, 10, 2], "Рандомное Имя"))
        self.assertEqual(("Lib", "Air", "Рандомное Имя"), main.searc([9, 10, 2], "Рандомное Имя"))
        self.assertEqual(("Lib", "Air", "Соня"), main.searc([10, 10, 2], "Соня"))
        self.assertEqual(("Lib", "Air", "Софья А"), main.searc([11, 10, 2], "Софья А"))
        self.assertEqual(("Lib", "Air", "Маша"), main.searc([12, 10, 2], "Маша"))
        self.assertEqual(("Lib", "Air", "Маша"), main.searc([13, 10, 2], "Маша"))
        self.assertEqual(("Lib", "Air", "Рандомное Имя"), main.searc([14, 10, 2], "Рандомное Имя"))
        self.assertEqual(("Lib", "Air", "Полина"), main.searc([15, 10, 2], "Полина"))
        self.assertEqual(("Lib", "Air", "Рандомное Имя"), main.searc([16, 10, 2], "Рандомное Имя"))
        self.assertEqual(("Lib", "Air", "Рандомное Имя"), main.searc([17, 10, 2], "Рандомное Имя"))
        self.assertEqual(("Lib", "Air", "Кирилл"), main.searc([18, 10, 2], "Кирилл"))
        self.assertEqual(("Lib", "Air", "Рандомное Имя"), main.searc([19, 10, 2], "Рандомное Имя"))
        self.assertEqual(("Lib", "Air", "Лиза"), main.searc([20, 10, 2], "Лиза"))
        self.assertEqual(("Lib", "Air", "Маша"), main.searc([21, 10, 2], "Маша"))
        self.assertEqual(("Lib", "Air", "Кирилл"), main.searc([22, 10, 2], "Кирилл"))
        self.assertEqual(("Lib", "Air", "Соня"), main.searc([23, 10, 2], "Соня"))
        self.assertEqual(("Sco", "Aqu", "Соня"), main.searc([24, 10, 2], "Соня"))
        self.assertEqual(("Sco", "Aqu", "Соня"), main.searc([25, 10, 2], "Соня"))
        self.assertEqual(("Sco", "Aqu", "Соня"), main.searc([26, 10, 2], "Соня"))
        self.assertEqual(("Sco", "Aqu", "Соня"), main.searc([27, 10, 2], "Соня"))
        self.assertEqual(("Sco", "Aqu", "Софья А"), main.searc([28, 10, 2], "Софья А"))
        self.assertEqual(("Sco", "Aqu", "Лиза"), main.searc([29, 10, 2], "Лиза"))
        self.assertEqual(("Sco", "Aqu", "Маша"), main.searc([30, 10, 2], "Маша"))
        self.assertEqual(("Sco", "Aqu", "Рандомное Имя"), main.searc([31, 10, 2], "Рандомное Имя"))
        self.assertEqual(("Sco", "Aqu", "Рандомное Имя"), main.searc([1, 11, 2], "Рандомное Имя"))
        self.assertEqual(("Sco", "Aqu", "Соня"), main.searc([2, 11, 2], "Соня"))
        self.assertEqual(("Sco", "Aqu", "Дима"), main.searc([3, 11, 2], "Дима"))
        self.assertEqual(("Sco", "Aqu", "Полина"), main.searc([4, 11, 2], "Полина"))
        self.assertEqual(("Sco", "Aqu", "Рандомное Имя"), main.searc([5, 11, 2], "Рандомное Имя"))
        self.assertEqual(("Sco", "Aqu", "Кирилл"), main.searc([6, 11, 2], "Кирилл"))
        self.assertEqual(("Sco", "Aqu", "Кирилл"), main.searc([7, 11, 2], "Кирилл"))
        self.assertEqual(("Sco", "Aqu", "Лиза"), main.searc([8, 11, 2], "Лиза"))
        self.assertEqual(("Sco", "Aqu", "Соня"), main.searc([9, 11, 2], "Соня"))
        self.assertEqual(("Sco", "Aqu", "Катя Скрицкая"), main.searc([10, 11, 2], "Катя Скрицкая"))
        self.assertEqual(("Sco", "Aqu", "Софья А"), main.searc([11, 11, 2], "Софья А"))
        self.assertEqual(("Sco", "Aqu", "Лиза"), main.searc([12, 11, 2], "Лиза"))
        self.assertEqual(("Sco", "Aqu", "Дима"), main.searc([13, 11, 2], "Дима"))
        self.assertEqual(("Sco", "Aqu", "Лиза"), main.searc([14, 11, 2], "Лиза"))
        self.assertEqual(("Sco", "Aqu", "Полина"), main.searc([15, 11, 2], "Полина"))
        self.assertEqual(("Sco", "Aqu", "Софья А"), main.searc([16, 11, 2], "Софья А"))
        self.assertEqual(("Sco", "Aqu", "Дима"), main.searc([17, 11, 2], "Дима"))
        self.assertEqual(("Sco", "Aqu", "Соня"), main.searc([18, 11, 2], "Соня"))
        self.assertEqual(("Sco", "Aqu", "Соня"), main.searc([19, 11, 2], "Соня"))
        self.assertEqual(("Sco", "Aqu", "Дима"), main.searc([20, 11, 2], "Дима"))
        self.assertEqual(("Sco", "Aqu", "Соня"), main.searc([21, 11, 2], "Соня"))
        self.assertEqual(("Sco", "Aqu", "Лиза"), main.searc([22, 11, 2], "Лиза"))
        self.assertEqual(("Sgr", "Ign", "Лиза"), main.searc([23, 11, 2], "Лиза"))
        self.assertEqual(("Sgr", "Ign", "Полина"), main.searc([24, 11, 2], "Полина"))
        self.assertEqual(("Sgr", "Ign", "Кирилл"), main.searc([25, 11, 2], "Кирилл"))
        self.assertEqual(("Sgr", "Ign", "Соня"), main.searc([26, 11, 2], "Соня"))
        self.assertEqual(("Sgr", "Ign", "Софья А"), main.searc([27, 11, 2], "Софья А"))
        self.assertEqual(("Sgr", "Ign", "Маша"), main.searc([28, 11, 2], "Маша"))
        self.assertEqual(("Sgr", "Ign", "Софья А"), main.searc([29, 11, 2], "Софья А"))
        self.assertEqual(("Sgr", "Ign", "Дима"), main.searc([30, 11, 2], "Дима"))
        self.assertEqual(("Sgr", "Ign", "Кирилл"), main.searc([1, 12, 2], "Кирилл"))
        self.assertEqual(("Sgr", "Ign", "Софья А"), main.searc([2, 12, 2], "Софья А"))
        self.assertEqual(("Sgr", "Ign", "Софья А"), main.searc([3, 12, 2], "Софья А"))
        self.assertEqual(("Sgr", "Ign", "Лиза"), main.searc([4, 12, 2], "Лиза"))
        self.assertEqual(("Sgr", "Ign", "Лиза"), main.searc([5, 12, 2], "Лиза"))
        self.assertEqual(("Sgr", "Ign", "Дима"), main.searc([6, 12, 2], "Дима"))
        self.assertEqual(("Sgr", "Ign", "Полина"), main.searc([7, 12, 2], "Полина"))
        self.assertEqual(("Sgr", "Ign", "Полина"), main.searc([8, 12, 2], "Полина"))
        self.assertEqual(("Sgr", "Ign", "Лиза"), main.searc([9, 12, 2], "Лиза"))
        self.assertEqual(("Sgr", "Ign", "Кирилл"), main.searc([10, 12, 2], "Кирилл"))
        self.assertEqual(("Sgr", "Ign", "Кирилл"), main.searc([11, 12, 2], "Кирилл"))
        self.assertEqual(("Sgr", "Ign", "Дима"), main.searc([12, 12, 2], "Дима"))
        self.assertEqual(("Sgr", "Ign", "Кирилл"), main.searc([13, 12, 2], "Кирилл"))
        self.assertEqual(("Sgr", "Ign", "Полина"), main.searc([14, 12, 2], "Полина"))
        self.assertEqual(("Sgr", "Ign", "Рандомное Имя"), main.searc([15, 12, 2], "Рандомное Имя"))
        self.assertEqual(("Sgr", "Ign", "Соня"), main.searc([16, 12, 2], "Соня"))
        self.assertEqual(("Sgr", "Ign", "Софья А"), main.searc([17, 12, 2], "Софья А"))
        self.assertEqual(("Sgr", "Ign", "Соня"), main.searc([18, 12, 2], "Соня"))
        self.assertEqual(("Sgr", "Ign", "Лиза"), main.searc([19, 12, 2], "Лиза"))
        self.assertEqual(("Sgr", "Ign", "Дима"), main.searc([20, 12, 2], "Дима"))
        self.assertEqual(("Sgr", "Ign", "Дима"), main.searc([21, 12, 2], "Дима"))
        self.assertEqual(("Sgr", "Ign", "Соня"), main.searc([22, 12, 2], "Соня"))
        self.assertEqual(("Cap", "Ter", "Лиза"), main.searc([23, 12, 2], "Лиза"))
        self.assertEqual(("Cap", "Ter", "Дима"), main.searc([24, 12, 2], "Дима"))
        self.assertEqual(("Cap", "Ter", "Кирилл"), main.searc([25, 12, 2], "Кирилл"))
        self.assertEqual(("Cap", "Ter", "Лиза"), main.searc([26, 12, 2], "Лиза"))
        self.assertEqual(("Cap", "Ter", "Рандомное Имя"), main.searc([27, 12, 2], "Рандомное Имя"))
        self.assertEqual(("Cap", "Ter", "Полина"), main.searc([28, 12, 2], "Полина"))
        self.assertEqual(("Cap", "Ter", "Полина"), main.searc([29, 12, 2], "Полина"))
        self.assertEqual(("Cap", "Ter", "Кирилл"), main.searc([30, 12, 2], "Кирилл"))
        self.assertEqual(("Cap", "Ter", "Соня"), main.searc([31, 12, 2], "Соня"))
        self.assertEqual(("Cap", "Ter", "Соня"), main.searc([1, 1, 3], "Соня"))
    '''def test_low_comp(self):
        hum1 = ("Cap", "Ter", "name1")
        hum2 = ("Vir", "Ter", "name2")
        m = aiogram.types.message.Message()
        self.assertGreaterEqual(38, main.comp(hum1, hum2, m))

    def test_upper_comp(self):
        hum1 = ("Cap", "Ter", "name1")
        hum2 = ("Vir", "Ter", "name2")
        m = aiogram.types.message.Message()
        self.assertLessEqual(71, main.comp(hum1, hum2, m))'''

if __name__ == '__main__':
    unittest.main()