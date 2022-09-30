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

    def create_city_entry(self, city_info):
        # type: (list)->None
        """
        name, aliases, region, ruler, size, population, demonym, races, religions, alignment,
                          notes
        Returns: None

        """

        self.curs.executemany("INSERT INTO city VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", city_info)

    def create_npc_entry(self, npc_info):
        # type: (list)->None
        """
        name, surname, titles, aliases, nicknames, race, occupation, sex, age, home, patron,
                         notes
        Returns: None

        """

        self.curs.execute("INSERT INTO npc VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", npc_info)

    def create_event_entry(self, event_info):
        # type: (list) -> None
        """
        name, type, date, duration, location, cause, involved, notes
        Args:
            event_info:

        Returns:

        """

        self.curs.execute("INSERT INTO event VALUES(?, ?, ?, ?, ?, ?, ?, ?)", event_info)

    def create_generic_entry(self, generic_info):
        # type: (list) -> None
        """
        name, notes
        Args:
            generic_info:

        Returns:

        """
        self.curs.execute("INSERT INTO event VALUES(?, ?)", generic_info)
