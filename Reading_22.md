# Reading: Django Forms

Building a form¶

<form action="/your-name/" method="post">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
    <input type="submit" value="OK">
</form>

This tells the browser to return the form data to the URL /your-name/, using the POST method. It will display a text field, labeled “Your name:”, and a button marked “OK”. If the template context contains a current_name variable, that will be used to pre-fill the your_name field.

You’ll need a view that renders the template containing the HTML form, and that can supply the current_name field as appropriate.

When the form is submitted, the POST request which is sent to the server will contain the form data.

Now you’ll also need a view corresponding to that /your-name/ URL which will find the appropriate key/value pairs in the request, and then process them.

This is a very simple form. In practice, a form might contain dozens or hundreds of fields, many of which might need to be pre-populated, and we might expect the user to work through the edit-submit cycle several times before concluding the operation.

We might require some validation to occur in the browser, even before the form is submitted; we might want to use much more complex fields, that allow the user to do things like pick dates from a calendar and so on.

At this point it’s much easier to get Django to do most of this work for us.

# Building a form in Django¶

The Form class¶
We already know what we want our HTML form to look like. Our starting point for it in Django is this:

`forms.py¶`
`from django import forms`

`class NameForm(forms.Form):`
    `your_name = forms.CharField(label='Your name', max_length=100)`
This defines a Form class with a single field (your_name). We’ve applied a human-friendly label to the field, which will appear in the <label> when it’s rendered (although in this case, the label we specified is actually the same one that would be generated automatically if we had omitted it).

The field’s maximum allowable length is defined by max_length. This does two things. It puts a maxlength="100" on the HTML <input> (so the browser should prevent the user from entering more than that number of characters in the first place). It also means that when Django receives the form back from the browser, it will validate the length of the data.

A Form instance has an is_valid() method, which runs validation routines for all its fields. When this method is called, if all fields contain valid data, it will:

return True
place the form’s data in its cleaned_data attribute.
The whole form, when rendered for the first time, will look like:

`<label for="your_name">Your name: </label>`
`<input id="your_name" type="text" name="your_name" maxlength="100" required>`
Note that it does not include the <form> tags, or a submit button. We’ll have to provide those ourselves in the template.

The view¶
Form data sent back to a Django website is processed by a view, generally the same view which published the form. This allows us to reuse some of the same logic.

To handle the form we need to instantiate it in the view for the URL where we want it to be published:

`views.py¶`
`from django.http import HttpResponseRedirect`
`from django.shortcuts import render`

`from .forms import NameForm`

`def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()`

    return render(request, 'name.html', {'form': form})
If we arrive at this view with a GET request, it will create an empty form instance and place it in the template context to be rendered. This is what we can expect to happen the first time we visit the URL.

If the form is submitted using a POST request, the view will once again create a form instance and populate it with data from the request: form = NameForm(request.POST) This is called “binding data to the form” (it is now a bound form).

We call the form’s is_valid() method; if it’s not True, we go back to the template with the form. This time the form is no longer empty (unbound) so the HTML form will be populated with the data previously submitted, where it can be edited and corrected as required.

If is_valid() is True, we’ll now be able to find all the validated form data in its cleaned_data attribute. We can use this data to update the database or do other processing before sending an HTTP redirect to the browser telling it where to go next.

The template¶
We don’t need to do much in our name.html template:

<form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>
All the form’s fields and their attributes will be unpacked into HTML markup from that {{ form }} by Django’s template language.

Forms and Cross Site Request Forgery protection

Django ships with an easy-to-use protection against Cross Site Request Forgeries. When submitting a form via POST with CSRF protection enabled you must use the csrf_token template tag as in the preceding example. However, since CSRF protection is not directly tied to forms in templates, this tag is omitted from the following examples in this document.

HTML5 input types and browser validation

If your form includes a URLField, an EmailField or any integer field type, Django will use the url, email and number HTML5 input types. By default, browsers may apply their own validation on these fields, which may be stricter than Django’s validation. If you would like to disable this behavior, set the novalidate attribute on the form tag, or specify a different widget on the field, like TextInput.

We now have a working web form, described by a Django Form, processed by a view, and rendered as an HTML <form>.

That’s all you need to get started, but the forms framework puts a lot more at your fingertips. Once you understand the basics of the process described above, you should be prepared to understand other features of the forms system and ready to learn a bit more about the underlying machinery.

More about Django Form classes¶
All form classes are created as subclasses of either django.forms.Form or django.forms.ModelForm. You can think of ModelForm as a subclass of Form. Form and ModelForm actually inherit common functionality from a (private) BaseForm class, but this implementation detail is rarely important.

