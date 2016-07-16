# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from mooc.models import Course
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

@login_required
def back(request, id):
    return HttpResponseRedirect('/index/')

@login_required
def mooc_list(request):
    ml = Course.objects.all()
    return render_to_response('mooc_list.html', {'ml': ml})


@login_required
def mooc_detail(request, id):
    try:
        md = Course.objects.get(id=str(id))
    except Course.DoesNotExist:
        raise Http404
    return render_to_response('mooc_detail.html', {'md': md})


@login_required
def course_add(request, id):
    try:
        user = User.objects.get(id=request.user.id)
        course = Course.objects.get(id=id)
        verify = User.objects.filter(course__id=id, id=request.user.id)
        if verify:
            messages.error(request, '已经选择该课程！')
        else:
            course.course_choose.add(user)
            course.save()
            messages.success(request, "选课成功！")
        return HttpResponseRedirect('/index/')
    except Course.DoesNotExist:
        raise Http404


@login_required
def course_delete(request, id):
    try:
        user = User.objects.get(id=request.user.id)
        course = Course.objects.get(id=id)
        verify = User.objects.filter(course__id=id, id=request.user.id)
        if not verify:
            messages.error(request, '尚未选择这门课程！')
        else:
            course.course_choose.remove(user)
            course.save()
            messages.success(request, "退课成功！")
        return HttpResponseRedirect('/index/')
    except Course.DoesNotExist:
        raise Http404


@login_required
def course_detect(request, id):
    try:
        md = Course.objects.get(id=str(id))
        user = User.objects.get(id=request.user.id)
        my_courses = user.course_set.all()
        course = Course.objects.get(id=id)
        a = set()
        for i in my_courses:
            if i.course_index[:5] == course.course_index[:5] and i.course_name != course.course_name:
                a.add(i)
            if i.course_index[6:11] == course.course_index[:5] and i.course_name != course.course_name:
                a.add(i)
            if i.course_index[:5] == course.course_index[6:11] and i.course_name != course.course_name:
                a.add(i)
            if i.course_index[6:11] == course.course_index[6:11] and i.course_name != course.course_name:
                a.add(i)
        if len(a):
            for j in a:
                messages.error(request, '检测到冲突! %s 与 %s 有冲突！ ' % (j.course_name.encode('utf-8'), course.course_name.encode('utf-8')))
            return HttpResponseRedirect('/index/')
        else:
            messages.success(request, "无冲突！")
            return HttpResponseRedirect('/index/')
    except Course.DoesNotExist:
        raise Http404

@login_required
def show_my_course(request):
    user = User.objects.get(id=request.user.id)
    my_course = user.course_set.all()
    return render_to_response('mooc_select_show.html', {'my_course': my_course})


@login_required
def show_who_choose_this_class(request, id):
    course = Course.objects.get(id=id)
    class_mates = course.course_choose.all()
    return render_to_response('mooc_class_mates.html', {'class_mates': class_mates})
