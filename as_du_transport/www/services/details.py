import frappe
def get_context(context):
    context.single_service= frappe.get_doc("Service", frappe.form_dict.docname )
    context.services= frappe.get_list("Service", fields=['name','service_title', 'short_description', 'full_description', 'service_full_image', 'service_short_image'] )
    
    




    