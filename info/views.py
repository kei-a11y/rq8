#/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import AutomationRequestForm
from .models import AutomationRequest
import openpyxl

# 一般訪問者用フォーム
def request_form_view(request):
    if request.method == "POST":
        form = AutomationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("info:request_success")
    else:
        form = AutomationRequestForm()
    return render(request, "info/request_form.html", {"form": form})

# 送信完了画面
def request_success_view(request):
    return render(request, "info/request_success.html")

# 管理者用一覧
@login_required
def admin_list_view(request):
    requests = AutomationRequest.objects.all().order_by("-created_at")
    return render(request, "info/admin_list.html", {"requests": requests})

# Excel出力のみ
@login_required
def export_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Requests"
    ws.append(["送信日時", "業態", "業態（その他）", "システム名", "マニュアル", "連絡先", "その他"])

    for r in AutomationRequest.objects.all():
        # Windowsでも動くフォーマット（ゼロ付き）
        formatted_date = r.created_at.strftime("%Y年%m月%d日 %H時%M分%S秒")
        ws.append([
            formatted_date,
            r.industry,
            r.other_industry if r.industry == "その他" else "-",
            r.system_name,
            r.manual_file.name if r.manual_file else "",
            r.contact_info,
            r.other if r.other else "-"
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="requests.xlsx"'
    wb.save(response)
    return response