Models and Forms

In fact if your form is going to be used to directly add or edit a Django model, a ModelForm can save you a great deal of time, effort, and code, because it will build a form, along with the appropriate fields and their attributes, from a Model class.

Bound and unbound form instances¶
The distinction between Bound and unbound forms is important:

An unbound form has no data associated with it. When rendered to the user, it will be empty or will contain default values.
A bound form has submitted data, and hence can be used to tell if that data is valid. If an invalid bound form is rendered, it can include inline error messages telling the user what data to correct.
The form’s is_bound attribute will tell you whether a form has data bound to it or not.

More on fields¶
Consider a more useful form than our minimal example above, which we could use to implement “contact me” functionality on a personal website:

forms.py¶
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
Our earlier form used a single field, your_name, a CharField. In this case, our form has four fields: subject, message, sender and cc_myself. CharField, EmailField and BooleanField are just three of the available field types; a full list can be found in Form fields.

Widgets¶
Each form field has a corresponding Widget class, which in turn corresponds to an HTML form widget such as <input type="text">.

In most cases, the field will have a sensible default widget. For example, by default, a CharField will have a TextInput widget, that produces an <input type="text"> in the HTML. If you needed <textarea> instead, you’d specify the appropriate widget when defining your form field, as we have done for the message field.

Field data¶
Whatever the data submitted with a form, once it has been successfully validated by calling is_valid() (and is_valid() has returned True), the validated form data will be in the form.cleaned_data dictionary. This data will have been nicely converted into Python types for you.

Note

You can still access the unvalidated data directly from request.POST at this point, but the validated data is better.

In the contact form example above, cc_myself will be a boolean value. Likewise, fields such as IntegerField and FloatField convert values to a Python int and float respectively.

Here’s how the form data could be processed in the view that handles this form:

views.py¶
from django.core.mail import send_mail

if form.is_valid():
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']

    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect('/thanks/')
Tip

For more on sending email from Django, see Sending email.

Some field types need some extra handling. For example, files that are uploaded using a form need to be handled differently (they can be retrieved from request.FILES, rather than request.POST). For details of how to handle file uploads with your form, see Binding uploaded files to a form.

Working with form templates¶
All you need to do to get your form into a template is to place the form instance into the template context. So if your form is called form in the context, {{ form }} will render its <label> and <input> elements appropriately.

Form rendering options¶
Additional form template furniture

Don’t forget that a form’s output does not include the surrounding <form> tags, or the form’s submit control. You will have to provide these yourself.

There are other output options though for the <label>/<input> pairs:

{{ form.as_table }} will render them as table cells wrapped in <tr> tags
{{ form.as_p }} will render them wrapped in <p> tags
{{ form.as_ul }} will render them wrapped in <li> tags
Note that you’ll have to provide the surrounding <table> or <ul> elements yourself.

Here’s the output of {{ form.as_p }} for our ContactForm instance:

<p><label for="id_subject">Subject:</label>
    <input id="id_subject" type="text" name="subject" maxlength="100" required></p>
<p><label for="id_message">Message:</label>
    <textarea name="message" id="id_message" required></textarea></p>
<p><label for="id_sender">Sender:</label>
    <input type="email" name="sender" id="id_sender" required></p>
<p><label for="id_cc_myself">Cc myself:</label>
    <input type="checkbox" name="cc_myself" id="id_cc_myself"></p>
Note that each form field has an ID attribute set to id_<field-name>, which is referenced by the accompanying label tag. This is important in ensuring that forms are accessible to assistive technology such as screen reader software. You can also customize the way in which labels and ids are generated.

See Outputting forms as HTML for more on this.

Rendering fields manually¶
We don’t have to let Django unpack the form’s fields; we can do it manually if we like (allowing us to reorder the fields, for example). Each field is available as an attribute of the form using {{ form.name_of_field }}, and in a Django template, will be rendered appropriately. For example:

{{ form.non_field_errors }}
<div class="fieldWrapper">
    {{ form.subject.errors }}
    <label for="{{ form.subject.id_for_label }}">Email subject:</label>
    {{ form.subject }}
</div>
<div class="fieldWrapper">
    {{ form.message.errors }}
    <label for="{{ form.message.id_for_label }}">Your message:</label>
    {{ form.message }}
</div>
<div class="fieldWrapper">
    {{ form.sender.errors }}
    <label for="{{ form.sender.id_for_label }}">Your email address:</label>
    {{ form.sender }}
</div>
<div class="fieldWrapper">
    {{ form.cc_myself.errors }}
    <label for="{{ form.cc_myself.id_for_label }}">CC yourself?</label>
    {{ form.cc_myself }}
