from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from app.forms import *

class IndexView(TemplateView):
    template_data = {}
    template_name = 'app/index.html'

    def get(self, request, **kwargs):
        form = AppForm()
        self.template_data = {'form': form}
        return render(request, self.template_name, self.template_data)

    def post(self, request):
        form = AppForm(request.POST)
        data = {}
        if form.is_valid():
            p_s = form.clean_pressure_select()
            s = int(form.clean_materials_select())
            p = int(form.clean_pressure_input())
            ri = int(form.clean_internal_radius_input())
            e = int(form.clean_joint_efficiency_input())
            ltt = int(form.clean_tan2tan_input())
            c = int(form.clean_corr_allow_input())
            o_s = int(form.clean_allow_stress_input())

            if s == 0:
                s = o_s

            if (p*ri)/((2*s*e)+(0.4*p))+c < (p*ri)/((2*s*e)-(0.6*p))+c:
                 print("thickness is  {} mm".format((p*ri)/((2*s*e)-(0.6*p))+c))
            else:
                print("thickness is {} mm".format((p*ri)/((2*s*e)+(0.4*p))+c))



        self.template_data = {'form': form, 'app': 'ids', 'data': data}
        return render(request, self.template_name, self.template_data)
