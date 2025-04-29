from django.shortcuts import render, redirect
import json
from .algorithms import Members
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def add_members_view(request):
    if not request.session.get('username'):
        return redirect('custom_login')
    data = {}
    if request.method == "POST":
        name_error = None
        age_error = None
        contact_error = None
        Address_error = None

        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        Address = request.POST.get('Address')

        data = {
            'name': name,
            'age': age,
            'contact': contact,
            'Address': Address
        }

        # validating name
        if not name:
            name_error = 'Please Enter Name'
        elif len(name) < 3:
            name_error = 'Name must be of 3 characters atleast!'
        elif any(char in name for char in ['@', '$', '#', '%', '&', '+','!']):
            name_error = 'No Special characters are allowed Except"-"'
        else:
            name_error = ""

         # validating Age 
        if not age:
            age_error = 'Please enter age limit'
        else:
            try:
                age_int = int(age)
                age_error = ""
            except ValueError:
                age_error = 'Age must be an integer value'

        # validating contact
        if not contact:
            contact_error = 'Please Enter Name'
        elif len(contact) < 3:
            contact_error = 'Contact must be of 3 characters atleast!'
        elif any(char in contact for char in ['@', '$', '#', '%', '&', '+','!']):
            contact_error = 'No Special characters are allowed  except "-"'
        else:
            contact_error = ""

        # validating contact
        if not Address:
            Address_error = 'Please Enter Name'
        elif len(Address) < 3:
            Address_error = 'Address must be of 3 characters atleast!'
        elif any(char in Address for char in ['@', '$', '#', '%', '&', '+','!']):
            Address_error = 'No Special characters are allowed  except "-"'
        else:
            Address_error = ""

        
        if name_error or age_error  or contact_error  or Address_error:

            data.update({
                'error': True,
                'name_error' : name_error,
                'age_error': age_error,
                'contact_error': contact_error,
                'Address_error':Address_error
            })
            return render(request,"memberTemplates/addMember.html",data)

        try:

            with open('members/members.json','r') as file:
                members = json.load(file)
            
            members_class = Members()
            try:
                status = members_class.add_members(memberList=members,name=name,age=age_int,contact=contact,address=Address)
                messages.success(request,status)
                return redirect('members_preview') # Direct to Dash Board
              
            except:
                messages.error(request,"Error While uploading Member to Database Please Try Again")
                return redirect('addMember')
        
        

        except FileNotFoundError:
            messages.error(request, "Error While Adding Book Please Try Again")
            return redirect('addMember')
        




    return render(request, "memberTemplates/addMember.html")

def get_member_view(request,memberID):
    try:
        with open('members/members.json', 'r') as file:
            members = json.load(file)
        
        member_class = Members()
        member_index = member_class.searhMember(membersList=members,ID=memberID)

        if member_index is not None:

            return JsonResponse({
                'name': members[member_index]["name"],
                'age': members[member_index]["age"],
                'contact': members[member_index]["contact"],
                'Address': members[member_index]["Address"],
            })
    except FileNotFoundError:
        print('Error while reading members.json')

def update_member_view(request):
    if not request.session.get('username'):
        return redirect('custom_login')
    if request.method == "POST":

        member_class = Members()
        memberID = request.POST.get('memberID')
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        Address = request.POST.get('address')

        try:
            with open('members/members.json', 'r') as file:
                members = json.load(file)
            status = member_class.update_member(memberList=members,MemberID=memberID,name=name,age=age,contact=contact,Address=Address)
            messages.success(request, status)
            return redirect("members_preview")
        except Exception:
            messages.error(request, 'Error while updating member to Data base')
            return redirect("updateMember")
    return render(request,"memberTemplates/updateMember.html")


def members_preview(request):
    if not request.session.get('username'):
        return redirect('custom_login')
    try:

        with open('members/members.json', 'r') as file:
            members = json.load(file)
        return render(request, "memberTemplates/membersPreview.html",{'members':json.dumps(members)})
    except FileExistsError:
        messages.error(request,"Database File Not Found")
        return render(request, "memberTemplates/membersPreview.html")

def search_members(request):
    query = request.GET.get('query', '').lower()

    with open('members/members.json', 'r') as file:
        members = json.load(file)

    filtered_members = [
        member for member in members
        if query in member.get('MemberID', '').lower() or query in member.get('name', '').lower()
    ]

    return JsonResponse({'members': filtered_members})

def delete_member_view(request):
    if not request.session.get('username'):
        return redirect('custom_login')
    if request.method == "POST":
        member_class = Members()
        memberID = request.POST.get("memberID")

        try:
            with open('members/members.json', 'r') as file:
                members = json.load(file)
            
            status = member_class.delete_member(memberList=members,MemberID=memberID)
            messages.success(request, status)
            return redirect("members_preview")
            
        except Exception:
            messages.error(request, "Unable to Delete Member Try again!")
            return  redirect("deleteMember")

    return render(request,"memberTemplates/deleteMember.html")

    
