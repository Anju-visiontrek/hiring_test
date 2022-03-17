# from django.shortcuts import render
#
# # Create your views here.
# def Admin_Register(request):
#         print("enter")
#         if request.method == "POST":
#             print("jdfjd")
#             form = profileform(request.POST, request.FILES)
#             print("cmng")
#             name = request.POST['Name']
#             email = request.POST['Email']
#             phone_no = request.POST['Phone_No']
#             password= request.POST['Password']
#             password= request.POST['city']
#
#             if form.is_valid():
#                 f1 = form.save(commit=False)
#                 f1.Name = name
#                 f1.city = city
#                 f1.Email = email
#                 f1.Phone_No = phone_no
#                 f1.Password = password
#                 f1.save()
#                 user=User.objects.create(username=name,password=password)
#                 user.set_password(password)
#                 print(user.password)
#                 user.save()
#                 x=Profile.objects.create(user=user,fisrt_name=name,city=address)
#                 x.save()
#                 print(f1)
#                 return redirect('/')
#
#
#             else:
#                 print("form not valid")
#                 form = profileform(request.POST)
#                 return render(request, 'admin_register.html', {'form': form})
#
#         else:
#             print("else")
#         return render(request, 'profile.html', locals())
#
#
#
# def Admin_login(request):
#         if request.method == "POST":
#             form = Login_form(request.POST)
#             if form.is_valid():
#                 username = request.POST['username']
#                 print(username)
#                 password = request.POST['password']
#                 print(password)
#                 a = auth.authenticate(request, username=username, password=password)
#                 print(a)
#                 if a is not None:
#                     auth.login(request, a)
#                     return redirect('/language')
#         else:
#             form = Login_form(request.POST)
#         return render(request, 'admin_login.html', {'form': form})
#
