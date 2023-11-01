from django.shortcuts import render, redirect, get_object_or_404
from .models import Conversation
from .forms import ConversationMessageForm  # Make sure to import your ConversationMessageForm
from item.models import Item

from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')

    # Check if a conversation already exists for the item and user
    conversations = Conversation.objects.filter(item=item, members=request.user)

    if conversations:
        # If a conversation exists, you might want to handle this case accordingly.
        return redirect('conversation:detail',pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            # Create a new conversation associated with the item
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            # Create a conversation message and associate it with the conversation
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()  # Save the message

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.htm', {'form': form})


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])


    context={

        'conversations':conversations,
    }
    return render(request,'conversation/inbox.htm',context)


@login_required
def detail(request,pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    if request.method=='POST':
        form=ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            conversation.save()

            return redirect('conversation:detail',pk=pk)

    else:
        form=ConversationMessageForm()
    context={
        'conversation':conversation,
        'form':form
    }
    return render(request,'conversation/detail.htm',context)







