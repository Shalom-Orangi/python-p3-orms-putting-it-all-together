import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    def __init__(self,name,breed):
        self.id=None
        self.name=name
        self.breed=breed

    @classmethod
    def create_table(cls):
      sql="""
          CREATE TABLE IF NOT EXISTS dogs
          id INTEGER PRIMARY KEY,
          name TEXT,
          breed TEXT
      """  
      CURSOR.execute(sql)
      CONN.commit()

    @classmethod
    def drop_table(cls):
       
       CURSOR.execute('DROP TABLE IF EXISTS,dogs')
       CONN.commit()
       CONN.close()

    def save(self):
        sql="""
            INSERT INTO dogs(name,breed)
            VALUES(?,?)
        """
        CURSOR.execute(sql(self.name,self.breed))
        CONN.commit()

    @classmethod
    def create(cls,name,breed):
        dog=cls(name,breed)
        dog.save()
        CONN.commit()

    @classmethod
    def from_database(cls, data):
        dog = cls(name=data[1], breed=data[2]) 
        dog.id = data[0]
        return dog
        

    @classmethod
    def find_by_name(cls):
        sql="""
        SELECT * FROM dogs WHERE name=?,(name,)
        """
        row=CURSOR.fetchone()
        CONN.close()

        if row:
           return cls.from_database(row)
        else:
           return None
        
    @classmethod
    def find_by_id(cls):
        sql="""
        SELECT * FROM dogs WHERE id = ?", (dog_id,)
        """
        row=CURSOR.fetchone()
        CONN.close()
        
        if row:
            return cls.from_database(row)
        else:
            return None
    
    