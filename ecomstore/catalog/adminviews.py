from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django.utils.translation import gettext as _
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect




from ecomstore.catalog.forms import InventoryForm


def edit_inventory(request):
    """A quick inventory price, qty update form"""

    if request.method == "POST":
        new_data = request.POST.copy()
        form = InventoryForm(new_data)
        if form.is_valid():
            form.save(request)
            url = reverse('satchmo_admin_edit_inventory')
            return HttpResponseRedirect(url)
    else:
        form = InventoryForm()

    ctx = {
        'title' : _('Inventory Editor'),
        'form' : form
        }

    return render(request, 'catalog/admin/inventory_form.html',
                              ctx)

edit_inventory = user_passes_test(lambda u: u.is_authenticated() and u.is_staff, login_url='/accounts/login/')(edit_inventory)
