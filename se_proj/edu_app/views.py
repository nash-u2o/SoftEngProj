from django.shortcuts import get_object_or_404, redirect, render
from edu_app.models import (
    Tbl_assignment,
    Tbl_class,
    Tbl_grade,
    Tbl_student,
    Tbl_student_class,
    Tbl_student_teacher,
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

    context = {
        "login": True,
    }

    if request.method == "POST":
        email = request.POST["user"]  # Use email to log in
        password = request.POST["pass"]

        s_res = Tbl_student.objects.filter(student_email=email)
        t_res = Tbl_teacher.objects.filter(teacher_email=email)
        if len(s_res) > 0:
            if s_res[0].student_password == password:  # Successful student login
                s_id = s_res[0].student_id

                request.session["teacher"] = False
                request.session["id"] = s_id

                # Rendering doesn't perform desired functionality. Instead, we must redirect
                return redirect("dashboard")
            else:
                context["login"] = False
        elif len(t_res) > 0:
            if t_res[0].teacher_password == password:  # Successful teacher login
                t_id = t_res[0].teacher_id

                request.session["teacher"] = True
                request.session["id"] = t_id

                return redirect("dashboard")
            else:
                context["login"] = False
        else:
            context["login"] = False

    return render(request, "login.html", context)


def assignments(request, class_id):

    is_teacher = request.session["teacher"]
    user_id = request.session["id"]
    student_classes = Tbl_student_class.objects.filter(student_id=user_id).values_list(
        "class_id", flat=True
    )
    student_assignments = Tbl_assignment.objects.filter(class_id__in=student_classes)

    context = {
        "assignments": student_assignments,
        "is_teacher": is_teacher,
        "class_id": class_id,
    }

    return render(request, "assignments.html", context)


def modules(request, class_id):
    is_teacher = request.session.get("teacher")
    user_id = request.session.get("id")

    if is_teacher:
        modules = Tbl_class.objects.filter(teacher_id=user_id)
    else:
        modules = Tbl_class.objects.filter(class_id=class_id)

    return render(
        request,
        "modules.html",
        {"modules": modules, "is_teacher": is_teacher, "class_id": class_id},
    )


def edit_module(request, class_id):

    request.method == "POST"
    module_content = request.POST.get("module_content")
    module = get_object_or_404(Tbl_class, class_id=class_id)
    module.class_module = module_content
    module.save()

    return redirect("modules", class_id=class_id)


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

    context = {"text": text}

    return render(request, "text.html", context)


# class_id is passed through django's get syntax. Url in urls.py has been modified for this
def info(request, class_id):
    text = ""
    is_teacher = request.session["teacher"]

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
    is_teacher = False

    # Get class ids
    id = request.session["id"]
    class_list = []
    if request.session["teacher"]:
        classes = Tbl_class.objects.filter(teacher_id=id)
        is_teacher = True
    else:
        classes = Tbl_student_class.objects.filter(student_id=id)

    # Use ids to get class info for cards
    for entry in classes:
        id = entry.class_id
        name = Tbl_class.objects.filter(class_id=id)[0].class_name
        class_info = {
            "id": id,
            "name": name,
        }
        class_list.append(class_info)

    context = {
        "class_list": class_list,
        "is_teacher": is_teacher,
    }

    return render(request, "dashboard.html", context)


def students(request, class_id):
    is_teacher = request.session["teacher"]
    context = {
        "is_teacher": is_teacher,
        "class_id": class_id,
    }

    if request.method == "POST":
        post_dict = request.POST

        # For add - get students of given email. If exist, check if in class. If not, add to class.
        # For delete - get student of given email. If exist, check if in class. If yes, delete from class
        if "add" in post_dict:
            student_filter = Tbl_student.objects.filter(student_email=post_dict["add"])
            if len(student_filter) != 0:
                student = student_filter[0]
                student_class_filter = Tbl_student_class.objects.filter(
                    student_id=student.student_id, class_id=class_id
                )
                if len(student_class_filter) == 0:
                    Tbl_student_class.objects.create(
                        student_id=student.student_id, class_id=class_id
                    )
        elif "delete" in post_dict:
            student_filter = Tbl_student.objects.filter(
                student_email=post_dict["delete"]
            )
            if len(student_filter) != 0:
                student = student_filter[0]
                student_class_filter = Tbl_student_class.objects.filter(
                    student_id=student.student_id, class_id=class_id
                )
                if len(student_class_filter) != 0:
                    student_class_filter.delete()

    return render(request, "students.html", context)


def manage(request):
    if request.method == "POST":
        post_dict = request.POST

        if "delete" in post_dict:
            # Check if email exists
            student_info = Tbl_student.objects.filter(student_email=post_dict["delete"])
            if len(student_info) > 0:
                student_id = student_info.first().student_id
                print(student_id)
                # Delete every entry from every table containing this student ID
                # Tbl_student_teacher, Tbl_student, Tbl_student_class, Tbl_grade
                Tbl_grade.objects.filter(student_id=student_id).delete()
                Tbl_student_class.objects.filter(student_id=student_id).delete()
                Tbl_student_teacher.objects.filter(student_id=student_id).delete()
                Tbl_student.objects.filter(student_id=student_id).delete()

        # If all forms for adding exist, create a new student
        if "email" in post_dict and "name" in post_dict and "password" in post_dict:
            Tbl_student.objects.create(
                student_email=post_dict["email"],
                student_name=post_dict["name"],
                student_password=post_dict["password"],
            )

    return render(request, "manage.html")


def test(request):
    return render(request, "test.html")
