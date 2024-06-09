/*==============================================================*/
/* DBMS name:      ORACLE Version 19c                           */
/* Created on:     07/06/2024 16:38:51                          */
/*==============================================================*/


alter table ACTIVIDAD
   drop constraint FK_ACTIVIDA_PERTENECE_PROGRAMA;

alter table EMPLEA
   drop constraint FK_EMPLEA_EMPLEA2_ACTIVIDA;

alter table EMPLEA
   drop constraint FK_EMPLEA_EMPLEA_MATERIAL;

alter table ESTADO_SALUD
   drop constraint FK_ESTADO_S_POSEE_NINIO;

alter table MATRICULA
   drop constraint FK_MATRICUL_RELATIONS_ANO_LECT;

alter table MATRICULA
   drop constraint FK_MATRICUL_RELATIONS_NINIO;

alter table NINIO
   drop constraint FK_NINIO_POSEE_UN__GENERO;

alter table NINIO
   drop constraint FK_NINIO_PRESENTAN_TALLA_ZA;

alter table NINIO
   drop constraint FK_NINIO_PRESENTA__TALLA_VE;

alter table NINIO
   drop constraint FK_NINIO_TIENEN_NA_NACIONAL;

alter table PADRE
   drop constraint FK_PADRE_POSEE_UNA_NACIONAL;

alter table PADRE
   drop constraint FK_PADRE_POSEE_UN__GENERO;

alter table PROFESIONAL
   drop constraint FK_PROFESIO_POSEE_UN__GENERO;

alter table PROFESIONAL
   drop constraint FK_PROFESIO_PROPONE_ACTIVIDA;

alter table PROFESIONAL
   drop constraint FK_PROFESIO_TIENE_MAC_NACIONAL;

alter table PROGRAMA
   drop constraint FK_PROGRAMA_RELATIONS_ANO_LECT;

alter table RELACION_PADRE_NINIO
   drop constraint FK_RELATION_RELATIONS_NINIO;

alter table RELACION_PADRE_NINIO
   drop constraint FK_RELATION_RELATIONS_PADRE;

alter table RENDIMIENTO
   drop constraint FK_RENDIMIE_RELATIONS_ACTIVIDA;

alter table RENDIMIENTO
   drop constraint FK_RENDIMIE_RELATIONS_NINIO;

alter table RENDIMIENTO
   drop constraint FK_RENDIMIE_RELATIONS_TIPO_REN;

alter table SALUD_ALERGIAS_RELATION
   drop constraint FK_SALUD_AL_SALUD_ALE_ALERGIAS;

alter table SALUD_ALERGIAS_RELATION
   drop constraint FK_SALUD_AL_SALUD_ALE_ESTADO_S;

alter table SALUD_MEDICAMENT_RELATION
   drop constraint FK_SALUD_ME_SALUD_MED_ESTADO_S;

alter table SALUD_MEDICAMENT_RELATION
   drop constraint FK_SALUD_ME_SALUD_MED_MEDICAME;

alter table TUTOR
   drop constraint FK_TUTOR_MANTIENE__RELACION;

alter table TUTOR
   drop constraint FK_TUTOR_POSEE_UN__GENERO;

alter table TUTOR
   drop constraint FK_TUTOR_TIENEN_NA_NACIONAL;

alter table TUTORES_NINIOS_RELATION
   drop constraint FK_TUTORES__TUTORES_N_NINIO;

alter table TUTORES_NINIOS_RELATION
   drop constraint FK_TUTORES__TUTORES_N_TUTOR;

drop index PERTENECE_FK;

drop table ACTIVIDAD cascade constraints;

drop table ALERGIAS cascade constraints;

drop table ANO_LECTIVO cascade constraints;

drop index EMPLEA_FK;

drop index EMPLEA2_FK;

drop table EMPLEA cascade constraints;

drop index POSEE_FK;

drop table ESTADO_SALUD cascade constraints;

drop table GENERO cascade constraints;

drop table MATERIAL cascade constraints;

drop index RELATIONSHIP_30_FK;

drop index RELATIONSHIP_24_FK;

drop table MATRICULA cascade constraints;

drop table MEDICAMENTO cascade constraints;

drop table NACIONALIDAD cascade constraints;

drop index PRESENTA_UNA_FK;

