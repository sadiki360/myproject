from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TimeTable

@login_required
def timetable_view(request):
    days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
    sessions = ['Matin', 'Soir']
    groups = ['AD-S1', 'AD-S2', 'IDAI-S1', 'IDAI-S2']

    rows = []
    for day in days:
        row = {'day': day, 'sessions': []}
        for session in sessions:
            cell = []
            for group in groups:
                entry = TimeTable.objects.filter(
                    day=day, session=session, group=group
                ).first()
                cell.append({
                    'group': group,
                    'subject': entry.subject if entry else '-'
                })
            row['sessions'].append(cell)
        rows.append(row)

    return render(request, 'timetable/timetable.html', {'rows': rows})