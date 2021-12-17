from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile as User
import random

# import solana
# # from spl.token import constants, client, instructions
# from solana import account


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "DCXA-XXXXXX",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Passcode",
                "class": "form-control"
            }
        ))



class SignUpForm(UserCreationForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Full Name",
                "class": "form-control"
            }
        ))
    referal_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sponsor",
                "class": "form-control",
                "value": "DCXa-XXXXXX",
                "onclick": "$('#id_referal_code').val('DCXa-')",
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    mob = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mobile",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Passcode",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))
    cc = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Country Code",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2', 'referal_code', 'username')

    def clean_name(self):
        name = self.cleaned_data['name']
        return name[0].upper() + name[1:].lower()

    def clean_username(self):
        def generateuser():
            r = random.randint(100001,999998)
            u = User.objects.filter(username='DCXa-{}'.format(r)).count()
            if u > 0:
                generateuser()
            else:
                return 'DCXa-{}'.format(r)
        u = generateuser()
        username = u
        return username

    def save(self, request):
        # user = User(username = self.clean_username())
        user = super(SignUpForm, self).save(request)
        referral = self.cleaned_data['referal_code']
        cc = self.cleaned_data['cc']
        try:
            userr = User.objects.get(username=referral)
        except Exception as e:
            userr = 'blank'
        if userr == 'blank':
            referral = 'DCXa-999999'
        # plan = UserTotal()
        # plan.user = user
        # plan.amount = 0
        # plan.active = False
        # plan.left_months = 0
        # plan.direct = referral
        # plan.save()
        # subject = 'Welcome to IPAYMATICS Inc.'
        # html_message = render_to_string('account/email/welcome.html', {'context': self.cleaned_data['name']})
        # plain_message = strip_tags(html_message)
        # from_email = 'support@ipaymatics.com'
        # to = user.email

        # mail.send_mail(subject=subject, message=plain_message, from_email=from_email, recipient_list=[to], html_message=html_message)
        # url = "http://2factor.in/API/V1/99254625-e54d-11eb-8089-0200cd936042/ADDON_SERVICES/SEND/PSMS"
        # payload = "{'From': 'TFCTOR', 'Msg': 'Hello World', 'To': '7000934949,'}"
        # response = requests.request("GET", url, data=payload)
        # print(response.text)
        user.mobile = cc + self.cleaned_data['mob']
        # acct = Account.create('{} {}'.format(self.cleaned_data['name'], self.cleaned_data['password1']))
        # sacct = account.Account()
        # user.swaddress = sacct.public_key()
        # user.sprkey = sacct.secret_key().hex()
        # user.prkey = acct.privateKey.hex()
        # user.waddress = acct.address

        user.name = self.cleaned_data['name']
        user.referral = referral
        user.username = self.clean_username()
        user.save()
        return user
