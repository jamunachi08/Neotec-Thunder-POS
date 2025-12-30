import frappe

@frappe.whitelist()
def ping():
    return {"ok": True, "app": "neotec_thunder_pos"}
