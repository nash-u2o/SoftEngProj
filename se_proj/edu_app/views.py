import json

from django.shortcuts import redirect, render
from edu_app.models import (
    Tbl_assignment,
    Tbl_class,
    Tbl_student,
    Tbl_student_class,
    Tbl_teacher,
    Test,
)


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def base(request):
    return render(request, "base.html")


def classpage(request):
    return render(request, "classpage.html")


def login(request):
    # Add Later: If session id already assigned, automatically redirect.
    # Logout option should redirect here and clear all session info

    context = {
        "login": True,
    }

    if request.method == "POST":
        email = request.POST["user"]  # Use email to log in
        password = request.POST["pass"]

        # This would allow direct querying of the DB. Might allow SQL injection so avoid
        """ 
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor() #Cursor allows us to execute SQL statements and fetch results
        res = cur.execute("SELECT password FROM edu_app_user WHERE email=?", (email,))
        """

        s_res = Tbl_student.objects.filter(student_email=email)
        t_res = Tbl_teacher.objects.filter(teacher_email=email)
        if len(s_res) > 0:
            if s_res[0].student_password == password:  # Successful student login
                s_id = s_res[0].student_id

                request.session["teacher"] = False
                request.session["id"] = s_id

                # Rendering doesn't perform desired functionality. Instead, we must redirect
                return redirect("dashboard")
        elif len(t_res) > 0:
            if t_res[0].teacher_password == password:  # Successful teacher login
                t_id = t_res[0].teacher_id

                request.session["teacher"] = True
                request.session["id"] = t_id

                return redirect("dashboard")
        else:
            context["login"] = False

    return render(request, "login.html", context)


def assignments(request):

    user_id = request.session["id"]
    student_classes = Tbl_student_class.objects.filter(student_id=user_id).values_list(
        "class_id", flat=True
    )
    student_assignments = Tbl_assignment.objects.filter(class_id__in=student_classes)

    return render(
        request, "assignments.html", context={"assignments": student_assignments}
    )


def modules(request):
    return render(request, "modules.html")


# To do: Make JS page insert whatever is loaded into the text field
def text(request):
    text = ""
    id_filter = Test.objects.filter(creator_id=request.session["id"])
    if request.method == "POST":
        data = request.POST.get("values")  # Get the values sent over by user
        if len(id_filter) == 0:
            entry = Test(creator_id=request.session["id"], text=data)
            entry.save()
        else:
            entry = Test.objects.get(creator_id=request.session["id"])
            entry.text = data
            entry.save()
    else:
        res = Test.objects.filter(creator_id=request.session["id"])
        if len(res) > 0:
            text = id_filter[0].text

    print(text)
    context = {"text": text}

    return render(request, "text.html", context)


# class_id is passed through django's get syntax. Url in urls.py has been modified for this
def info(request, class_id):
    text = ""
    is_teacher = request.session["teacher"]

    print(class_id)

    # Executes upon info update
    if request.method == "POST":
        data = request.POST.get("values")
        entry = Tbl_class.objects.get(class_id=class_id)
        entry.class_info = data
        entry.save()

    id_filter = Tbl_class.objects.filter(class_id=class_id)

    if len(id_filter) > 0 and id_filter[0].class_info != None:
        text = id_filter[0].class_info

    context = {
        "text": text,
        "is_teacher": is_teacher,
        "class_id": class_id,
    }

    return render(request, "info.html", context)


def dashboard(request):
    # Get class ids
    id = request.session["id"]
    class_list = []
    if request.session["teacher"]:
        classes = Tbl_class.objects.filter(teacher_id=id)
    else:
        classes = Tbl_student_class.objects.filter(student_id=id)

    # Use ids to get class info for cards
    count = 0
    for entry in classes:
        id = entry.class_id
        name = Tbl_class.objects.filter(class_id=id)[0].class_name
        class_info = {
            "id": id,
            "name": name,
        }
        class_list.append(class_info)
        count = count + 1

    context = {"class_list": class_list}

    return render(request, "dashboard.html", context)


def test(request):
    return render(request, "test.html")
