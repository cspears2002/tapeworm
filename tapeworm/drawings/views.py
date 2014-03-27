from django.shortcuts import render

# Create your views here.

def index(request):
  context_dict = {'message': 'Hello World!'}
  return render(request, 'drawings/index.html', context_dict)

def register(request):
  # Variable that tells if the registration was successful.
  registered = False

  if request.method == 'POST':
    # Grab data from the form
    user_form = UserForm(data=request.POST)

    if user_form.is_valid():
      # Save a user to the database
      user = user_form.save()

      # Hash the password and update the user
      user.set_password(user.password)
      user.save()

      # Registration succeeded
      registration = True
    else:
      print user_form.errors
  else:
    # Just render the form
    user_form = UserForm()

  context_dict = {'user_form': user_form, 'registered': registered}
  return render(request, 'drawings/register.html', context_dict)