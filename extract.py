"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo = []
    with open(neo_csv_path, 'r') as f:
        csvfile = csv.DictReader(f, delimiter=',')
        for row in csvfile:
            info = {
                'designation': row['pdes'],
                'name': row['name'],
                'diameter': row['diameter'],
                'hazardous': row['pha']
                }
            neo.append(NearEarthObject(**info))


    return neo


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    cad = []
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)  # Parse JSON data into a Python object.

        fields = contents['fields']
        key = {}
        for i in range(len(fields)):
            key[fields[i]] = i

        data = contents['data']

        for approach in data:
            info = {
                '_designation': approach[key['des']],
                'time': approach[key['cd']],
                'distance': approach[key['dist']],
                'velocity': approach[key['v_rel']],
                }
            cad.append(CloseApproach(**info))

    return cad
