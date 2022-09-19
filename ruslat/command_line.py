import ruslat
from argparse import ArgumentParser
from pathlib import Path

def main():
    parser = ArgumentParser(description="Russian Latinizator")
    parser.add_argument("filename", help="name of txt file to convert")
    args = parser.parse_args()
    cyrfilename = args.filename
    latfilename = 'lat_'+args.filename
    try:
        open(cyrfilename, 'r')
    except FileNotFoundError:
        print(f"Error: file {cyrfilename} is not found in {Path().absolute()}")
    else:
        with open(args.filename, 'r', encoding='utf-8') as cyr,\
            open(f'{latfilename}', 'w', encoding='utf-8') as lat:
            for line in cyr:
                lat.write(ruslat.latinizator(line))
        print(f"Succesfully latinized {cyrfilename} to {latfilename}")