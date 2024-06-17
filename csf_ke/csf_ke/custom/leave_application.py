import frappe

from frappe import _
from datetime import datetime
from frappe.utils import getdate
from frappe.utils import add_to_date

def validate(doc, event):
    minimum_days = doc.custom_minimum_leave_application_days
    
    #TODO Skip weekends and holidays

    leave_start_date = getdate(doc.from_date)
    leave_application_date = getdate(doc.posting_date)

    days_to_leave = (leave_start_date - leave_application_date).days

    if (days_to_leave < minimum_days):
        frappe.throw(f"Leave application is {days_to_leave} days to the leave day. Application must be made at least {minimum_days} working days before the leave date.")

