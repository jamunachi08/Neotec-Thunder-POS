import frappe

@frappe.whitelist()
def ping():
    return {"ok": True, "app": "neotec_fnb", "version": "0.3.0"}
