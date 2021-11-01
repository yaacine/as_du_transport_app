import frappe

def get_context(context):
    context.company_logo= frappe.get_all("Logo Entreprise", fields=['image'], start=0, page_length=1)
    context.company_contacts= frappe.get_all("Contacts", fields=['mobile','email','telephone','adresse','facebook_account','twitter_account','linkedin_account'], start=0, page_length=1)
    