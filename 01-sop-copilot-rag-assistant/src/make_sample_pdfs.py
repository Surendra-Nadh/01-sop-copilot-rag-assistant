"""Generate 15 realistic sample SOP PDFs for demo.
Run: python src/make_sample_pdfs.py
Output: data/sample_sops/*.pdf

This mimics enterprise SOPs. In production you would drop 1,000+ real PDFs here.
"""
import os

SOP_TOPICS = [
    ("Refund Policy", "Online purchases can be refunded within 30 days if item is unused. Refund is processed to original payment mode within 7-10 business days after quality check."),
    ("Password Reset", "Users must reset password every 90 days. Reset via SSO portal. Step 1: Login. Step 2: Forgot password. Step 3: Verify email OTP. Step 4: Set new password with 12 characters including special symbol."),
    ("Leave Policy", "Employees get 24 casual leaves per year. Leave must be applied 3 days in advance. Manager approval required. PTO does not carry forward beyond February."),
    ("Incident Response", "Severity 1 incidents must be acknowledged within 15 minutes. Escalation order: L1 Support -> On-call -> Manager -> CTO. Post-mortem within 48 hours."),
    ("Escalation Matrix", "P1: 15 min response. P2: 2 hours. P3: 8 hours. Matrix defines primary and secondary contacts per region."),
    ("Data Retention", "Logs retained 90 days hot + 1 year cold. Customer data deleted within 30 days of account closure per GDPR."),
    ("Vendor Onboarding", "Vendor KYC requires GST, ISO certificate, NDA. Onboarding SLA is 10 working days. Procurement approval mandatory."),
    ("Expense Rules", "Expenses above Rs 5,000 need manager approval. Receipts mandatory. Submit within 7 days of spending."),
    ("Travel Policy", "Domestic travel: economy class. International below 6 hours: economy, above 6 hours: business. Hotel cap Rs 7,500 per night."),
    ("IT Access", "New hire gets laptop in 2 days. Access requests via ServiceNow. Admin access requires CISO approval."),
    ("Change Management", "All production changes need CAB approval. Change window Sunday 11PM-3AM IST. Rollback plan mandatory."),
    ("Customer Complaint", "Acknowledge complaint within 24 hours. Resolve within 5 business days. Escalate if not resolved to Grievance Officer."),
    ("Quality Check", "QA must test 95% coverage. Defect severity: Critical, Major, Minor. Release blocked if Critical open."),
    ("Backup Procedure", "Full backup daily at 2AM, incremental hourly. RTO 4 hours, RPO 1 hour. Test restore monthly."),
    ("Audit Trail", "All DB changes logged with user, timestamp, before/after values. Audit review quarterly."),
]

def main():
    out_dir = os.path.join(os.path.dirname(__file__), "..", "data", "sample_sops")
    os.makedirs(out_dir, exist_ok=True)

    try:
        from fpdf import FPDF
        use_fpdf = True
    except ImportError:
        use_fpdf = False

    for i, (title, body) in enumerate(SOP_TOPICS, start=1):
        filename = f"SOP_{i:02d}_{title.replace(' ','_')}.pdf"
        path = os.path.join(out_dir, filename)

        if use_fpdf:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 15)
            pdf.multi_cell(0, 10, f"SOP Document {i}: {title}")
            pdf.set_font("Arial", "", 11)
            pdf.multi_cell(0, 7, f"Purpose: This SOP defines the procedure for {title}.")
            pdf.multi_cell(0, 7, f"Procedure: {body} Section 2 Scope. Section 3 Roles. Section 4 Step-by-step. Section 5 Escalation. " * 3)
            pdf.ln(4)
            pdf.multi_cell(0, 7, body)
            pdf.output(path)
        else:
            # Fallback: plain text PDF placeholder (pypdf can't read, so create text file only)
            with open(path.replace(".pdf", ".txt"), "w", encoding="utf-8") as f:
                f.write(f"SOP Document {i}: {title}\n\n{body}\n")
            print(f"WARN: fpdf not installed, wrote .txt instead for {title}. Run: pip install fpdf2")

        print(f"Created {filename}")

    print(f"\nDone. PDFs in {out_dir}. Next: python src/ingest.py")

if __name__ == "__main__":
    main()
