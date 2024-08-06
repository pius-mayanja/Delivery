from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from jumia.models import Type

from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Type, pk=item_pk)

    if item.product_by == request.user:
        return redirect('user:login')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('chart:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.product_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('chart:inbox')
    else:
        form = ConversationMessageForm()
    
    return render(request, 'chart/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'chart/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('chart:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'chart/detail.html', {
        'conversation': conversation,
        'form': form
    })