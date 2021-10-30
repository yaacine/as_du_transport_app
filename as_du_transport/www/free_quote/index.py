import frappe
def get_context(context):
    context.users = ["yacine"]
    context.demandes_devis= frappe.get_list("Demande Devis", fields=['full_name', 'email'])
    context.blogposts= frappe.get_list("Blog Post ASDT", fields=['title', 'read_time', 'published_on', 'published', 'blog_intro', 'blog_content', 'meta_image'])