from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required


from .models import Student, Note
from .forms import StudentForm, NoteForm


# Create your views here.
def index(request):
    """A página inicial de Web Espelp"""
    return render(request, 'diaries/index.html')
@login_required  
def alunos(request):
    """Mostra todos os alunos Ativos por página"""
    
     #Garante uma lista apenas para alunos Ativos
    student_list = Student.objects.filter(novalid=False).order_by('name')
    
    paginator = Paginator(student_list, 20) # Show 20 objects per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'diaries/students.html', context)

@login_required 
def inativo(request):
    """Mostra todos os alunos inativos por página"""
    
    #Garante lista apenas para alunos Inativos
    novalid_list = Student.objects.filter(novalid=True).order_by('name')
    
    paginator = Paginator(novalid_list, 20) # Show 20 objects per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'diaries/novalid.html', context)
    

@login_required
def aluno(request, aluno_id):
    student = Student.objects.filter(id=aluno_id)
    context = {'student': student}
    return render(request, 'diaries/student.html', context)

@login_required 
def anotacoes(request):
    """Mostra todos as anotações por página"""
    
    note_list = Note.objects.order_by('-date_added')
    paginator = Paginator(note_list, 20) # Show 20 objects per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request,'diaries/notes.html', context)

@login_required  
def anotacao(request, note_id):
    note = Note.objects.filter(id=note_id)
    context = {'note': note}
    return render(request, 'diaries/note.html', context)

#FORMULÁRIOS

@login_required
def novo_aluno(request):
    """Adiciona um novo aluno."""
    if request.method != 'POST':
        #Cria um form em branco
        form = StudentForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = StudentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = form.name.upper()
            form.lname = form.lname.upper()
            form.local = form.local.title()
            form.district = form.district.title()
            form.addr01 = form.addr01.title()
            form.addr02 = form.addr02.title()

            form.save()
            return HttpResponseRedirect(reverse('diaries:alunos'))
    context = {'form': form}
    return render(request, 'diaries/new_student.html', context)

@login_required
def add_anotacao(request):
    """Adiciona uma anotação."""
    if request.method != 'POST':
        form = NoteForm()
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diaries:anotacoes'))
    context = {'form': form}
    return render(request, 'diaries/add_note.html', context)

@login_required
def edit_aluno(request, aluno_id):
    """Edita um aluno existente."""
    aluno = get_object_or_404(Student, id=aluno_id)
    if request.method != 'POST':
        # Requisição inicial; preenche previamente o formulário com a entrada atual
        form = StudentForm(instance=aluno)
    else:
        # Dados de POST submetidos; processa os dados
        form = StudentForm(instance=aluno, data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = form.name.upper()
            form.lname = form.lname.upper()
            form.local = form.local.title()
            form.district = form.district.title()
            form.addr01 = form.addr01.title()
            form.addr02 = form.addr02.title()

            form.save()
            return HttpResponseRedirect(reverse('diaries:aluno', args=[aluno.id]))
    context = {'aluno': aluno, 'form': form}
    return render(request, 'diaries/edit_student.html', context)

@login_required
def edit_anotacao(request, note_id):
    """Edita uma anotação."""
    note = get_object_or_404(Note, id=note_id)
    if request.method != 'POST':
        form = NoteForm(instance=note)
    else:
        form  = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diaries:anotacao', args=[note.id]))
    context = {'note': note, 'form': form}
    return render(request, 'diaries/edit_note.html', context)
    
#   DELETE VIEWS

@login_required
def note_delete(request, note_id):
    """
    Excluir anotacao sem confirmaçao
    """
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return HttpResponseRedirect(reverse('diaries:anotacoes'))
    
@login_required
def del_aluno(request, aluno_id):
    """
    Excluir aluno e confirma
    """
    s = get_object_or_404(Student, id=aluno_id)
    if request.POST:
        s.delete()
        return HttpResponseRedirect(reverse('diaries:alunos'))
    context = {'s': s}
    return render(request, 'diaries/del_student.html', context)

@login_required
def search(request):
    """
    Barra de busca com paginação
    """
    query = request.GET.get('q')
    
    if query:
        # Garante a busca apenas para alunos Ativos
        main_list = Student.objects.filter(novalid=False) 
        
        results = main_list.filter(Q(name__icontains=query) | Q(lname__icontains=query))
    else:
        results = Student.objects.all()
         
    paginator = Paginator(results, 20) # Show 20 objects per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'query': query}
    
    return render(request, 'diaries/students.html', context)

@login_required
def search_note(request):
    """
    Barra de busca com paginação
    """
    query = request.GET.get('q')
    
    if query:        
        results = Note.objects.filter(Q(student__name__icontains=query))
    else:
        results = Note.objects.all()
         
    paginator = Paginator(results, 20) # Show 20 objects per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'query': query}
    
    return render(request, 'diaries/notes.html', context)
