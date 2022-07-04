from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import LoginTable, TeacherModel
from django.conf import settings


def LoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = LoginTable.objects.get(username=loginid, password=pswd)
            request.session['username'] = check.username
            if check.username != None or check.username != '':
                return render(request, 'apphome.html', {})
            else:
                messages.success(request, 'invalid Credential')
                return render(request, 'index.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')

    return render(request, 'index.html', {})


def apphome(request):
    return render(request, 'apphome.html', {})


def importedForm(request):
    return render(request, 'importerform.html', {})


def checkData():
    # plen = len(Profilepicture)
    import os
    # pic = 'default.JPG'
    li = []
    # dir_file = os.listdir()
    for x in os.listdir(settings.MEDIA_ROOT + "\\" + "profilepic"):
        if x.endswith(".JPG") or x.endswith(".jpg"):
            li.append(x)
    return li


def importBulk(request):
    TeacherModel.objects.all().delete()
    path = settings.MEDIA_ROOT + "\\" + "Teachers.csv"
    import pandas as pd
    df = pd.read_csv(path, encoding='utf-8')
    li = checkData()
    print(li)
    print()
    for i in df.index:
        FirstName = df['First Name'][i]
        LastName = df['Last Name'][i]
        Profilepicture = df['Profile picture'][i]
        EmailAddress = df['Email Address'][i]
        PhoneNumber = df['Phone Number'][i]
        RoomNumber = df['Room Number'][i]
        Subjectstaught = df['Subjects taught'][i]

        pic = 'default.jpg'
        if Profilepicture not in li:
            Profilepicture = pic

        # l2 = len(FirstName)
        sub = Subjectstaught.split(',')
        sub = len(sub)
        if sub <= 5:
            TeacherModel.objects.create(FirstName=FirstName, LastName=LastName, Profilepicture=Profilepicture,
                                        EmailAddress=EmailAddress, PhoneNumber=PhoneNumber, RoomNumber=RoomNumber,
                                        Subjectstaught=Subjectstaught)
        print('First Name', Profilepicture)

    messages.success(request, 'Data Imported')
    return render(request, 'importerform.html', {})


def DataView(request):
    qs = TeacherModel.objects.all()
    return render(request, 'AllData.html', {'data': qs})


def TeacherDirectoryForm(request):
    return render(request, 'FilterForm.html', {})


def FilterTeacherProfile(request):
    from django.db.models import Q
    if request.method == 'POST':
        filtertxt = request.POST.get('filtertext')
        data = TeacherModel.objects.filter(Q(LastName__icontains=filtertxt) | Q(Subjectstaught__icontains=filtertxt))
        return render(request, 'FilterForm.html', {'data': data})


def GetProfilePage(request):
    if request.method == 'GET':
        id = int(request.GET.get('uid'))
        data = TeacherModel.objects.get(id=id)
        return render(request, 'ProfilePage.html', {'data': data})


def AddTeacherData(request):
    if request.method == 'GET':
        return render(request, 'AddTeacherData.html', {})
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        roomnumber = request.POST.get('roomnumber')
        subjects = request.POST.get('subjects')
        TeacherModel.objects.create(FirstName=firstName, LastName=lastName, Profilepicture='default.jpg',
                                    EmailAddress=email, PhoneNumber=mobile, RoomNumber=roomnumber,
                                    Subjectstaught=subjects)
        qs = TeacherModel.objects.all()
        return render(request, 'AllData.html', {'data': qs})
