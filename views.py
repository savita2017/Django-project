from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.template import loader
from django.utils import timezone
from django.contrib.auth import authenticate,login,logout
from .models import Question,Choice,User
from .forms import UserForm,ActiveQuesForm
from django.contrib.auth.decorators import login_required  
           
@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context)


@login_required  
def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    active_user=request.user.id
    if active_user==question.user_id:          
        return HttpResponse("Not Allowed To Answer")
    else:  
        return render(request, 'polls/detail.html', {'question': question})
    
@login_required 
def results(request,question_id):    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required 
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
       
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', 
        {'question':question,
        'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))    

#login part---when user login
@login_required
def special(request):
    return HttpResponse("Logged")

#----when user logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
#---when new user want to sign up
def register(request):
    registered=False
    if request.method =='POST':
        user_form=UserForm(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            #reverse('polls:results',args=(question_id,
            #return render(request,'polls/registeration.html',{'user_form':user_form})
            registered=True
            return HttpResponse("You are registered now")
            return HttpResponseRedirect(reverse('index'))
            #return render(request,'polls/login.html',{})
        else:
            print(user_form.errors)
            return HttpResponse("Invalid details")
    else:
        user_form=UserForm()
        return render(request,'polls/registeration.html',{'user_form':user_form})
#----Check User Login authentication 
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User inactive")
        else:
            print("You are not registered user")
            print("You enter username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid details")
    else:
        return render(request,'polls/login.html',{})
  
#---New Question enter by logged User
@login_required        
def activeuser_ques(request):
    if request.method=='POST':
        form=ActiveQuesForm(data=request.POST)
        if user_login==True:
            if form.is_valid():
            #question_text=form.save()
                q=Question(question_text=request.POST['question_text'], pub_date = timezone.now(), user_id=request.user.id)
                q.save()
                q.choice_set.create(choice_text=request.POST['choice_1'], votes=0)
                q.choice_set.create(choice_text=request.POST['choice_2'], votes=0)
                q.choice_set.create(choice_text=request.POST['choice_3'], votes=0)
                return HttpResponse("You Entered a Question!!But not able to Answer this")
                #return HttpResponseRedirect(reverse("polls:index"))
                return render(request,'polls/index.html')           
            else:
                form=ActiveQuesForm()    
                return render(request, 'polls/activeuser_ques.html', {'form': form})
    
