from odoo import fields, models, api

class AttachmentDownloadWizard(models.Model):
    _name = "hr.applicant.download.wizard"
    _description = "Download Application Attachments"

    zip_file = fields.Binary("Download report Excel")
    file_name = fields.Char("Zip File", size=64)

    def emp_download_report(self):
        return{
            "type": "ir.actions.act_url",
            "url": f"web/content/?model=hr.applicant.download.wizard&field=zip_file&download=true&id={self.id}&filename={self.file_name}",
            "target": "new",
            }
