# profile_system — Django App

A complete customer profile system for the `sms_spam` project.

#urls access
 Done! Access the pages at:

/account/register/ — Register
/account/login/ — Login
/account/logout/ — Logout
/account/profile/ — View profile
/account/profile/edit/ — Edit profile
/account/profile/change-password/ — Change password
/account/profile/delete-account/ — Delete account

## Files
- models.py       — Profile model (linked to Django User via OneToOne + signals)
- forms.py        — Register, Login, Update, PasswordChange forms
- views.py        — All views (register, login, logout, profile, edit, password, delete)
- urls.py         — URL routes under `profile_system:` namespace
- apps.py         — AppConfig with signal registration
- admin.py        — Django admin for Profile
- templates/      — HTML templates
- migrations/     — Django migrations folder

## Integration Steps (see main README)
