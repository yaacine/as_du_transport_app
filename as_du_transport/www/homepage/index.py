import frappe
def get_context(context):
    context.users = ["yacine"]
    context.services= frappe.get_list("Service", fields=['name','service_title', 'short_description', 'full_description', 'service_full_image', 'service_short_image'] )
