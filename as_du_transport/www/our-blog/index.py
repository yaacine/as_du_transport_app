import frappe
def get_context(context):
    context.blogposts= frappe.get_list(
        "Blog Post ASDT", 
        fields=['name','title', 'read_time', 'published_on', 'published', 'blog_intro', 'blog_content', 'meta_image'], 
        filters={
        'published': 1
        }
    )
    