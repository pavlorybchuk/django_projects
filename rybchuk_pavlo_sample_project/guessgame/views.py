from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random

def guess_game(request):
    if 'secret_number' not in request.session:
        request.session['secret_number'] = random.randint(1, 100)
        request.session['message'] = 'I thought of a number between 1 and 100. Try to guess it!'
        request.session['user_guess'] = ''

    if request.method == 'POST':
        try:
            user_guess = int(request.POST.get('guess'))
        except (ValueError, TypeError):
            request.session['message'] = 'Invalid number!'
            return HttpResponseRedirect(reverse('guess_game'))

        secret = request.session['secret_number']

        if user_guess == secret:
            request.session['message'] = f'Congradulatios, you have guessed the generated number! Game restarts.'
            request.session['secret_number'] = random.randint(1, 100)
        elif user_guess < secret:
            request.session['message'] = 'Generated number is higher!'
        else:
            request.session['message'] = 'Generated number is lower!'
            
        request.session['user_guess'] = user_guess

        return HttpResponseRedirect(reverse('guess_game'))
    
    message = request.session.get('message', '')
    return render(request, 'guessgame/index.html', {'message': message, 'user_guess': request.session.get('user_guess', '')})