import os
from django.db import models


class Zq0010(models.Model):
    zq0_filial = models.CharField(max_length=2)
    zq0_cod = models.CharField(max_length=15)
    zq0_img = models.CharField(max_length=200)
    zq0_usuario = models.CharField(max_length=15)
    d_e_l_e_t_field = models.CharField(db_column='d_e_l_e_t_', max_length=1)
    r_e_c_n_o_field = models.BigIntegerField(db_column='r_e_c_n_o_', primary_key=True)
    r_e_c_d_e_l_field = models.BigIntegerField(db_column='r_e_c_d_e_l_')

    def delete(self, *args, **kwargs):
        image_path = self.zq0_img.rstrip()
        os.remove(image_path)
        super(Zq0010, self).delete(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'zq0010'


class Zq1010(models.Model):
    zq1_filial = models.CharField(max_length=2)
    zq1_cod = models.CharField(max_length=15)
    zq1_alg = models.CharField(max_length=30)
    zq1_confid = models.FloatField()
    zq1_dt = models.CharField(max_length=8)
    zq1_rec = models.CharField(max_length=1)
    zq1_fcod = models.CharField(max_length=15)
    d_e_l_e_t_field = models.CharField(db_column='d_e_l_e_t_', max_length=1)
    r_e_c_n_o_field = models.BigIntegerField(db_column='r_e_c_n_o_', primary_key=True)
    r_e_c_d_e_l_field = models.BigIntegerField(db_column='r_e_c_d_e_l_')

    def delete(self, *args, **kwargs):
        face_image = Zq0010.objects.get(zq0_cod=self.zq1_fcod)
        image_path = face_image.zq0_img.rstrip()
        os.remove(image_path)
        super(Zq1010, self).delete(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'zq1010'

    def __str__(self):
        return "{} {} {}".format(
            self.zq1_alg,
            self.zq1_confid,
            self.zq1_rec
        )