</div>
Complete <label> elements can also be generated using the label_tag(). For example:

<div class="fieldWrapper">
    {{ form.subject.errors }}
    {{ form.subject.label_tag }}
    {{ form.subject }}
</div>
Rendering form error messages¶
The price of this flexibility is a bit more work. Until now we haven’t had to worry about how to display form errors, because that’s taken care of for us. In this example we have had to make sure we take care of any errors for each field and any errors for the form as a whole. Note {{ form.non_field_errors }} at the top of the form and the template lookup for errors on each field.

Using {{ form.name_of_field.errors }} displays a list of form errors, rendered as an unordered list. This might look like:

<ul class="errorlist">
    <li>Sender is required.</li>
</ul>
The list has a CSS class of errorlist to allow you to style its appearance. If you wish to further customize the display of errors you can do so by looping over them:

{% if form.subject.errors %}
    <ol>
    {% for error in form.subject.errors %}
        <li><strong>{{ error|escape }}</strong></li>
    {% endfor %}
    </ol>
{% endif %}
Non-field errors (and/or hidden field errors that are rendered at the top of the form when using helpers like form.as_p()) will be rendered with an additional class of nonfield to help distinguish them from field-specific errors. For example, {{ form.non_field_errors }} would look like:

<ul class="errorlist nonfield">
    <li>Generic validation error</li>
</ul>
See The Forms API for more on errors, styling, and working with form attributes in templates.

Looping over the form’s fields¶
If you’re using the same HTML for each of your form fields, you can reduce duplicate code by looping through each field in turn using a {% for %} loop:

{% for field in form %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
        {% if field.help_text %}
        <p class="help">{{ field.help_text|safe }}</p>
        {% endif %}
    </div>
{% endfor %}
Useful attributes on {{ field }} include:

{{ field.label }}
The label of the field, e.g. Email address.
{{ field.label_tag }}
The field’s label wrapped in the appropriate HTML <label> tag. This includes the form’s label_suffix. For example, the default label_suffix is a colon:

<label for="id_email">Email address:</label>
{{ field.id_for_label }}
The ID that will be used for this field (id_email in the example above). If you are constructing the label manually, you may want to use this in lieu of label_tag. It’s also useful, for example, if you have some inline JavaScript and want to avoid hardcoding the field’s ID.
{{ field.value }}
The value of the field. e.g someone@example.com.
{{ field.html_name }}
The name of the field that will be used in the input element’s name field. This takes the form prefix into account, if it has been set.
{{ field.help_text }}
Any help text that has been associated with the field.
{{ field.errors }}
Outputs a <ul class="errorlist"> containing any validation errors corresponding to this field. You can customize the presentation of the errors with a {% for error in field.errors %} loop. In this case, each object in the loop is a string containing the error message.
{{ field.is_hidden }}
This attribute is True if the form field is a hidden field and False otherwise. It’s not particularly useful as a template variable, but could be useful in conditional tests such as:
{% if field.is_hidden %}
   {# Do something special #}
{% endif %}
{{ field.field }}
The Field instance from the form class that this BoundField wraps. You can use it to access Field attributes, e.g. {{ char_field.field.max_length }}.
See also

For a complete list of attributes and methods, see BoundField.

Looping over hidden and visible fields¶
If you’re manually laying out a form in a template, as opposed to relying on Django’s default form layout, you might want to treat <input type="hidden"> fields differently from non-hidden fields. For example, because hidden fields don’t display anything, putting error messages “next to” the field could cause confusion for your users – so errors for those fields should be handled differently.

Django provides two methods on a form that allow you to loop over the hidden and visible fields independently: hidden_fields() and visible_fields(). Here’s a modification of an earlier example that uses these two methods:

{# Include the hidden fields #}
{% for hidden in form.hidden_fields %}
{{ hidden }}
{% endfor %}
{# Include the visible fields #}
{% for field in form.visible_fields %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
    </div>
{% endfor %}
This example does not handle any errors in the hidden fields. Usually, an error in a hidden field is a sign of form tampering, since normal form interaction won’t alter them. However, you could easily insert some error displays for those form errors, as well.

Reusable form templates¶
If your site uses the same rendering logic for forms in multiple places, you can reduce duplication by saving the form’s loop in a standalone template and using the include tag to reuse it in other templates:

# In your form template:
{% include "form_snippet.html" %}

# In form_snippet.html:
{% for field in form %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
    </div>
{% endfor %}
If the form object passed to a template has a different name within the context, you can alias it using the with argument of the include tag:

{% include "form_snippet.html" with form=comment_form %}