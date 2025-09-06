# kk10/models.py
from django.db import models

class AutomationRequest(models.Model):
    INDUSTRY_CHOICES = [
        ("農業、林業", "農業、林業"),
        ("建設業", "建設業"),
        ("製造業", "製造業"),
        ("運輸業", "運輸業"),
        ("卸売業、小売業", "卸売業、小売業"),
        ("不動産業", "不動産業"),
        ("飲食業", "飲食業"),
        ("教育、学習支援", "教育、学習支援"),
        ("医療，福祉", "医療，福祉"),
        ("行政", "行政"),
        ("その他", "その他"),
    ]

    system_name = models.CharField("自動化してほしいシステムの名称", max_length=255)
    industry = models.CharField("業態", max_length=50, choices=INDUSTRY_CHOICES)
    other_industry = models.CharField("業態（その他）", max_length=255, blank=True, null=True)
    manual_file = models.FileField("マニュアル", upload_to="manuals/", blank=True, null=True)
    contact_info = models.CharField("連絡先（宛名・メールアドレス）", max_length=255, blank=True, null=True)
    other = models.CharField("その他", max_length=255, blank=True, null=True)
    created_at = models.DateTimeField("送信日時", auto_now_add=True)

    def __str__(self):
        return self.system_name
