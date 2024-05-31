from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from carpet.models import Carpet
from .models import Conversation
from .forms import ConversationMessageForm

@login_required
def new_conversation(request, carpet_id):
    carpet = get_object_or_404(Carpet, id=carpet_id)

    conversations = Conversation.objects.filter(carpet=carpet).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', id=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(carpet=carpet)
            conversation.members.add(request.user)
            conversation.members.add(carpet.seller)
            conversation.save()

            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()

            return redirect('carpet:detail', carpet_id)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })


@login_required
def detail(request, id):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(id=id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()

            conversation.save()

            return redirect('conversation:detail', id=id)

    else:
        form = ConversationMessageForm()
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
    })

@login_required
def delete(request, id):
    conversation = get_object_or_404(Conversation, id=id)
    conversation.delete()
    return redirect('conversation:inbox')