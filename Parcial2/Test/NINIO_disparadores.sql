
            CREATE OR REPLACE TRIGGER NINIO_AFTER_INSERT
            AFTER INSERT ON NINIO
            FOR EACH ROW
            BEGIN
                INSERT INTO AUDITORIA (NOMBRE_TABLA_AFECTADA, USUARIO_ACTUAL, FECHA_HORA, DETALLE_ACCION)
                VALUES ('NINIO', USER, SYSTIMESTAMP,
                    'Inserto el nuevo dato con el ID: ' || :NEW.ID_NINIO);
            END;
            /
            CREATE OR REPLACE TRIGGER NINIO_AFTER_UPDATE
            AFTER UPDATE ON NINIO
            FOR EACH ROW
            BEGIN
                INSERT INTO AUDITORIA (NOMBRE_TABLA_AFECTADA, USUARIO_ACTUAL, FECHA_HORA, DETALLE_ACCION)
                VALUES ('NINIO', USER, SYSTIMESTAMP,
                    'Actualizo el dato con el ID: ' || :NEW.ID_NINIO);
            END;
            /
            CREATE OR REPLACE TRIGGER NINIO_AFTER_DELETE
            AFTER DELETE ON NINIO
            FOR EACH ROW
            BEGIN
                INSERT INTO AUDITORIA (NOMBRE_TABLA_AFECTADA, USUARIO_ACTUAL, FECHA_HORA, DETALLE_ACCION)
                VALUES ('NINIO', USER, SYSTIMESTAMP,
                    'Se eliminó la fila con el ID' || :OLD.ID_NINIO);
            END;
            /
            