from django.shortcuts import render

import json
from django.utils import timezone
from datetime import timedelta
from model_app.models import PublicPredictionLog

def landing_page(request):
    """
    Public landing page for all users, offering information and routing them
    to registration, login, or the scanner tools.
    """
    today = timezone.now().date()
    dates = [(today - timedelta(days=i)) for i in range(6, -1, -1)]
    date_labels = [d.strftime('%b %d') for d in dates]
    
    spam_data = [0] * 7
    ham_data = [0] * 7
    
    for i, d in enumerate(dates):
        spam_data[i] = PublicPredictionLog.objects.filter(created_at__date=d, predicted_label__iexact='spam').count()
        ham_data[i] = PublicPredictionLog.objects.filter(created_at__date=d).exclude(predicted_label__iexact='spam').count()
        
    chart_data = {
        'dates': date_labels,
        'spam': spam_data,
        'ham': ham_data
    }

    return render(request, 'core/landing.html', {'chart_data_json': json.dumps(chart_data)})

def documentation_page(request):
    """
    Project overview, tutorial, and guide page.
    """
    return render(request, 'core/documentation.html')
