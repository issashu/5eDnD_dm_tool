import sqlite3 as sql
import os


class AppDB(object):

    def __init__(self):
        print("DEBUG: DB created in: {}".format(os.getcwd()))
        self.conn = sql.connect('map_entries.db')
        self.curs = self.conn.cursor()
        self.curs.execute("CREATE TABLE city(name, aliases, region, ruler, size, population, demonym, races, "
                          "religions, alignment, notes)")
        self.curs.execute("CREATE TABLE npc(name, surname, titles, aliases, nicknames, race, occupation sex, "
                          "age, home, patron, notes )")
        self.curs.execute("CREATE TABLE event(name, type, date, duration, location, cause, other involved,"
                          " notes )")
        self.curs.execute("CREATE TABLE generic(name, notes)")

    def create_city_entry(self, name, aliases, region, ruler, size, population, demonym, races, religions, alignment,
                          notes):
        #TODO Make the arguments as one list object
        self.curs.execute("INSERT INTO city VALUES('{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{}', '{}', '{}')"
                          .format(name, aliases, region, ruler, size, population, demonym, races, religions, alignment,
                          notes))


    def create_npc_entry(self, name, surname, titles, aliases, nicknames, race, occupation, sex, age, home, patron,
                         notes):
        # TODO Make the arguments as one list object
        self.curs.execute("INSERT INTO npc VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}')"
                          .format(name, surname, titles, aliases, nicknames, race, occupation, sex, age, home, patron,
                                  notes))


    def create_event_entry(self, name, type, date, duration, location, cause, other, involved, notes):
        # TODO Make the arguments as one list object
        self.curs.execute("INSERT INTO event VALUES('{}', '{}', {}, {}, '{}', '{}', '{}', {})"
                          .format(name, type, date, duration, location, cause, involved, notes))

    def create_generic_entry(self, name, notes):
        # TODO Make the arguments as one list object
        self.curs.execute("INSERT INTO event VALUES('{}', '{}')".format(name, notes))
