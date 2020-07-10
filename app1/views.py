from django.shortcuts import render,redirect
from app1.models import StudentModel,AddClassModel
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
#from app1.forms import AddClassForm

def Showmain(request):
    results = AddClassModel.objects.all()
    return render(request,"main.html",{"da":results})


def stu_reg(request):
    return render(request,"stu_reg.html")

def stu_registerd(request):
    na=request.POST.get("t1")
    cn = request.POST.get("t2")
    ei = request.POST.get("t3")
    pw = request.POST.get("t4")
    StudentModel(name=na,Contactno=cn,emailid=ei,password=pw).save()
    return redirect('stu_reg')



def student_info(request):
    res=StudentModel.objects.all()
    return render(request,"new for reg.html",{"data":res})
    #return render(request,"new for reg.html")

def stu_login(request):
    return render(request,"stu_login.html")



def stu_login_check(request):
    un=request.POST.get("l1")
    pw=request.POST.get("l2")
    try:
        StudentModel.objects.get(name=un,password=pw)
        return render(request,"student_page.html",{"data":un})
    except ObjectDoesNotExist:
        messages.error(request,"Invalid User")
        return redirect('stu_login')


def admin_login(request):
    return render(request,"admin_login.html")


def admin_login_check(request):
    na = request.POST.get("a1")
    pw = request.POST.get("a2")
    if na == "a" and pw == "a":
        return render(request, "admin_page.html")
    else:
        messages.error(request, "Invali Admin")
        return redirect('admin_login')


def shedule_new_cls(request):
    return render(request,"shedule_new_cls.html")


def class_added(request):
    #cf=AddClassForm(request.POST)
    #if cf.is_valid():
      #  cf.save()
    #return redirect("shedule_new_cls")
    na=request.POST.get("c1")
    fa = request.POST.get("c2")
    da = request.POST.get("c3")
    ti = request.POST.get("c4")
    fe = request.POST.get("c5")
    du = request.POST.get("c6")
    AddClassModel(Name=na,Faculty=fa,Date=da,Time=ti,Fee=fe,Duration=du).save()
    return render(request,"shedule_new_cls.html",{"result":'shedule is saved'})


def view_shedule(request):
    res=AddClassModel.objects.all()
    return render(request,"view_shedul.html",{"data":res})


def showupdate(request):
    no=request.GET.get("t1")
    # Query to read 1 record from DB
    result=AddClassModel.objects.get(id=no)
    return render(request, "update.html", {"data": result})


def update_cls(request):
    no=request.POST.get("u1")
    na = request.POST.get("u2")
    fa = request.POST.get("u3")
    da = request.POST.get("u4")
    ti = request.POST.get("u5")
    fe = request.POST.get("u6")
    du = request.POST.get("u7")
    AddClassModel.objects.filter(id=no).update(Name=na, Faculty=fa, Date=da, Time=ti, Fee=fe,Duration=du),
    return redirect('view_shedule')


def delete(request):
    no=request.GET.get("no")
    # delete 1 recod from DB
    AddClassModel.objects.filter(id=no).delete()
    return redirect('view_shedule')


def enrol_course(request):
    res = AddClassModel.objects.all()
    return render(request, "enrol_course.html", {"data": res})










