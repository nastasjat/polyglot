from django.urls import path
from PolyglotApp import views


urlpatterns = [
    path("language/", views.languageApi),  # Retrieve all languages
    path(
        "language/<int:id>/", views.languageApi
    ),  # Retrieve, update, or delete a specific language
    path("course/", views.courseApi),
    path("course/<int:id>/", views.courseApi),
    path("teacher/", views.teacherApi),
    path("teacher/<int:id>/", views.teacherApi),
    path("enrolment/", views.enrolmentApi),
    path("enrolment/<int:id>/", views.enrolmentApi),
    path("student/", views.studentApi),
    path("student/<int:id>/", views.studentApi),
]
