from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from .models import product
from .forms import ProductCreate, NewUserForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    stock = product.objects.all()
    return render(request, 'index.html', {'stock': stock})

def upload(request):
    upload = ProductCreate()
    if request.method == 'POST':
        upload = ProductCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{% url  '/' %}">reload</a>""")
    else:
        return render(request, 'upload_product.html', {'upload_form':upload})

def update_product(request, product_id):
    product_id = int(product_id)
    try:
        product_sel = product.objects.get(id = product_id)
    except product.DoesNotExist:
        return redirect('index')
    product_form = ProductCreate(request.POST or None, instance = product_sel)
    if product_form.is_valid():
       product_form.save()
       return redirect('index')
    return render(request, 'upload_product.html', {'upload_form':product_form})

def delete_product(request, product_id):
    product_id = int(product_id)
    try:
        product_sel = product.objects.get(id = product_id)
    except product.DoesNotExist:
        return redirect('index')
    product_sel.delete()
    return redirect('index')
#public
def seed_plant(request):
    stock2 = product.objects.all()
    return render(request, 'seeds&plants.html', {'stock2': stock2})

def traps(request):
    stock3 = product.objects.all()
    return render(request, 'traps.html', {'stock3': stock3})

def fertilizers(request):
    stock4 = product.objects.all()
    return render(request, 'fertilizers.html', {'stock4': stock4})

def pesticides(request):
    stock5 = product.objects.all()
    return render(request, 'pesticides.html', {'stock5': stock5})

#registeration
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

#login-logout
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("index")

#users list
def users(request):
    all_users = User.objects.values()
    return render(request, 'users.html',{'users': all_users})

#about us
def aboutus(request):
    return render(request,'about.html')

#contact us
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            send_mail(subject, "Thank You for your inquiry", sender, [sender])
            send_mail(subject, message, sender, ['xyz492865@gmail.com'])


            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

def success(request):
    return render(request,'success.html')