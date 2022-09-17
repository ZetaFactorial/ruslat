import unittest

from ruslat import latinizator, regularize

expected_conversion = {
    'съесть': 'sjestj',
    'вьюга': 'vjuga',
    'Илья - Ильи': 'Ilja - Ilji',
    'яблочный': 'jabločnyj',
    'ёлка': 'jëlka',
    'Россия': 'Rossija',
    'рябь': 'riabj',
    'шёлк': 'šëlk',
    'БОЛЬШИЕ БУКВЫ': 'BOLJŠIJE BUKVY',

    'Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства':
    'Širokaja elektrifikacija južnyh gubernij dast mosčnyj tolčok podjëmu seljskogo hoziajstva',

    'Съешь же ещё этих мягких французских булок да выпей чаю.':
    'Sješ že jesčë etih miagkih francuzskih bulok da vypej čaju.',

    'В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!':
    'V časčah juga žil by citrus? Da, no faljšivyj ekzempliar!',

    'Шеф взъярён тчк щипцы с эхом гудбай Жюль.':
    'Šef vzjarën tčk sčipci s ehom gudbaj Žulj.',
}

class ConversionTestCase(unittest.TestCase):
    def test_regularization(self):
        self.assertEqual(regularize('мышь'),'мыш') # (кродеться)

    def test_conversion_to_latin(self):
        for cyr, lat in expected_conversion.items():
            self.assertEqual(latinizator(cyr), lat)

if __name__ == '__main__':
    unittest.main()