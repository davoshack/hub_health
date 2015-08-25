from data_users.models import ProfileUser
from registration.models import RegistrationProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def load_profile(request):
    data = {}
    user_login = request.user
    object_profile = RegistrationProfile.objects.filter(user_id=user_login.id)
    type_user = object_profile[0].tipo_usuario
    user_object = ProfileUser.objects.filter(user_id=user_login.id)
    if user_object.count() == 1:
        data['image'] = user_object[0].image
        data['sex'] = user_object[0].sex
    if type_user == 'medic':
        data['type_user_tag'] = 'Specialist'
    else:
        data['type_user_tag'] = 'Patient'
    return data