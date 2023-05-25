from django.db import models
from django.core.exceptions import MultipleObjectsReturned

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    atribut = models.TextField(default='')
    serv = models.TextField(default='')
    unid = models.TextField(default='')


class Tryacess(models.Model):
    name = models.CharField(max_length=100)
    login_try = models.PositiveIntegerField(default=0)

class Solicitado(models.Model):
    id_registro	 = models.CharField(max_length=10000)
    id_pdf	 = models.CharField(max_length=10000)
    municipio	 = models.CharField(max_length=10000)
    regiÃo	 = models.CharField(max_length=10000)
    unidade_solicitante	 = models.CharField(max_length=10000)
    unidade_requerente	 = models.CharField(max_length=10000)
    telefone	 = models.CharField(max_length=10000)
    mÉdico_solicitante	 = models.CharField(max_length=10000)
    cns	 = models.CharField(max_length=10000)
    nome	 = models.CharField(max_length=10000)
    data_de_nascimento	 = models.CharField(max_length=10000)
    idade	 = models.CharField(max_length=10000)
    sexo	 = models.CharField(max_length=10000)
    nome_da_mÃe	 = models.CharField(max_length=10000)
    nome_do_acompanhante	 = models.CharField(max_length=10000)
    telefone_do_acompanhante	 = models.CharField(max_length=10000)
    endereÇo	 = models.CharField(max_length=10000)
    municÍpio_de_procedÊncia	 = models.CharField(max_length=10000)
    data_de_admissÃo_na_unidade_solicitante	 = models.CharField(max_length=10000)
    hora_de_admissÃo_na_unidade_solicitante	 = models.CharField(max_length=10000)
    pressÃo_arterial	 = models.CharField(max_length=10000)
    frequÊncia_cardÍaca	 = models.CharField(max_length=10000)
    frequÊncia_respiratÓria	 = models.CharField(max_length=10000)
    glicemia	 = models.CharField(max_length=10000)
    temperatura	 = models.CharField(max_length=10000)
    escala_de_glasgow	 = models.CharField(max_length=10000)
    saturaÇÃo	 = models.CharField(max_length=10000)
    oxigenoterapia	 = models.CharField(max_length=10000)
    fluxo_de_o2_parÂmetros_ventilatÓrios	 = models.CharField(max_length=10000)
    comorbidades	 = models.CharField(max_length=10000)
    hd_diagnÓstico	 = models.CharField(max_length=10000)
    histÓrico_clÍnico	 = models.CharField(max_length=10000)
    exame_fÍsico	 = models.CharField(max_length=10000)
    medicaÇÕes	 = models.CharField(max_length=10000)
    drogas_vasoativas_dvas	 = models.CharField(max_length=10000)
    exames_complementares	 = models.CharField(max_length=10000)
    observaÇÕes	 = models.CharField(max_length=10000)
    ecg	 = models.CharField(max_length=10000)
    exame_de_imagem	 = models.CharField(max_length=10000)
    arquivo_de_exames	 = models.CharField(max_length=10000)
    tipo_de_leito_solicitado	 = models.CharField(max_length=10000)
    especialidade	 = models.CharField(max_length=10000)
    situaÇÃo	 = models.CharField(max_length=10000)
    motivo_de_desistÊncia	 = models.CharField(max_length=10000)
    aceita_servidor	 = models.CharField(max_length=10000)
    aceita_medico_regulador	 = models.CharField(max_length=10000)
    carimbo_aceita_medico	 = models.CharField(max_length=10000)
    mÉdico_regulador	 = models.CharField(max_length=10000)
    registro_do_mÉdico_regulador	 = models.CharField(max_length=10000)
    destino_da_regulaÇÃo	 = models.CharField(max_length=10000)
    setor	 = models.CharField(max_length=10000)
    tipo_de_leito	 = models.CharField(max_length=10000)
    leito	 = models.CharField(max_length=10000)
    motivo_para_fila_de_espera	 = models.CharField(max_length=10000)
    unidade_executante	 = models.CharField(max_length=10000)
    mÉdico_responsÁvel	 = models.CharField(max_length=10000)
    crm	 = models.CharField(max_length=10000)
    contato_executante	 = models.CharField(max_length=10000)
    registro_da_executante	 = models.CharField(max_length=10000)
    motivo_de_negaÇÃo_da_executante	 = models.CharField(max_length=10000)
    cÓdigo_regulaÇÃo	 = models.CharField(max_length=10000)
    aih	 = models.CharField(max_length=10000)
    motivo_da_finalizaÇÃo	 = models.CharField(max_length=10000)
    carimbo	 = models.CharField(max_length=10000)
    carimbo_unidade	 = models.CharField(max_length=10000)
    carimbo_medico	 = models.CharField(max_length=10000)
    carimbo_executante	 = models.CharField(max_length=10000)
    carimbo_de_permanencia	 = models.CharField(max_length=10000)
    pdf	 = models.CharField(max_length=10000)
    xlsx	 = models.CharField(max_length=10000)
