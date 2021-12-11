"""
Módulo model.py
"""
import re
import mysql.connector

class Model:
    """
    Clase Model
    Obtiene y guarda en base de datos.
    """
    def get_all(self):
        """
        devuelve todos los registros
        de la tabla noticias
        ordenados por fecha
        """
        db_cacho = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="carro_maier"
        )

        csr_cacho = db_cacho.cursor()
        sql_get = """
            SELECT
                Id
                , Fecha
                , Medio
                , Seccion
                , Titulo
                , Cuerpo
            FROM Noticias
            ORDER BY Fecha DESC
            """

        csr_cacho.execute(sql_get)
        resultado = csr_cacho.fetchall()

        db_cacho.close()

        return resultado

    def get_medios(self):
        """
        devuelve todos los registros
        de la tabla medios
        ordenados por descripción
        """
        r_list = []

        db_cacho = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="carro_maier"
        )

        csr_cacho = db_cacho.cursor()
        sql_get = """
            SELECT
                Id
                , Descripcion
            FROM Medios
            ORDER BY Descripcion
            """
        csr_cacho.execute(sql_get)
        resultado = csr_cacho.fetchall()
        for r in resultado:
            r_list.append(r)

        return r_list

    def get_secciones(self, id_medio):
        """
        devuelve todos los registros
        de la tabla secciones
        según id_medio indicado
        ordenados por descripción
        """
        r_list = []

        db_cacho = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="carro_maier"
        )

        csr_cacho = db_cacho.cursor()
        sql_get = """
            SELECT
                Id
                , Descripcion
            FROM Secciones
            WHERE IdMedio = %s
            ORDER BY Descripcion
            """

        csr_cacho.execute(sql_get, (id_medio, ))
        resultado = csr_cacho.fetchall()
        for r in resultado:
            r_list.append(r)

        return r_list

    def create_data(self):
        """
        crea la base de datos carro_maier
        si existe, la elimina
        """
        try:
            db_cacho = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=""
            )

            csr_cacho = db_cacho.cursor()

            try:
                sql_drop = "DROP DATABASE IF EXISTS carro_maier"
                sql_create = "CREATE DATABASE carro_maier"

                csr_cacho.execute(sql_drop)
                csr_cacho.execute(sql_create)

                db_cacho.commit()

            except Exception as e:
                db_cacho.rollback()
                raise Exception(f'Error al crear base de datos carro_maier: {str(e)}')

            finally:
                db_cacho.close()

        except Exception as e:
            raise Exception(f'error al abrir conexion: {str(e)}')

    def create_tables(self):
        """
        crea las tabla
        - noticias
        - medios
        - secciones
        si existe, la elimina
        las tablas medios y noticias se cargan con datos
        """
        try:
            db_cacho = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="carro_maier"
            )

            csr_cacho = db_cacho.cursor()

            try:
                sql_drop_noticias = """
                    DROP TABLE IF EXISTS `Noticias`;
                    """

                sql_drop_medios = """
                    DROP TABLE IF EXISTS `Medios`;
                    """

                sql_drop_secciones = """
                    DROP TABLE IF EXISTS `Secciones`;
                    """

                sql_create_noticias = """
                    CREATE TABLE `Noticias`(
                        Id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        Fecha DATE,
                        Medio INT(3) NOT NULL,
                        Seccion INT(3) NOT NULL,
                        Titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                        Cuerpo TEXT COLLATE utf8_spanish2_ci NOT NULL
                        );
                    """

                sql_create_medios = """
                    CREATE TABLE `Medios`(
                        Id INT(3) NOT NULL PRIMARY KEY,
                        Descripcion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL
                        );
                    """

                sql_create_secciones = """
                    CREATE TABLE `Secciones`(
                        Id INT(3) NOT NULL PRIMARY KEY,
                        IdMedio INT(3) NOT NULL,
                        Descripcion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL
                        );
                    """

                sql_populate_medios = """
                    INSERT INTO Medios(Id, Descripcion)
                        VALUES
                            (32, 'Ámbito Financiero'),
                            (36, 'BAE'),
                            (299, 'Buenos Aires Herald'),
                            (38, 'Clarín'),
                            (221, 'Página 12 Online');
                """

                sql_populate_secciones = """
                    INSERT INTO Secciones(Id, IdMedio, Descripcion)
                        VALUES
                            (145, 32, 'Ámbito Nacional'),
                            (411, 32, 'Cuerpo Principal'),
                            (80, 36, 'Política Económica'),
                            (81, 36, 'BAE inversor'),
                            (82, 36, 'Empresas & Negocios'),
                            (415, 299, 'Argentina'),
                            (422, 299, 'Day by Day'),
                            (93, 38, 'Sociedad'),
                            (94, 38, 'Cultura'),
                            (96, 38, 'Policiales'),
                            (871, 221, 'Supl. - Cash'),
                            (136, 221, 'Supl. - Las 12'),
                            (103, 221, 'Espectáculos');
                """

                csr_cacho.execute(sql_drop_noticias)
                csr_cacho.execute(sql_drop_medios)
                csr_cacho.execute(sql_drop_secciones)
                csr_cacho.execute(sql_create_noticias)
                csr_cacho.execute(sql_create_medios)
                csr_cacho.execute(sql_create_secciones)
                csr_cacho.execute(sql_populate_medios)
                csr_cacho.execute(sql_populate_secciones)

                db_cacho.commit()

            except Exception as e:
                db_cacho.rollback()
                raise Exception(f"error al crear tablas: {str(e)}")

            finally:
                db_cacho.close()

        except Exception as e:
            raise Exception(f"error al abrir base de datos carro_maier: {str(e)}")

    def save_data(self, noticia):
        """
        guarda una noticia
        """
        try:
            db_cacho = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="carro_maier"
                )

            try:
                csr_cacho = db_cacho.cursor()

                medio = re.sub("[\"']", r"", noticia.medio)
                seccion = re.sub("[\"']", r"", noticia.seccion)
                titulo = re.sub("[\"']", r"", noticia.titulo)
                cuerpo = re.sub("[\"']", r"", noticia.cuerpo)

                if noticia.id == "0":
                    sql_insert = """
                        INSERT INTO Noticias (Fecha, Medio, Seccion, Titulo, Cuerpo)
                            VALUES (%s, %s, %s, %s, %s)
                        """
                    datos = (noticia.fecha, medio, seccion, titulo, cuerpo)

                    csr_cacho.execute(sql_insert, datos)
                else:
                    sql_update = f"""
                        UPDATE Noticias SET
                            Fecha = '{noticia.fecha}',
                            Medio = '{medio}',
                            Seccion = '{seccion}',
                            Titulo = '{titulo}',
                            Cuerpo = '{cuerpo}'
                        WHERE Id = {noticia.id}
                        """
                    csr_cacho.execute(sql_update)

                db_cacho.commit()
                db_cacho.close()

            except Exception as e:
                db_cacho.rollback()
                db_cacho.close()
                raise Exception(f"error al {'insertar' if noticia.id == '0' else 'actualizar'} registro en tabla Noticias: {str(e)}")

        except Exception as e:
            raise Exception(f"error al abrir base de datos carro_maier: {str(e)}")

    def get_datos(self, search_id):
        """
        devuelve un registro según search_id
        si lo encuentra
        """
        try:
            db_cacho = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="carro_maier"
            )

            try:
                csr_cacho = db_cacho.cursor()
                sql_get = f"""
                    SELECT
                        Id
                        , Fecha
                        , Medio
                        , Seccion
                        , Titulo
                        , Cuerpo
                    FROM Noticias
                    WHERE Id = {search_id}
                    """

                csr_cacho.execute(sql_get)
                resultado = csr_cacho.fetchone()
                db_cacho.close()

                return resultado

            except Exception as e:
                db_cacho.close()
                raise Exception(f"error al leer registros en tabla Noticias: {str(e)}")

        except Exception as e:
            raise Exception(f"error al abrir base de datos carro_maier: {str(e)}")

    def delete_data(self, search_id):
        """
        elimina un registro según search_id
        si lo encuentra
        """
        try:
            db_cacho = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="carro_maier"
            )

            try:
                csr_cacho = db_cacho.cursor()
                sql_delete = f"""
                    DELETE FROM Noticias
                    WHERE Id = {search_id}
                    """
                csr_cacho.execute(sql_delete)
                db_cacho.commit()
                db_cacho.close()

            except Exception as e:
                db_cacho.rollback()
                db_cacho.close()
                raise Exception(f"error al eliminar registro en tabla Noticias: {str(e)}")

        except Exception as e:
            raise Exception(f"error al abrir base de datos carro_maier: {str(e)}")
