from ecomstore.accounts.models import UserProfile
from ecomstore.accounts.forms import UserProfileForm
from ecomstore.utils import checkout_audit

def retrieve(request):
    """ gets the UserProfile instance for a user, creates one if it does not exist """
    try:
        profile = UserProfile.objects.get(user_id=request.user.id)
    except:
        profile = None

    if profile == None:
        checkout_audit._audit(request, 'UserProfile does not exist, create one: ', 'User id:{}'.format(request.user.id)) 
        profile = UserProfile(user=request.user)
        profile.save()
    return profile
    
def set(request):
    """ updates the information stored in the user's profile """
    if request.user.id is not None:
        profile = retrieve(request)
        profile_form = UserProfileForm(request.POST, instance=profile)
        profile_form.save()
    
