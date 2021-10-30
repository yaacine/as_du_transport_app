import frappe
def get_context(context):
    context.users = ["yacine"]
    context.demandes_devis= frappe.get_list("Demande Devis", fields=['full_name', 'email'])