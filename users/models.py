import os
from django.db import models


# Create your models here.
class Sra010(models.Model):
    ra_filial = models.CharField(max_length=2)
    ra_mat = models.CharField(max_length=6)
    ra_cc = models.CharField(max_length=9)
    ra_nome = models.CharField(max_length=30)
    ra_cic = models.CharField(max_length=11)
    ra_clvl = models.CharField(max_length=9)
    ra_item = models.CharField(max_length=9)
    ra_pis = models.CharField(max_length=12)
    ra_rg = models.CharField(max_length=15)
    ra_numcp = models.CharField(max_length=7)
    ra_sercp = models.CharField(max_length=5)
    ra_ufcp = models.CharField(max_length=2)
    ra_habilit = models.CharField(max_length=11)
    ra_reservi = models.CharField(max_length=12)
    ra_tituloe = models.CharField(max_length=12)
    ra_zonasec = models.CharField(max_length=8)
    ra_nomecmp = models.CharField(max_length=70)
    ra_enderec = models.CharField(max_length=30)
    ra_complem = models.CharField(max_length=15)
    ra_bairro = models.CharField(max_length=15)
    ra_municip = models.CharField(max_length=20)
    ra_estado = models.CharField(max_length=2)
    ra_cep = models.CharField(max_length=8)
    ra_telefon = models.CharField(max_length=20)
    ra_mae = models.CharField(max_length=40)
    ra_natural = models.CharField(max_length=2)
    ra_pai = models.CharField(max_length=40)
    ra_naciona = models.CharField(max_length=2)
    ra_sexo = models.CharField(max_length=1)
    ra_estcivi = models.CharField(max_length=1)
    ra_anocheg = models.CharField(max_length=2)
    ra_depir = models.CharField(max_length=2)
    ra_depsf = models.CharField(max_length=2)
    ra_nasc = models.CharField(max_length=8)
    ra_admissa = models.CharField(max_length=8)
    ra_altnasc = models.CharField(max_length=1)
    ra_opcao = models.CharField(max_length=8)
    ra_demissa = models.CharField(max_length=8)
    ra_vctoexp = models.CharField(max_length=8)
    ra_vctexp2 = models.CharField(max_length=8)
    ra_examedi = models.CharField(max_length=8)
    ra_bcdepsa = models.CharField(max_length=8)
    ra_ctdepsa = models.CharField(max_length=11)
    ra_bcdpfgt = models.CharField(max_length=8)
    ra_ctdpfgt = models.CharField(max_length=12)
    ra_sitfolh = models.CharField(max_length=1)
    ra_hrsmes = models.FloatField()
    ra_hrseman = models.FloatField()
    ra_chapa = models.CharField(max_length=5)
    ra_tnotrab = models.CharField(max_length=3)
    ra_codfunc = models.CharField(max_length=5)
    ra_cbo = models.CharField(max_length=5)
    ra_pgctsin = models.CharField(max_length=1)
    ra_sindica = models.CharField(max_length=2)
    ra_altcbo = models.CharField(max_length=1)
    ra_proces = models.CharField(max_length=5)
    ra_adtpose = models.CharField(max_length=6)
    ra_cestab = models.CharField(max_length=1)
    ra_valeref = models.CharField(max_length=2)
    ra_segurov = models.CharField(max_length=2)
    ra_pensali = models.FloatField()
    ra_percadt = models.FloatField()
    ra_catfunc = models.CharField(max_length=1)
    ra_tipopgt = models.CharField(max_length=1)
    ra_salario = models.FloatField()
    ra_anteaum = models.FloatField()
    ra_pericul = models.FloatField()
    ra_insmin = models.FloatField()
    ra_insmed = models.FloatField()
    ra_insmax = models.FloatField()
    ra_tipoadm = models.CharField(max_length=2)
    ra_afasfgt = models.CharField(max_length=1)
    ra_viemrai = models.CharField(max_length=2)
    ra_grinrai = models.CharField(max_length=2)
    ra_rescrai = models.CharField(max_length=2)
    ra_mestrab = models.CharField(max_length=2)
    ra_mesesan = models.FloatField()
    ra_altend = models.CharField(max_length=1)
    ra_altcp = models.CharField(max_length=1)
    ra_altpis = models.CharField(max_length=1)
    ra_altadm = models.CharField(max_length=1)
    ra_altopc = models.CharField(max_length=1)
    ra_altnome = models.CharField(max_length=1)
    ra_codret = models.CharField(max_length=4)
    ra_cracha = models.CharField(max_length=10)
    ra_regra = models.CharField(max_length=2)
    ra_bitmap = models.CharField(max_length=8)
    ra_categ = models.CharField(max_length=2)
    ra_seqturn = models.CharField(max_length=2)
    ra_senha = models.CharField(max_length=6)
    ra_registr = models.CharField(max_length=6)
    ra_ficha = models.CharField(max_length=8)
    ra_tpcontr = models.CharField(max_length=1)
    ra_nivel = models.CharField(max_length=2)
    ra_apelido = models.CharField(max_length=15)
    ra_tprcbt = models.CharField(max_length=1)
    ra_tcfmsg = models.CharField(max_length=6)
    ra_insssc = models.CharField(max_length=1)
    ra_classec = models.CharField(max_length=2)
    ra_ocorren = models.CharField(max_length=2)
    ra_percsat = models.FloatField()
    ra_distsn = models.CharField(max_length=1)
    ra_defifis = models.CharField(max_length=1)
    ra_bhfol = models.CharField(max_length=1)
    ra_rgorg = models.CharField(max_length=3)
    ra_brpdh = models.CharField(max_length=1)
    ra_acumbh = models.CharField(max_length=1)
    ra_racacor = models.CharField(max_length=1)
    ra_oktrans = models.CharField(max_length=2)
    ra_tabela = models.CharField(max_length=3)
    ra_tabnive = models.CharField(max_length=2)
    ra_tabfaix = models.CharField(max_length=2)
    ra_recmail = models.CharField(max_length=1)
    ra_recpfnc = models.CharField(max_length=1)
    ra_email = models.CharField(max_length=50)
    ra_perfgts = models.FloatField()
    ra_dtvtest = models.CharField(max_length=8)
    ra_tpmail = models.CharField(max_length=1)
    ra_codigo = models.CharField(max_length=14)
    ra_cargo = models.CharField(max_length=5)
    ra_codtit = models.CharField(max_length=2)
    ra_msblql = models.CharField(max_length=1)
    ra_posto = models.CharField(max_length=9)
    ra_tipamed = models.CharField(max_length=1)
    ra_asmedic = models.CharField(max_length=2)
    ra_dpassme = models.CharField(max_length=2)
    ra_tpasodo = models.CharField(max_length=1)
    ra_asodont = models.CharField(max_length=2)
    ra_chident = models.CharField(max_length=25)
    ra_dtcpexp = models.CharField(max_length=8)
    ra_dtrgexp = models.CharField(max_length=8)
    ra_tpdeffi = models.CharField(max_length=1)
    ra_rgexp = models.CharField(max_length=6)
    ra_rguf = models.CharField(max_length=2)
    ra_numinsc = models.CharField(max_length=11)
    ra_servico = models.CharField(max_length=60)
    ra_orgemrg = models.CharField(max_length=5)
    ra_depto = models.CharField(max_length=9)
    ra_codunic = models.CharField(max_length=30)
    ra_regime = models.CharField(max_length=1)
    ra_fwidm = models.CharField(max_length=34)
    ra_fecrei = models.CharField(max_length=8)
    ra_demiant = models.CharField(max_length=8)
    ra_assist = models.CharField(max_length=1)
    ra_confed = models.CharField(max_length=1)
    ra_mensind = models.CharField(max_length=1)
    ra_resext = models.CharField(max_length=1)
    ra_ftinsal = models.FloatField()
    ra_molest = models.CharField(max_length=8)
    ra_hoparc = models.CharField(max_length=1)
    ra_claures = models.CharField(max_length=1)
    ra_dtfimct = models.CharField(max_length=8)
    ra_compsab = models.CharField(max_length=1)
    ra_inssaut = models.CharField(max_length=1)
    ra_munnasc = models.CharField(max_length=30)
    ra_adctrf = models.FloatField()
    ra_tipende = models.CharField(max_length=1)
    ra_complrg = models.CharField(max_length=20)
    ra_secao = models.CharField(max_length=4)
    ra_datcheg = models.CharField(max_length=8)
    ra_numende = models.CharField(max_length=6)
    ra_cpostal = models.CharField(max_length=9)
    ra_cepcxpo = models.CharField(max_length=8)
    ra_dddfone = models.CharField(max_length=2)
    ra_dddcelu = models.CharField(max_length=2)
    ra_numcelu = models.CharField(max_length=10)
    ra_cpaisor = models.CharField(max_length=5)
    ra_adcconf = models.FloatField()
    ra_brnasex = models.CharField(max_length=1)
    ra_tipcert = models.CharField(max_length=1)
    ra_emicert = models.CharField(max_length=8)
    ra_matcert = models.CharField(max_length=32)
    ra_livcert = models.CharField(max_length=8)
    ra_folcert = models.CharField(max_length=4)
    ra_carcert = models.CharField(max_length=30)
    ra_ufcert = models.CharField(max_length=2)
    ra_cdmucer = models.CharField(max_length=5)
    ra_numepas = models.CharField(max_length=15)
    ra_emispas = models.CharField(max_length=15)
    ra_ufpas = models.CharField(max_length=2)
    ra_demipas = models.CharField(max_length=8)
    ra_dvalpas = models.CharField(max_length=8)
    ra_codpais = models.CharField(max_length=5)
    ra_numnatu = models.CharField(max_length=10)
    ra_datnatu = models.CharField(max_length=8)
    ra_numric = models.CharField(max_length=12)
    ra_emisric = models.CharField(max_length=10)
    ra_ufric = models.CharField(max_length=2)
    ra_cdmuric = models.CharField(max_length=5)
    ra_dexpric = models.CharField(max_length=8)
    ra_rhexp = models.CharField(max_length=6)
    ra_servent = models.CharField(max_length=6)
    ra_codacer = models.CharField(max_length=2)
    ra_regcivi = models.CharField(max_length=2)
    ra_tplivro = models.CharField(max_length=1)
    ra_paisext = models.CharField(max_length=5)
    ra_logrtp = models.CharField(max_length=4)
    ra_logrdsc = models.CharField(max_length=80)
    ra_logrnum = models.CharField(max_length=10)
    ra_codmun = models.CharField(max_length=5)
    ra_tpctsal = models.CharField(max_length=1)
    ra_nacionc = models.CharField(max_length=5)
    ra_tpprevi = models.CharField(max_length=1)
    ra_codmunn = models.CharField(max_length=9)
    ra_cnhorg = models.CharField(max_length=20)
    ra_dtemcnh = models.CharField(max_length=8)
    ra_dtvccnh = models.CharField(max_length=8)
    ra_email2 = models.CharField(max_length=60)
    ra_portdef = models.CharField(max_length=6)
    ra_obsdefi = models.TextField(blank=True, null=True)
    ra_catefd = models.CharField(max_length=3)
    ra_tpjorna = models.CharField(max_length=1)
    ra_eaposen = models.CharField(max_length=1)
    ra_njud14 = models.CharField(max_length=20)
    ra_tpreint = models.CharField(max_length=1)
    ra_nrproc = models.CharField(max_length=20)
    ra_nrleian = models.CharField(max_length=1)
    ra_dtefret = models.CharField(max_length=8)
    ra_dtefrtn = models.CharField(max_length=8)
    ra_rne = models.CharField(max_length=14)
    ra_rneorg = models.CharField(max_length=20)
    ra_rnedexp = models.CharField(max_length=8)
    ra_casadbr = models.CharField(max_length=1)
    ra_filhobr = models.CharField(max_length=1)
    ra_ocemis = models.CharField(max_length=20)
    ra_ocdtexp = models.CharField(max_length=8)
    ra_ocdtval = models.CharField(max_length=8)
    ra_locbnf = models.CharField(max_length=4)
    ra_valeali = models.CharField(max_length=2)
    ra_dtcaged = models.CharField(max_length=8)
    ra_autmei = models.CharField(max_length=1)
    ra_catcnh = models.CharField(max_length=1)
    ra_ufcnh = models.CharField(max_length=2)
    ra_clasest = models.CharField(max_length=2)
    ra_hojorva = models.CharField(max_length=1)
    r_e_c_d_e_l_field = models.IntegerField(db_column='r_e_c_d_e_l_')  # Field renamed because it ended with '_'.
    d_e_l_e_t_field = models.CharField(db_column='d_e_l_e_t_', max_length=1)  # Field renamed because it ended with '_'.
    r_e_c_n_o_field = models.IntegerField(db_column='r_e_c_n_o_', primary_key=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'sra010'
        unique_together = (('ra_filial', 'ra_mat', 'r_e_c_d_e_l_field'), ('ra_filial', 'ra_mat', 'r_e_c_d_e_l_field'),)


class Zq0010(models.Model):
    zq0_filial = models.CharField(max_length=2)
    zq0_cod = models.CharField(max_length=15)
    zq0_img = models.CharField(max_length=200)
    zq0_usuario = models.CharField(max_length=15)
    d_e_l_e_t_field = models.CharField(db_column='d_e_l_e_t_', max_length=1)  # Field renamed because it ended with '_'.
    r_e_c_n_o_field = models.BigIntegerField(db_column='r_e_c_n_o_', primary_key=True)  # Field renamed because it ended with '_'.
    r_e_c_d_e_l_field = models.BigIntegerField(db_column='r_e_c_d_e_l_')  # Field renamed because it ended with '_'.

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
    zq1_confid = models.BigIntegerField()
    zq1_dt = models.CharField(max_length=8)
    zq1_rec = models.CharField(max_length=1)
    zq1_fcod = models.CharField(max_length=15)
    d_e_l_e_t_field = models.CharField(db_column='d_e_l_e_t_', max_length=1)  # Field renamed because it ended with '_'.
    r_e_c_n_o_field = models.BigIntegerField(db_column='r_e_c_n_o_', primary_key=True)  # Field renamed because it ended with '_'.
    r_e_c_d_e_l_field = models.BigIntegerField(db_column='r_e_c_d_e_l_')  # Field renamed because it ended with '_'.

    def delete(self, *args, **kwargs):
        face_image = Zq0010.objects.get(zq0_cod=self.zq1_fcod)
        image_path = face_image.zq0_img.rstrip()
        os.remove(image_path)
        super(Zq1010, self).delete(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'zq1010'
