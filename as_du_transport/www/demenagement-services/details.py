import frappe
def get_context(context):
    context.single_blog= frappe.get_doc("Service demenagement", frappe.from_dict.docname )
    