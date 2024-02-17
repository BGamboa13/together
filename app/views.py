from decimal import Decimal, DecimalException

from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.views.generic import DetailView

from .forms import ContactForm
from .models import Blog, Gallery, DonationCampaign, Donations


# Create your views here.
def index(request):
    blogs = Blog.objects.filter(enabled=True)  # Obtén todos los blogs desde la base de datos
    return render(request, 'index.html', {'blogs': blogs})


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'components/main/blog_detail.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'


def page_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Renderiza el template de correo con los datos del formulario
            email_content = render_to_string('components/email/email_template.html', {'form': form.cleaned_data})

            # Envía el correo
            send_mail(
                'Nueva Solicitud de Contacto',
                email_content,
                'tu_correo@example.com',  # Reemplaza con tu correo
                ['tu_correo@example.com'],  # Reemplaza con tu correo
                fail_silently=False,
            )

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    return render(request, 'page_contact.html', {'formulario': form})


def page_donate(request):
    campaigns = DonationCampaign.objects.filter(enabled=True)

    # Calcular el progreso para cada campaña
    for campaign in campaigns:
        if campaign.target_amount > 0:
            campaign.progress_percentage = (campaign.current_amount / campaign.target_amount) * 100
        else:
            campaign.progress_percentage = 0

        # Verificar si se ha enviado el formulario
        if request.method == 'POST':
            campaign_id = request.POST.get('campaign_id')
            currency = request.POST.get('currency')
            amount = request.POST.get('amount')

            # Verificar si Zelle fue seleccionado
            if currency == 'add-money-zelle-usd-automatic':
                # Obtener la campaña seleccionada
                selected_campaign = DonationCampaign.objects.get(pk=campaign_id)

                # Renderizar la plantilla de instrucciones de Zelle
                return render(request, 'components/donate/zelle_instructions.html',
                              {'campaign': selected_campaign, 'amount': amount})

            # Si no es Zelle o no se ha enviado el formulario, renderizar la página normal
        return render(request, 'page_donate.html', {'campaigns': campaigns})


@require_POST
def process_transaction(request):
    try:
        transaction_number = request.POST.get('transaction_number')
        amount_str = request.POST.get('amount')

        # Validar y convertir el monto a Decimal
        amount = Decimal(amount_str)

        # Obtener la campaña asociada
        campaign_id = request.POST.get('campaign_id')
        selected_campaign = DonationCampaign.objects.get(pk=campaign_id)

        # Crear una nueva instancia del modelo Donations
        Donations.objects.create(
            transaction_number=transaction_number,
            amount=amount,
            currency='USD'  # Ajusta según la moneda de tus transacciones
        )

        # Actualizar el campo current_amount de la campaña
        selected_campaign.current_amount += amount
        selected_campaign.save()

        return redirect('page_donate')  # Redirigir a una página de agradecimiento o confirmación

    except (ValueError, DecimalException) as e:
        # Manejar errores de conversión de Decimal o cualquier otro error
        # Puedes personalizar este bloque de acuerdo a tus necesidades
        return HttpResponse(f'Error en la transacción: {str(e)}', status=400)


class CampaignDetailView(DetailView):
    model = DonationCampaign
    template_name = 'components/donate/campaign_details.html'
    context_object_name = 'campaign'
    slug_url_kwarg = 'slug'


def page_about(request):
    return render(request, 'page_about.html')


def page_gallery(request):
    galleries = Gallery.objects.prefetch_related('images').all()
    return render(request, 'page_gallery.html', {'galleries': galleries})


def page_not_found(request):
    return render(request, 'page_not_found.html', status=404)


def page_camp(request):
    return render(request, 'components/donate/zelle_instructions.html')
