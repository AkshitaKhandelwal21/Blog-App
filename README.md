Phase 3: Models (The Heart of Django)

Spend the most time here.

Learn:

Creating models
Field types
Relationships
OneToOne
ForeignKey
ManyToMany

Also learn:

Migrations
makemigrations
migrate
showmigrations
Meta class
__str__()
Model methods

Mini project:

Blog
User
Category
Comment
Phase 4: ORM

This is where people usually become productive.

Master queries.

Create
Read
Update
Delete

Then:

filter()
exclude()
get()
all()
order_by()
values()
values_list()
count()
exists()

Advanced:

select_related()
prefetch_related()
annotate()
aggregate()
Q objects
F objects

Practice until writing SQL feels unnecessary.

Phase 5: Admin Panel

Learn:

admin.py

Customize:

list_display
search_fields
filters
ordering
readonly fields
inline models

Build a polished admin dashboard.

Phase 6: Forms

Understand:

Difference between

HTML Form
↓

Request.POST
↓

Validation
↓

Database

Topics:

Forms
ModelForms
Validation
Widgets
Crispy Forms (optional)

Phase 7: Authentication

Very important.

Learn:

User Model

Then:

Login
Logout
Register
Password hashing
Password reset
Permissions
Groups
Custom user model

Mini project:

Notes App

Phase 8: Class-Based Views

You probably learned function-based views first.

Now understand CBVs.

Start with:

View
TemplateView
ListView
DetailView
CreateView
UpdateView
DeleteView

Then:

LoginRequiredMixin

Later:

FormView
Phase 9: Static & Media Files

Understand the difference.

Static

CSS
JS
Images

vs

Media

User uploads

Learn:

MEDIA_ROOT
MEDIA_URL

STATIC_ROOT
STATIC_URL
Phase 10: Django Signals

Learn:

pre_save
post_save
post_delete

Example:

User created
↓

Automatically create Profile
Phase 11: Middleware

Understand request lifecycle.

Request

↓

Middleware

↓

View

↓

Middleware

↓

Response

Create one custom middleware.