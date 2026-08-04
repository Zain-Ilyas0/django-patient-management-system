
from django.shortcuts import render
from rest_framework import generics
from . models import PatientData
from .serializers import PatientDataSerializer
from django.shortcuts import render
from rest_framework.parsers import FormParser, MultiPartParser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 

# Create your views here.

class PatientDataListCreate(generics.ListCreateAPIView):
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer
    parser_classes = [FormParser, MultiPartParser]


# def sidebar(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         data = {
#             'title': title,
#             'description': description
#         }

#         PatientData.objects.create(
#             title=title,
#             description=description
#         )

#     data = PatientData.objects.all()


#     return render(request, "sidebar.html", {'data':data})




def sidebar(request):
    if request.method == "POST":
        patient_name = request.POST.get("patient_name")
        patient_number = request.POST.get("patient_number")
        patient_issue = request.POST.get("patient_issue")
        appointment_date = request.POST.get("appointment_date")

        if not patient_name or not patient_number or not patient_issue or not appointment_date:
            messages.error(request, "Please enter all values.")
            return redirect("sidebar")

        PatientData.objects.create(
            patient_name=patient_name,
            patient_number=patient_number,
            patient_issue=patient_issue,
            appointment_date=appointment_date
        )
        
        messages.success(request, "Patient added successfully.")
        return redirect("sidebar")

    patients = PatientData.objects.filter(is_deleted=False)

    return render(request, "sidebar.html", {
    "patients": patients,
    "patient": None,
    })






def edit(request, id):
    data = get_object_or_404(PatientData, id=id)
    

    if request.method == "POST":
        data.patient_name = request.POST.get("patient_name")
        data.patient_number = request.POST.get("patient_number")
        data.patient_issue = request.POST.get("patient_issue")
        data.appointment_date = request.POST.get("appointment_date")
        data.save()
        return redirect("sidebar")


    patients = PatientData.objects.all()
    return render(request, "sidebar.html", {
            "patients": patients,
            "patient": data,
    })

    # return render(request, "sidebar.html", {"data": data})


# def delete(request, id):
#     data = get_object_or_404(PatientData, id=id)
#     data.delete()
#     return redirect('sidebar')




def delete(request, id):
    patient = get_object_or_404(PatientData, id=id)
    patient.is_deleted = True
    patient.save()
    return redirect("sidebar")


def header(request):
    return render(request, "header.html")



def doctordata(request):
    return render(request, "doctordata.html")