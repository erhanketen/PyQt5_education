from sqlite3 import connect

class DB:
    def __init__(self):
        self.con = connect("Kullanıcı_Girişi_DB.db")
        self.cursor = self.con.cursor()

    def baglanti_kes(self):
        self.con.close()

    def veri_cek(self,bilgiler: tuple):

        self.cursor.execute("""
        SELECT * FROM Kullanicilar WHERE kullanıcı_adı = ? AND sifre = ?
        """,(bilgiler[0],bilgiler[1]))

        bilgi = self.cursor.fetchall()

        if bilgi:
            return True
        else:
            return False

    def veri_bas(self,bilgiler: tuple):

        self.cursor.execute("""
        SELECT * FROM Kullanicilar WHERE kullanıcı_adı = ? AND sifre = ?
        """,(bilgiler[0],bilgiler[1]))

        bilgi = self.cursor.fetchall()

        if bilgi:
            return "Bu Kullanıcı Zaten Var!"

        self.cursor.execute("""
        INSERT INTO Kullanicilar VALUES (?,?)
        """,(bilgiler[0],bilgiler[1]))

        self.con.commit()

DBconnection = DB()


