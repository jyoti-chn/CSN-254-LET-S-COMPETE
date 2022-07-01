from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [

    path('',views.ProductView.as_view(),name="home"),
    path('event-detail/<int:pk>', views.ProductDetailView.as_view(), name='event-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('showevents/', views.show_events, name='showevents'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),

    path('courses/', views.Courses, name='courses'),
    path('courses/<slug:data>', views.Courses, name='coursesdata'),
    path('scholarships/', views.Scholarships, name='scholarships'),
    path('scholarships/<slug:data>', views.Scholarships, name='scholarshipsdata'),
    path('hackathons/', views.Hackathons, name='hackathons'),
    path('hackathons/<slug:data>', views.Hackathons, name='hackathonsdata'),
    path('internships/', views.Internships, name='internships'),
    path('internships/<slug:data>', views.Internships, name='internshipsdata'),
    path('culevents/', views.CulEvents, name='culevents'),
    path('culevents/<slug:data>', views.CulEvents, name='culeventsdata'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    path('orgregistration/', views.OrgRegistrationView.as_view(), name="orgregistration"),
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path('searchbar/',views.searchbar,name='searchbar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
