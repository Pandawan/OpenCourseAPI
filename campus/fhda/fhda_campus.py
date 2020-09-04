from os.path import join

from tinydb import TinyDB

from common import ApiError, DB_DIR


class FHDACampus:
    CAMPUS = ['fh', 'da']
    QUARTER_TO_NUM = {
        'summer': 1,
        'fall': 2,
        'winter': 3,
        'spring': 4
    }
    CAMPUS_TO_NUM = {
        'fh': 1,
        'da': 2
    }

    def load_db(self, campus, year, quarter):
        if quarter not in self.QUARTER_TO_NUM:
            raise ApiError(
                404,
                f'Invalid quarter name. Possible quarters are {", ".join(self.QUARTER_TO_NUM.keys())}'
            )

        name = f'{year}{self.QUARTER_TO_NUM[quarter]}{self.CAMPUS_TO_NUM[campus]}'

        try:
            db = TinyDB(join(DB_DIR, f'fhda/{name}_database.json'), access_mode='r')
        except FileNotFoundError:
            # raise FileNotFoundError
            try:
                db = TinyDB(join(DB_DIR, f'fhda/new_{name}_database.json'), access_mode='r')
            except FileNotFoundError:
                # raise FileNotFoundError
                try:
                    db = TinyDB(join(DB_DIR, f'fhda/sched_{name}_database.json'), access_mode='r')
                except FileNotFoundError:
                    raise FileNotFoundError

        return db


fhda_campus = FHDACampus()