drop index PRESENTAN_UNA_FK;

drop index POSEE_UN_GENERO_FK;

drop index TIENEN_NACIONALIDAD_FK;

drop table NINIO cascade constraints;

drop index POSEE_UNA_NACIONALIDAD___FK;

drop index POSEE_UN_GENERO___FK;

drop table PADRE cascade constraints;

drop index TIENE_MACIONALIDAD_FK;

drop index POSEE_UN_GENEROO_FK;

drop index PROPONE_FK;

drop table PROFESIONAL cascade constraints;

drop index RELATIONSHIP_29_FK;

drop table PROGRAMA cascade constraints;

drop table RELACION cascade constraints;

drop index RELATIONSHIP_15_FK;

drop index RELATIONSHIP_16_FK;

drop table RELACION_PADRE_NINIO cascade constraints;

drop index RELATIONSHIP_31_FK;

drop index RELATIONSHIP_23_FK;

drop index RELATIONSHIP_21_FK;

drop table RENDIMIENTO cascade constraints;

drop index SALUD_ALERGIAS_RELATION_FK;

drop index SALUD_ALERGIAS_RELATION2_FK;

drop table SALUD_ALERGIAS_RELATION cascade constraints;

drop index SALUD_MEDICAMENT_RELATION_FK;

drop index SALUD_MEDICAMENT_RELATION2_FK;

drop table SALUD_MEDICAMENT_RELATION cascade constraints;

drop table TALLA_VESTIMENTA cascade constraints;

drop table TALLA_ZAPATO cascade constraints;

drop table TIPO_RENDIMIENTO cascade constraints;

drop index MANTIENE_UNA_RELACION_DE_FK;

drop index POSEE_UN_GENERO__FK;

drop index TIENEN_NACIONALIDAD__FK;

drop table TUTOR cascade constraints;

drop index TUTORES_NINIOS_RELATION_FK;

drop index TUTORES_NINIOS_RELATION2_FK;

drop table TUTORES_NINIOS_RELATION cascade constraints;

/*==============================================================*/
/* Table: ACTIVIDAD                                             */
/*==============================================================*/
create table ACTIVIDAD (
   ID_ACTIVIDAD         NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   ID_PROGRAMA          INTEGER               not null,
   NOMBRE_AVTIVI        VARCHAR2(60)          not null,
   DESCRIPCION_ACTIVI   VARCHAR2(300)           not null,
   DURACION_ACTIVI      INTEGER               not null,
   FINALIZADO           VARCHAR(5)              not null,
   constraint PK_ACTIVIDAD primary key (ID_ACTIVIDAD)
);

/*==============================================================*/
/* Index: PERTENECE_FK                                          */
/*==============================================================*/
create index PERTENECE_FK on ACTIVIDAD (
   ID_PROGRAMA ASC
);

/*==============================================================*/
/* Table: ALERGIAS                                              */
/*==============================================================*/
create table ALERGIAS (
   ID_ALERGIA           NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   NOMBRE_ALERGIA       VARCHAR2(30)          not null,
   constraint PK_ALERGIAS primary key (ID_ALERGIA)
);

/*==============================================================*/
/* Table: ANO_LECTIVO                                           */
/*==============================================================*/
create table ANO_LECTIVO (
   ID_ANO_LECTIVO       NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   ANO                  VARCHAR2(4)           not null,
   constraint PK_ANO_LECTIVO primary key (ID_ANO_LECTIVO)
);

/*==============================================================*/
/* Table: EMPLEA                                                */
/*==============================================================*/
create table EMPLEA (
   ID_MATERIAL          INTEGER               not null,
   ID_ACTIVIDAD         INTEGER               not null,
   constraint PK_EMPLEA primary key (ID_MATERIAL, ID_ACTIVIDAD)
);

/*==============================================================*/
/* Index: EMPLEA2_FK                                            */
/*==============================================================*/
create index EMPLEA2_FK on EMPLEA (
   ID_ACTIVIDAD ASC
);

/*==============================================================*/
/* Index: EMPLEA_FK                                             */
/*==============================================================*/
create index EMPLEA_FK on EMPLEA (
   ID_MATERIAL ASC
);

