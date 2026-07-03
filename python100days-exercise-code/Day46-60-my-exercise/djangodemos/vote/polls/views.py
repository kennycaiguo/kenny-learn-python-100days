from django.shortcuts import render, redirect
from polls.models import Subject, Teacher
from django.http import JsonResponse

# Create your views here.
def show_subjects(request):
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


def show_teachers(request):
    teachers = Teacher.objects.all()
    return None


def get_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
        return render(request, 'teacher.html', {
            'subject': subject,
            'teachers': teachers
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')


# /praise/?tno=1 gcount
# /scold/?tno=2  bcount
def good_or_bad(request):
    try:
        tno = int(request.GET.get('tno'))
        teacher = Teacher.objects.get(no=tno)
        if request.path.starswith('/praise'):
            teacher.gcount += 1
            count = teacher.gcount
        else:
            teacher.bcount += 1
            count = teacher.bcount
        teacher.save()
        data = {
            "code": 20000, "msg": "操作成功", "count": count
        }
    except (ValueError, Teacher.DoseNotExist):
        data = {
            "code": 20001, "msg": "操作失败"
        }
    return JsonResponse(data)



