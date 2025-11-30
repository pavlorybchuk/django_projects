from django.shortcuts import render, redirect
from typing import List

class FeedbacksList(List):
    def __init__(self):
        super().__init__()
    
    def add_feedback(self, rating: int, customer_name: str):
        self.append({'rating': rating, 'customer_name': customer_name})
        
feedbacks = FeedbacksList()

def anagram_check(request):
    if request.method == 'POST':
        word1 = request.POST.get('word1', '').strip()
        word2 = request.POST.get('word2', '').strip()
        return redirect('anagram_result', are_anagrams=sorted(list(word1)) == sorted(list(word2)))

    return render(request, 'task_2_3/index.html', {'message': ''})

def anagram_result(request, are_anagrams: bool):
    are_anagrams = are_anagrams.lower() == 'true'
    if are_anagrams:
        message = "The words are anagrams"
    else:
        message = "The words aren't anagrams"
        
    return render(request, 'task_2_3/index.html', {'message': message})

def send_feedback(request):
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        customer_name = request.POST.get('customer_name', 'Anonymous').strip()
        feedbacks.add_feedback(rating, customer_name)
        return render(request, 'task_2_3/feedback.html', {'message': 'Thank you for your feedback!'})
    
    return render(request, 'task_2_3/feedback.html', {'message': ''})

def get_feedbacks(request):
    if not feedbacks:
        return render(request, 'task_2_3/rating.html', {'message': 'No feedbacks yet.'})
    ctx = {
        'message': '',
        'feedbacks': feedbacks, 
        'average_rating': round(sum(f['rating'] for f in feedbacks) / len(feedbacks), 2) if feedbacks else 0, 
        'total_feedbacks': len(feedbacks),
        'count_1': len([f['rating'] for f in feedbacks if f['rating'] == 1]),
        'count_2': len([f['rating'] for f in feedbacks if f['rating'] == 2]),
        'count_3': len([f['rating'] for f in feedbacks if f['rating'] == 3]),
        'count_4': len([f['rating'] for f in feedbacks if f['rating'] == 4]),
        'count_5': len([f['rating'] for f in feedbacks if f['rating'] == 5]),
        'fashion': max(set(f['rating'] for f in feedbacks), key=lambda x: len([f for f in feedbacks if f['rating'] == x])) if feedbacks else 0,
        'median': ((
            sorted(f['rating'] for f in feedbacks)[(len(feedbacks) - 1)//2]) 
                   if len(feedbacks) % 2 != 0 else (
                       sorted(f['rating'] for f in feedbacks)[(len(feedbacks) - 1)//2 - 1] + sorted(f['rating'] for f in feedbacks)[len(feedbacks)//2] / 2)) if feedbacks else 0,
    }
    return render(request, 'task_2_3/rating.html', ctx)