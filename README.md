# Converter for Russian Latin Alphabet

## Installation
```pip install ruslat```

## Usage
Using a function
```python
>>> import ruslat
>>> ruslat.latinizator('Съешь же ещё этих мягких французских булок да выпей чаю.')
'Sješ že jesčë etih miagkih francuzskih bulok da vypej čaju.'
```
From command line (Windows example)
```
C:\Users\user>py -m ruslat "В чащах юга жил бы цитрус.."
V časčah juga žil by citrus..
```

## Known issues
- Each word must be in lowercase, titlecase or uppercase. "Mixed case" like `ФсЕМ прИФФкИ в эТОм чЯТиКе` is not allowed, but `ПРИВЕТ` or `Чатик` works. For regular texts, it is enough.
- Word 'Я' (not letter, but word) is always being converted to 'Ja', even if it's e.g. a title: `КАК Я ПРОВЕЛ ЛЕТО -> KAK Ja PROVEL LETO`.

## License
ruslat is licensed under the MIT License. For the full text, check out `LICENSE`.