/*==============================================================*/
/* Table: ESTADO_SALUD                                          */
/*==============================================================*/
create table ESTADO_SALUD (
   ID_SALUD_STAT        NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   ID_NINIO             INTEGER               not null,
   ULTIMA_FECHA_ENFERMO VARCHAR(60)                  not null,
   DIAGNOSTICO          VARCHAR2(300),
   DOCTOR_TRATANTE      VARCHAR2(60),
   constraint PK_ESTADO_SALUD primary key (ID_SALUD_STAT)
);

/*==============================================================*/
/* Index: POSEE_FK                                              */
/*==============================================================*/
create index POSEE_FK on ESTADO_SALUD (
   ID_NINIO ASC
);

/*==============================================================*/
/* Table: GENERO                                                */
/*==============================================================*/
create table GENERO (
   ID_GENERO            NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   NOMBRE_GENERO        VARCHAR2(30)          not null,
   constraint PK_GENERO primary key (ID_GENERO)
);

/*==============================================================*/
/* Table: MATERIAL                                              */
/*==============================================================*/
create table MATERIAL (
   ID_MATERIAL          NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   NOMBRE_MATERIAL      VARCHAR2(30),
   constraint PK_MATERIAL primary key (ID_MATERIAL)
);

/*==============================================================*/
/* Table: MATRICULA                                             */
/*==============================================================*/
create table MATRICULA (
   ID_MATRICULA         NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   ID_NINIO             INTEGER               not null,
   ID_ANO_LECTIVO       INTEGER               not null,
   PRECIO_MATRICULA     INTEGER               not null,
   constraint PK_MATRICULA primary key (ID_MATRICULA)
);

