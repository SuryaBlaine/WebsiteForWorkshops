from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import classroom,classroomjoin
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,UpdateView)
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.
def classroomhome(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = classroom.objects.filter(Q(title__icontains=srch))
            if match:
                return render(request,"classroom/home.html",{'sr':match,})
            else:
                messages.error(request,f'no results!')
        else:
            return redirect('classroomhome')

    return render(request,'classroom/home.html',{'classrooms' : classroom.objects.all().order_by('-date_posted'),'classroomjoin' : classroomjoin.objects.all()})
    
@method_decorator([login_required],name='dispatch')
class ClassroomCreateView(CreateView):
    model = classroom
    fields = ('title','subtitle','teacher','description','venue','fee','date_of_class','additional_info')
    template_name = 'classroom/classroomcreate.html'

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.host = self.request.user
        quiz.save()
        return redirect('classroomhome')



@method_decorator([login_required],name='dispatch')
class ClassroomJoinView(CreateView):
    model = classroomjoin
    fields = ()
    template_name = 'classroom/classroomjoin.html'
    
    def get_context_data(self, **kwargs):
        context = {
            'classroom' : classroom.objects.get(pk=self.kwargs['pk'])
        }
        return context
    def form_valid(self, form,**kwargs):
        quiz = form.save(commit=False)
        quiz.classroom = classroom.objects.get(pk=self.kwargs['pk'])
        quiz.user = self.request.user
        quiz.save()
        return redirect('classroomhome')

@method_decorator([login_required],name='dispatch')
class ClassroomEditView(UpdateView):
    model = classroom
    fields = ('title','subtitle','teacher','description','venue','fee','date_of_class','additional_info')
    template_name = "classroom/classroomedit.html"
    success_url = reverse_lazy('classroomhome')

    def form_valid(self,form):
        quiz = form.save(commit=False)
        quiz.user = self.request.user
        quiz.save()
        return redirect('classroomhome')






@method_decorator([login_required],name='dispatch')
class ClassroomDetailView(CreateView):
    model = classroomjoin
    fields = ()
    template_name = 'classroom/classroomdetail.html'
    
    def get_context_data(self, **kwargs):
        context = {
            'classroom' : classroom.objects.get(pk=self.kwargs['pk']),
            'students' : classroomjoin.objects.all()
        }
        return context
    def form_valid(self, form,**kwargs):
        quiz = form.save(commit=False)
        quiz.classroom = classroom.objects.get(pk=self.kwargs['pk'])
        quiz.user = self.request.user
        quiz.save()
        return redirect('classroomhome')


@method_decorator([login_required],name='dispatch')
class ClassroomDeleteView(DeleteView):
    template_name = 'classroom/classroomdelete.html'
    success_url = reverse_lazy('classroomhome')
    def get_object(self, **kwargs):
        id = self.kwargs.get("pk")
        return get_object_or_404(classroom,id=id)
