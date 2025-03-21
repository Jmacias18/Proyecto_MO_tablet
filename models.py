﻿# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Empleados(models.Model):
    codigo_emp = models.IntegerField(db_column='Codigo_Emp', primary_key=True)  # Field name and type updated.
    nombre_emp = models.CharField(db_column='Nombre_Emp', max_length=255)  # Field length updated.
    estado = models.CharField(db_column='Estado', max_length=1)  # New field added.
    id_departamento = models.IntegerField(db_column='ID_Departamento')  # New field added.
    id_puesto = models.IntegerField(db_column='ID_Puesto')  # New field added.
    id_turno = models.CharField(db_column='ID_Turno', max_length=10)  # New field added.
    id_supervisor = models.CharField(db_column='ID_Supervisor', max_length=10, blank=True, null=True)  # New field added.

    class Meta:
        managed = True
        db_table = 'Empleados'
    
    def __str__(self):
        return self.nombre_emp




class Horasprocesos(models.Model):
    id_hrspro = models.AutoField(db_column='ID_HrsProcesos', primary_key=True)
    fecha_hrspro = models.DateField(db_column='Fecha_HrsProcesos')
    codigo_emp = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Codigo_Emp', related_name='horasprocesos_horas')
    ID_Asis = models.CharField(db_column='ID_Asis', max_length=3, null=True, blank=True)  # Ajustar para almacenar el ID del tipo de inasistencia como cadena de texto
    id_pro = models.IntegerField(db_column='ID_Proceso', null=True, blank=True)
    horaentrada = models.TimeField(db_column='HoraEntrada', null=True, blank=True)
    horasalida = models.TimeField(db_column='HoraSalida', null=True, blank=True)
    hrs = models.FloatField(db_column='Hrs', null=True, blank=True)
    totalhrs = models.FloatField(db_column='TotalHrs', null=True, blank=True)
    hrsextras = models.FloatField(db_column='HrsExtras', null=True, blank=True)
    id_producto = models.CharField(max_length=10, null=True, blank=True)  # Ajustar a CharField
    autorizado = models.BooleanField(db_column='Autorizado')
    sync = models.BooleanField(db_column='SYNC')
    ucreado = models.CharField(db_column='UCreado', max_length=20, null=True, blank=True)  # Nueva columna UCreado
    umod = models.CharField(db_column='UMod', max_length=20, null=True, blank=True)  # Nueva columna UMod
    fmod = models.DateField(db_column='FMod', null=True)  # Nueva columna FMod
    class Meta:
        managed = True
        db_table = 'HorasProcesos'

class Procesos(models.Model):
    id_pro = models.IntegerField(db_column='ID_Pro', primary_key=True)  # Field name made lowercase.
    nombre_pro = models.CharField(db_column='Nombre_Pro', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado_pro = models.BooleanField(db_column='Estado_Pro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Procesos'