from . import __version__ as app_version

from as_du_transport.routes import routes

app_name = "as_du_transport"
app_title = "As Du Transport"
app_publisher = "yacine"
app_description = "app to manage asDuTransport doctypes"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "yacine.zidel@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/as_du_transport/css/as_du_transport.css"
# app_include_js = "/assets/as_du_transport/js/as_du_transport.js"

# include js, css files in header of web template
# web_include_css = "/assets/as_du_transport/css/as_du_transport.css"
# web_include_js = "/assets/as_du_transport/js/as_du_transport.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "as_du_transport/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }


website_route_rules = routes 


# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "as_du_transport.install.before_install"
# after_install = "as_du_transport.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "as_du_transport.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"as_du_transport.tasks.all"
# 	],
# 	"daily": [
# 		"as_du_transport.tasks.daily"
# 	],
# 	"hourly": [
# 		"as_du_transport.tasks.hourly"
# 	],
# 	"weekly": [
# 		"as_du_transport.tasks.weekly"
# 	]
# 	"monthly": [
# 		"as_du_transport.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "as_du_transport.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "as_du_transport.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "as_du_transport.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"as_du_transport.auth.validate"
# ]

