import sqlite3
from pprint import pprint
import os.path
from pandas import DataFrame
import json

def _pass():
    pass

def SqliteLocDataConver(name : str):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, f"{name}.bytes")
    with sqlite3.connect(db_path) as db:
        ans = db.execute(f"SELECT * FROM '{name}'")
        d = ans.fetchall()
        df = DataFrame(d,columns=['key', 'value'],index=[str(i) for i in range(len(d))])
        result = df.to_json(orient="table", indent=4, force_ascii=False)
        with open(os.path.join(BASE_DIR, f"{name}.json"), 'w', encoding='utf-8') as f:
            f.write(result)


def SqliteMapDataConvert(name : str):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, f"{name}.bytes")
    with sqlite3.connect(db_path) as db:
        ans = db.execute(f"SELECT maps FROM 'mapNames'")
        names = ans.fetchall()
        data = []

        for item in names:
            ans = db.execute(f"SELECT * FROM {item[0]}")
            data.append(ans.fetchall())

    for index,map in enumerate(data):
        df = DataFrame(
            map,
            columns=[
                'index',
                'type',
                'x',
                'y',
                'z',
                'Ry',
                'Rx',
                'Rz',
                ],
            index=[str(i) for i in range(len(map))]
        )
        result = df.to_json(orient="table", indent=4,force_ascii=False)

        with open(os.path.join(BASE_DIR, f"{names[index][0]}.json"), 'w', encoding='utf-8') as f:
            f.write(result)
    pprint(result)

if __name__ == "__main__":
    _pass()
    SqliteLocDataConver("EnglishLocalization")
    SqliteLocDataConver("UkrainianLocalization")
    # SqliteMapDataConvert("db")