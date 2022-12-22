

from flask import render_template, request

from PhongMachTu import app, db, utils
from flask_admin import Admin, expose, BaseView
from flask_admin.contrib.sqla import ModelView
from PhongMachTu.models import Patient, Card, Medicine, Container, Define

admin = Admin(app=app, name="E-commerce Website", template_mode='bootstrap4')


class PatientView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['username', 'gender', 'year']
    column_filters = ['username', 'gender', 'year']
    column_labels = {
        'username': 'Họ và tên',
        'gender': 'Giới tính',
        'year': 'Năm sinh',
        'address': 'Địa chỉ',
        'joined_date': 'Ngày đăng kí'
    }
    column_sortable_list = ['id', 'username']


# class CardView(ModelView):
#     column_display_pk = False
#     can_view_details = False
#     can_export = False
#     column_searchable_list = ['symptom_medicine', 'predict_medicine']
#     column_filters = ['patient_id', 'symptom_medicine', 'predict_medicine']
#     column_labels = {
#         'patient_id': 'Mã định danh',
#         'symptom_medicine': 'Triệu chứng',
#         'predict_medicine': 'Chuẩn đoán'
#     }
#     column_sortable_list = ['symptom_medicine', 'predict_medicine']


class MedicineView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['name', 'type']
    column_filters = ['name', 'type']
    column_labels = {
        'id': 'Số thứ tự',
        'name': 'Tên thuốc',
        'type': 'Loại',
        'amount': 'Số lượng',
        'instruction': 'Cách sử dụng'
    }
    column_sortable_list = ['type', 'name']


class ContainerView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['name', 'type']
    column_filters = ['name', 'type']
    column_labels = {
        'name': 'Tên thuốc',
        'type': 'Loại',
        'amount': 'Số lượng',
        'instruction': 'Cách sử dụng'
    }
    column_sortable_list = ['type', 'name']


class DefineView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['amount_bn', 'money']
    column_filters = ['amount_bn', 'money']
    column_labels = {
        'amount_bn': 'Số bệnh nhân quy định mỗi ngày',
        'money': 'Tiền khám'
    }
    column_sortable_list = ['amount_bn', 'money']


class StatsView(BaseView):
    @expose("/")
    def index(self):
        stats = utils.stats_revenue(sign_date=request.args.get("sign_date"))
        return self.render('functions/stats.html', stats=stats)


admin.add_view(PatientView(Patient, db.session))
# admin.add_view(ModelView(Card, db.session))
admin.add_view(MedicineView(Medicine, db.session))
admin.add_view(ContainerView(Container, db.session))
admin.add_view(DefineView(Define, db.session))
admin.add_view(StatsView(name='Statistics'))