/*==============================================================*/
/* Index: RELATIONSHIP_24_FK                                    */
/*==============================================================*/
create index RELATIONSHIP_24_FK on MATRICULA (
   ID_NINIO ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_30_FK                                    */
/*==============================================================*/
create index RELATIONSHIP_30_FK on MATRICULA (
   ID_ANO_LECTIVO ASC
);

/*==============================================================*/
/* Table: MEDICAMENTO                                           */
/*==============================================================*/
create table MEDICAMENTO (
   ID_MEDICAMENTO       NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   NOMBRE_MEDICAMENTO   VARCHAR2(30)          not null,
   DESCRIPTION_MEDICAMENTO VARCHAR2(300)           not null,
   constraint PK_MEDICAMENTO primary key (ID_MEDICAMENTO)
);

/*==============================================================*/
/* Table: NACIONALIDAD                                          */
/*==============================================================*/
create table NACIONALIDAD (
   ID_NACIONALIDAD      NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   NOMBRE_NACIONALIDAD  VARCHAR2(30)          not null,
   constraint PK_NACIONALIDAD primary key (ID_NACIONALIDAD)
);

/*==============================================================*/
/* Table: NINIO                                                 */
/*==============================================================*/
create table NINIO (
   ID_NINIO             NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   ID_NACIONALIDAD      INTEGER               not null,
   ID_GENERO            INTEGER               not null,
   ID_TALLA_ZAPATO      INTEGER               not null,
   ID_TALLA_VESTIMENTA  INTEGER               not null,
   CI_NINIO             VARCHAR2(10)          not null,
   NOMBRE_NINIO         VARCHAR2(30)          not null,
   APELLIDO_NINIO       VARCHAR2(30)          not null,
   NACIMIENTO_DATE      VARCHAR(30)                  not null,
   ESTADO_MATRICULA     VARCHAR(5)              not null,
   constraint PK_NINIO primary key (ID_NINIO)
);

/*==============================================================*/
/* Index: TIENEN_NACIONALIDAD_FK                                */
/*==============================================================*/
create index TIENEN_NACIONALIDAD_FK on NINIO (
   ID_NACIONALIDAD ASC
);

/*==============================================================*/
/* Index: POSEE_UN_GENERO_FK                                    */
/*==============================================================*/
create index POSEE_UN_GENERO_FK on NINIO (
   ID_GENERO ASC
);

/*==============================================================*/
/* Index: PRESENTAN_UNA_FK                                      */
/*==============================================================*/
create index PRESENTAN_UNA_FK on NINIO (
   ID_TALLA_ZAPATO ASC
);

/*==============================================================*/
/* Index: PRESENTA_UNA_FK                                       */
/*==============================================================*/
create index PRESENTA_UNA_FK on NINIO (
   ID_TALLA_VESTIMENTA ASC
);

/*==============================================================*/
/* Table: PADRE                                                 */
/*==============================================================*/
create table PADRE (
   ID_PADRE             NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   ID_GENERO            INTEGER               not null,
   ID_NACIONALIDAD      INTEGER               not null,
   NOMBRE_PADRE         VARCHAR2(30)          not null,
   APELLIDO_PADRE       VARCHAR2(30)          not null,
   CI_PADRE             VARCHAR2(10)          not null,
   DIRECCION_PADRE      VARCHAR2(30)          not null,
   TELEFONO_PADRE       VARCHAR2(10)          not null,
   DOMICILIO_PADRE      VARCHAR2(30)          not null,
   constraint PK_PADRE primary key (ID_PADRE)
);

/*==============================================================*/
/* Index: POSEE_UN_GENERO___FK                                  */
/*==============================================================*/
create index POSEE_UN_GENERO___FK on PADRE (
   ID_GENERO ASC
);

/*==============================================================*/
/* Index: POSEE_UNA_NACIONALIDAD___FK                           */
/*==============================================================*/
create index POSEE_UNA_NACIONALIDAD___FK on PADRE (
   ID_NACIONALIDAD ASC
);

/*==============================================================*/
/* Table: PROFESIONAL                                           */
/*==============================================================*/
create table PROFESIONAL (
   ID_PROF              NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   ID_ACTIVIDAD         INTEGER               not null,
   ID_GENERO            INTEGER               not null,
   ID_NACIONALIDAD      INTEGER               not null,
   NOMBRES_PROF         VARCHAR2(30)          not null,
   APELLIDOS_PROF       VARCHAR2(30)          not null,
   CI_PROF              VARCHAR2(10)          not null,
   DIRECCION_PROF       VARCHAR2(60)          not null,
   TELEFONO_PROF        VARCHAR2(10)          not null,
   NO_CERTIFI_SENECYT   CHAR(15)              not null,
   constraint PK_PROFESIONAL primary key (ID_PROF)
);

/*==============================================================*/
/* Index: PROPONE_FK                                            */
/*==============================================================*/
create index PROPONE_FK on PROFESIONAL (
   ID_ACTIVIDAD ASC
);

/*==============================================================*/
/* Index: POSEE_UN_GENEROO_FK                                   */
/*==============================================================*/
create index POSEE_UN_GENEROO_FK on PROFESIONAL (
   ID_GENERO ASC
);

/*==============================================================*/
/* Index: TIENE_MACIONALIDAD_FK                                 */
/*==============================================================*/
create index TIENE_MACIONALIDAD_FK on PROFESIONAL (
   ID_NACIONALIDAD ASC
);

/*==============================================================*/
/* Table: PROGRAMA                                              */
/*==============================================================*/
create table PROGRAMA (
   ID_PROGRAMA          NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   ID_ANO_LECTIVO       INTEGER               not null,
   NOMBRE_PROGRAMA      VARCHAR2(60)          not null,
   constraint PK_PROGRAMA primary key (ID_PROGRAMA)
);

/*==============================================================*/
/* Index: RELATIONSHIP_29_FK                                    */
/*==============================================================*/
create index RELATIONSHIP_29_FK on PROGRAMA (
   ID_ANO_LECTIVO ASC
);

/*==============================================================*/
/* Table: RELACION                                              */
/*==============================================================*/
create table RELACION (
   ID_PARENTESCO        NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   NOMBRE_PARENTESCO    VARCHAR2(30)          not null,
   constraint PK_RELACION primary key (ID_PARENTESCO)
);

/*==============================================================*/
/* Table: RELACION_PADRE_NINIO                                  */
/*==============================================================*/
create table RELACION_PADRE_NINIO (
   ID_PADRE             INTEGER               not null,
   ID_NINIO             INTEGER               not null,
   constraint PK_RELATIONSHIP_15 primary key (ID_PADRE, ID_NINIO)
);

/*==============================================================*/
/* Index: RELATIONSHIP_16_FK                                    */
/*==============================================================*/
create index RELATIONSHIP_16_FK on RELACION_PADRE_NINIO (
   ID_NINIO ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_15_FK                                    */
/*==============================================================*/
create index RELATIONSHIP_15_FK on RELACION_PADRE_NINIO (
   ID_PADRE ASC
);

/*==============================================================*/
/* Table: RENDIMIENTO                                           */
/*==============================================================*/
create table RENDIMIENTO (
   ID_RENDIMIENTO       NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   ID_ACTIVIDAD         INTEGER               not null,
   ID_TIPO_RENDIMIENT   INTEGER               not null,
   ID_NINIO             INTEGER               not null,
   OBSERVACIONES        VARCHAR2(300)           not null,
   constraint PK_RENDIMIENTO primary key (ID_RENDIMIENTO)
);

/*==============================================================*/
/* Index: RELATIONSHIP_21_FK                                    */
/*==============================================================*/
create index RELATIONSHIP_21_FK on RENDIMIENTO (
   ID_ACTIVIDAD ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_23_FK                                    */
/*==============================================================*/
create index RELATIONSHIP_23_FK on RENDIMIENTO (
   ID_TIPO_RENDIMIENT ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_31_FK                                    */
/*==============================================================*/
create index RELATIONSHIP_31_FK on RENDIMIENTO (
   ID_NINIO ASC
);

/*==============================================================*/
/* Table: SALUD_ALERGIAS_RELATION                               */
/*==============================================================*/
create table SALUD_ALERGIAS_RELATION (
   ID_ALERGIA           INTEGER               not null,
   ID_SALUD_STAT        INTEGER               not null,
   constraint PK_SALUD_ALERGIAS_RELATION primary key (ID_ALERGIA, ID_SALUD_STAT)
);

/*==============================================================*/
/* Index: SALUD_ALERGIAS_RELATION2_FK                           */
/*==============================================================*/
create index SALUD_ALERGIAS_RELATION2_FK on SALUD_ALERGIAS_RELATION (
   ID_SALUD_STAT ASC
);

/*==============================================================*/
/* Index: SALUD_ALERGIAS_RELATION_FK                            */
/*==============================================================*/
create index SALUD_ALERGIAS_RELATION_FK on SALUD_ALERGIAS_RELATION (
   ID_ALERGIA ASC
);

/*==============================================================*/
/* Table: SALUD_MEDICAMENT_RELATION                             */
/*==============================================================*/
create table SALUD_MEDICAMENT_RELATION (
   ID_MEDICAMENTO       INTEGER               not null,
   ID_SALUD_STAT        INTEGER               not null,
   constraint PK_SALUD_MEDICAMENT_RELATION primary key (ID_MEDICAMENTO, ID_SALUD_STAT)
);

/*==============================================================*/
/* Index: SALUD_MEDICAMENT_RELATION2_FK                         */
/*==============================================================*/
create index SALUD_MEDICAMENT_RELATION2_FK on SALUD_MEDICAMENT_RELATION (
   ID_SALUD_STAT ASC
);

/*==============================================================*/
/* Index: SALUD_MEDICAMENT_RELATION_FK                          */
/*==============================================================*/
create index SALUD_MEDICAMENT_RELATION_FK on SALUD_MEDICAMENT_RELATION (
   ID_MEDICAMENTO ASC
);

/*==============================================================*/
/* Table: TALLA_VESTIMENTA                                      */
/*==============================================================*/
create table TALLA_VESTIMENTA (
   ID_TALLA_VESTIMENTA  NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   NUMERO_TALLA         NUMBER(4)             not null,
   constraint PK_TALLA_VESTIMENTA primary key (ID_TALLA_VESTIMENTA)
);

/*==============================================================*/
/* Table: TALLA_ZAPATO                                          */
/*==============================================================*/
create table TALLA_ZAPATO (
   ID_TALLA_ZAPATO      NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   NUMERO_TALLA         NUMBER(4)             not null,
   constraint PK_TALLA_ZAPATO primary key (ID_TALLA_ZAPATO)
);

/*==============================================================*/
/* Table: TIPO_RENDIMIENTO                                      */
/*==============================================================*/
create table TIPO_RENDIMIENTO (
   ID_TIPO_RENDIMIENT   NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   NOMBRE_RENDIMIENT    VARCHAR2(20)          not null,
   constraint PK_TIPO_RENDIMIENTO primary key (ID_TIPO_RENDIMIENT)
);

/*==============================================================*/
/* Table: TUTOR                                                 */
/*==============================================================*/
create table TUTOR (
   ID_TUTOR             NUMBER(6)           
      generated as identity ( start with 1 nocycle noorder)  not null,
   ID_NACIONALIDAD      INTEGER               not null,
   ID_GENERO            INTEGER               not null,
   ID_PARENTESCO        INTEGER               not null,
   NOMBRE_TUTOR         VARCHAR2(30)          not null,
   APELLIDO_TUTOR       VARCHAR2(30)          not null,
   CI_TUTOR             VARCHAR2(10)          not null,
   DIRECCION_TUTOR      VARCHAR2(30)          not null,
   TELEFONO_TUTOR       VARCHAR2(10)          not null,
   DOMICILIO_TUTOR      VARCHAR2(30)          not null,
   MOTIVO               VARCHAR2(300),
   constraint PK_TUTOR primary key (ID_TUTOR)
);

/*==============================================================*/
/* Index: TIENEN_NACIONALIDAD__FK                               */
/*==============================================================*/
create index TIENEN_NACIONALIDAD__FK on TUTOR (
   ID_NACIONALIDAD ASC
);

/*==============================================================*/
/* Index: POSEE_UN_GENERO__FK                                   */
/*==============================================================*/
create index POSEE_UN_GENERO__FK on TUTOR (
   ID_GENERO ASC
);

/*==============================================================*/
/* Index: MANTIENE_UNA_RELACION_DE_FK                           */
/*==============================================================*/
create index MANTIENE_UNA_RELACION_DE_FK on TUTOR (
   ID_PARENTESCO ASC
);

/*==============================================================*/
/* Table: TUTORES_NINIOS_RELATION                               */
/*==============================================================*/
create table TUTORES_NINIOS_RELATION (
   ID_NINIO             INTEGER               not null,
   ID_TUTOR             INTEGER               not null,
   constraint PK_TUTORES_NINIOS_RELATION primary key (ID_NINIO, ID_TUTOR)
);

/*==============================================================*/
/* Index: TUTORES_NINIOS_RELATION2_FK                           */
/*==============================================================*/
create index TUTORES_NINIOS_RELATION2_FK on TUTORES_NINIOS_RELATION (
   ID_TUTOR ASC
);

/*==============================================================*/
/* Index: TUTORES_NINIOS_RELATION_FK                            */
/*==============================================================*/
create index TUTORES_NINIOS_RELATION_FK on TUTORES_NINIOS_RELATION (
   ID_NINIO ASC
);

alter table ACTIVIDAD
   add constraint FK_ACTIVIDA_PERTENECE_PROGRAMA foreign key (ID_PROGRAMA)
      references PROGRAMA (ID_PROGRAMA);

alter table EMPLEA
   add constraint FK_EMPLEA_EMPLEA2_ACTIVIDA foreign key (ID_ACTIVIDAD)
      references ACTIVIDAD (ID_ACTIVIDAD);

alter table EMPLEA
   add constraint FK_EMPLEA_EMPLEA_MATERIAL foreign key (ID_MATERIAL)
      references MATERIAL (ID_MATERIAL);

alter table ESTADO_SALUD
   add constraint FK_ESTADO_S_POSEE_NINIO foreign key (ID_NINIO)
      references NINIO (ID_NINIO);

alter table MATRICULA
   add constraint FK_MATRICUL_RELATIONS_ANO_LECT foreign key (ID_ANO_LECTIVO)
      references ANO_LECTIVO (ID_ANO_LECTIVO);

alter table MATRICULA
   add constraint FK_MATRICUL_RELATIONS_NINIO foreign key (ID_NINIO)
      references NINIO (ID_NINIO);

alter table NINIO
   add constraint FK_NINIO_POSEE_UN__GENERO foreign key (ID_GENERO)
      references GENERO (ID_GENERO);

alter table NINIO
   add constraint FK_NINIO_PRESENTAN_TALLA_ZA foreign key (ID_TALLA_ZAPATO)
      references TALLA_ZAPATO (ID_TALLA_ZAPATO);

alter table NINIO
   add constraint FK_NINIO_PRESENTA__TALLA_VE foreign key (ID_TALLA_VESTIMENTA)
      references TALLA_VESTIMENTA (ID_TALLA_VESTIMENTA);

alter table NINIO
   add constraint FK_NINIO_TIENEN_NA_NACIONAL foreign key (ID_NACIONALIDAD)
      references NACIONALIDAD (ID_NACIONALIDAD);

alter table PADRE
   add constraint FK_PADRE_POSEE_UNA_NACIONAL foreign key (ID_NACIONALIDAD)
      references NACIONALIDAD (ID_NACIONALIDAD);

alter table PADRE
   add constraint FK_PADRE_POSEE_UN__GENERO foreign key (ID_GENERO)
      references GENERO (ID_GENERO);

alter table PROFESIONAL
   add constraint FK_PROFESIO_POSEE_UN__GENERO foreign key (ID_GENERO)
      references GENERO (ID_GENERO);

alter table PROFESIONAL
   add constraint FK_PROFESIO_PROPONE_ACTIVIDA foreign key (ID_ACTIVIDAD)
      references ACTIVIDAD (ID_ACTIVIDAD);

alter table PROFESIONAL
   add constraint FK_PROFESIO_TIENE_MAC_NACIONAL foreign key (ID_NACIONALIDAD)
      references NACIONALIDAD (ID_NACIONALIDAD);

alter table PROGRAMA
   add constraint FK_PROGRAMA_RELATIONS_ANO_LECT foreign key (ID_ANO_LECTIVO)
      references ANO_LECTIVO (ID_ANO_LECTIVO);

alter table RELACION_PADRE_NINIO
   add constraint FK_RELATION_RELATIONS_NINIO foreign key (ID_NINIO)
      references NINIO (ID_NINIO);

alter table RELACION_PADRE_NINIO
   add constraint FK_RELATION_RELATIONS_PADRE foreign key (ID_PADRE)
      references PADRE (ID_PADRE);

alter table RENDIMIENTO
   add constraint FK_RENDIMIE_RELATIONS_ACTIVIDA foreign key (ID_ACTIVIDAD)
      references ACTIVIDAD (ID_ACTIVIDAD);

alter table RENDIMIENTO
   add constraint FK_RENDIMIE_RELATIONS_NINIO foreign key (ID_NINIO)
      references NINIO (ID_NINIO);

alter table RENDIMIENTO
   add constraint FK_RENDIMIE_RELATIONS_TIPO_REN foreign key (ID_TIPO_RENDIMIENT)
      references TIPO_RENDIMIENTO (ID_TIPO_RENDIMIENT);

alter table SALUD_ALERGIAS_RELATION
   add constraint FK_SALUD_AL_SALUD_ALE_ALERGIAS foreign key (ID_ALERGIA)
      references ALERGIAS (ID_ALERGIA);

alter table SALUD_ALERGIAS_RELATION
   add constraint FK_SALUD_AL_SALUD_ALE_ESTADO_S foreign key (ID_SALUD_STAT)
      references ESTADO_SALUD (ID_SALUD_STAT);

alter table SALUD_MEDICAMENT_RELATION
   add constraint FK_SALUD_ME_SALUD_MED_ESTADO_S foreign key (ID_SALUD_STAT)
      references ESTADO_SALUD (ID_SALUD_STAT);

alter table SALUD_MEDICAMENT_RELATION
   add constraint FK_SALUD_ME_SALUD_MED_MEDICAME foreign key (ID_MEDICAMENTO)
      references MEDICAMENTO (ID_MEDICAMENTO);

alter table TUTOR
   add constraint FK_TUTOR_MANTIENE__RELACION foreign key (ID_PARENTESCO)
      references RELACION (ID_PARENTESCO);

alter table TUTOR
   add constraint FK_TUTOR_POSEE_UN__GENERO foreign key (ID_GENERO)
      references GENERO (ID_GENERO);

alter table TUTOR
   add constraint FK_TUTOR_TIENEN_NA_NACIONAL foreign key (ID_NACIONALIDAD)
      references NACIONALIDAD (ID_NACIONALIDAD);

alter table TUTORES_NINIOS_RELATION
   add constraint FK_TUTORES__TUTORES_N_NINIO foreign key (ID_NINIO)
      references NINIO (ID_NINIO);

alter table TUTORES_NINIOS_RELATION
   add constraint FK_TUTORES__TUTORES_N_TUTOR foreign key (ID_TUTOR)
      references TUTOR (ID_TUTOR);

