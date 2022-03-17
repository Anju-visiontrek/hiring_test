from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Product_owner_role.models import User, TaskLanguage, TaskLevel
from company_role.models import Company_Profile
from Sample_Paper.models import Question, SamplePaper


def dashboard_index(request):
   return render(request, "dashboard.html", locals())


    # if not request.user.is_superuser:
    #     employee_tab = True
    #     user_tasks_count = TaskLanguage.objects.filter(user=request.user).count()
    #     # user_project_count = Project.objects.filter(user=request.user).count()
    #     # user_attendence_count = Attendence.objects.filter(user=request.user).count()
    #     # task_details=Task.objects.values_list('task_type__type_name',flat=True).filter(user=request.user)
    #
    #     # page_list = list()
    #     #
    #     # for link in task_details:
    #     #
    #     #     page_list.append(link)
    #     # page_list=set(page_list)
    # if request.user.is_superuser:
    #     super_user_tab = True
    #     total_users = User.objects.all().count()
    #     total_tasks = TaskLevel.objects.all().count()
    #     # total_departments = ProgrammingLanguage.objects.all().count()
    #     # total_systems = system_detail.objects.all().count()
    #     # total_user_task = Task.objects.all().count()
    #     # total_user_project = Project.objects.all().count()
    #     #
    # return render(request, "dashboardapp/dashboard_home.html", locals())


def company_Register(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
            company_profile = Company_Profile.objects.create(company_Name=request.POST['company_Name'],
                                                                  company_address=request.POST['company_address'],
                                                                  company_phone_no=request.POST['company_phone_no'],
                                                                  company_email=request.POST["company_email"],
                                                                  company_Password=request.POST['company_Password'],
                                                                  company_state=request.POST['company_state'])

            request.session['company_Profile']=company_profile.pk
            get=request.session['company_Profile']
            x=Company_Profile.objects.get(id=company_profile.pk)
            user=User.objects.create(company=x,username=x.company_Name,password=x.company_Password)
            user.set_password(x.company_Password)
            user.save()


        else:
            if request.method == "POST":
                company_profile = Company_Profile.objects.create(company_Name=request.POST['company_Name'],
                                                                 company_address=request.POST['company_address'],
                                                                 company_phone_no=request.POST['company_phone_no'],
                                                                 company_email=request.POST["company_email"],
                                                                 company_Password=request.POST['company_Password'],
                                                                 company_state=request.POST['company_state'])

                request.session['company_Profile'] = company_profile.pk
                get = request.session['company_Profile']
                x = Company_Profile.objects.get(id=company_profile.pk)
                user = User.objects.create(company=x, username=x.company_Name, password=x.company_Password)
                user.set_password(x.company_Password)
                user.save()

        return render(request, 'profile.html', locals())


#
def Admin_login(request):
        if request.method == "POST":
                username = request.POST['username']
                print(username)
                password = request.POST['password']
                print(password)
                user= auth.authenticate(request, username=username, password=password)
                auth.login(request, user)
                print("login")
                return redirect('/dashboard_index')
        return render(request, 'profile_login.html', locals())


def get_language(request):
    if request.user.is_superuser==True:
        all_task_languages = TaskLanguage.objects.filter(is_active=True).values_list('name')
    return render(request, 'inbuilt_languge.html', locals())

def create_language(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
              language=TaskLanguage.objects.create(name=request.POST['name'],user=request.user)
              print(language)
              return redirect("/add_level")

    else:
        print("jdsj")
    return render(request, 'add_language.html', locals())


def get_level(request):
    if request.user.is_superuser==True:
        all_level = TaskLevel.objects.filter(is_active=True).values_list('name')


    return render(request, 'inbuilt_level.html', locals())



def create_level(request):
    if request.user.is_superuser==True:
       if request.method == "POST":
          language=TaskLevel.objects.create(name=request.POST['name'],user=request.user)
          print(language)
          return redirect("/add_questions")

    else:
        print("jdsj")
    return render(request, 'add_level.html', locals())




def get_allcompanies(request):
    if request.user.is_superuser == True:
        all_companies=Company_Profile.objects.all()
        print(all_companies)
    else:
        print("error")
    return render(request, 'all_companies.html', locals())




def add_questions(request):
    if request.user.is_superuser == True:

        all_task_languages = TaskLanguage.objects.filter(is_active=True).values_list('name')
        all_level = TaskLevel.objects.filter(is_active=True).values_list('name')

        all_ques_ans = Question.objects.all()
        print(all_ques_ans)
        if request.method == "POST":
            languge=request.POST['task_language'].lower()
            level=request.POST['level_task'].lower()
            taskLanguage= TaskLanguage.objects.get(name=languge)
            taskLevel= TaskLevel.objects.get(name=level)
            question= Question.objects.create(language=taskLanguage,level=taskLevel,ques=request.POST['ques'],ans=request.POST['ans'],user=request.user)
            return redirect("/create_sample_paper")

    else:
        print("exit")
    return render(request, 'add_ques_ans.html', locals())



def create_sample_paper(request):
    if request.user.is_superuser == True:
        all_task_languages = TaskLanguage.objects.filter(is_active=True).values_list('name')
        print(all_task_languages)
        all_level = TaskLevel.objects.filter(is_active=True).values_list('name')
        all_ques = Question.objects.filter(is_active=True).values_list('ques')

        if request.method == "POST":
            language=request.POST.get('task_language').lower()
            print(language)
            level=request.POST.get('level_task').lower()
            print(level)
            taskLanguage = TaskLanguage.objects.get(name=language)
            taskLevel = TaskLevel.objects.get(name=level)

            question1 = SamplePaper.objects.filter(language=taskLanguage,
                                       level=taskLevel)
            print(question1)

            for i in question1.objects.all():
                print(i.question.all)






    else:
        print("exit")
    return render(request, 'add_sample_paper.html', locals())







