import frappe
def get_context(context):
    context.about_us= frappe.get_list("A Propos Asdt", fields=['about_asdt'] ,start=0, page_length=1)
    