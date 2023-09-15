
from django.urls import path
from .views import ai_prediction, appointment_letter, home,register,verify_otp,login,dasboard,appointment, user_history,show_appointment,prescription,patient,payment,crud

urlpatterns = [
    path("",home.home,name = "home"),
    path("signin",login.signin,name = "signin"),
    path("signout",login.signout,name = "signout"),
    path("signup",register.register.as_view(),name = "signup"),
    path("verifyuser",register.verify_user,name = "verifyuser"),

    path("dasboard",dasboard.dasboard,name = "dasboard"),

    # USER SECTION ................................................................
    path("appointment",appointment.appointment,name = "appointment"),
    path("appointment_history",user_history.appointment_history,name = "history"),
    path("appointment_letter/<slug:slug>",appointment_letter.user_appointment_letter,name = "appointment_letter"),
    path("prescription/<slug:slug>",prescription.user_prescription,name = "prescription"),
    path("payment_history",user_history.payment_history,name = "history"),


    # DOCTOR SECTION ................................................................
    path("today_appointment",show_appointment.appointment,{'template_name':'dasboard/doctor/today_appointment.html'},name = "today_appointment"),
    path("all_appointment",show_appointment.appointment,{'template_name':'dasboard/doctor/all_appointment.html'},name = "all_appointment"),
    path("show_appointment/<slug:slug>",show_appointment.show_appointment,name = "show_appointment"),
    path("doctor_prescription/<slug:slug>",patient.doctor_prescription,name = "doctor_prescription"),
    path("patient-form/<slug:slug>",patient.patient_form,name = "patient-form"),
    path("patient",patient.patient,name = "patient"),



    # path("show_appointment",show_appointment.show_appointment,name = "show_appointment"),
    # TECHNICIAN SECTION ................................................................

    path("add_member/<slug:slug>",crud.add_member,name = "add_member"),
    path("user_data",user_history.user_data,name = "user_data"),
    path("payment",payment.payment,name = "payment"),


    # UPDATE PROFILE SECTION ................................................................
    path("update_password",crud.update_password,name = "update_password"),
    path("profile",crud.profile,name = "profile"),
    path("edit_profile",crud.edit_profile,name = "edit_profile"),
   


    # UPDATE PROFILE SECTION ................................................................


    path("VerifyPasswordOtp",verify_otp.VerifyPasswordOtp,name = "VerifyPasswordOtp"),

    path("prediction",ai_prediction.prediction,name = "prediction"),


]