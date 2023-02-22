from odoo import fields, models, api
from odoo.tools.translate import _
from datetime import datetime
import os, base64, zipfile
import tempfile
import shutil
from tempfile import gettempdir

class JobExtended(models.Model):
    _inherit = 'hr.job'

    def open_download_attachments(self):
        self.ensure_one()
        if not self.application_ids:
            return
            
        context = dict(self._context) or {}
        temp_filename = f'{datetime.now().strftime("%d%m%Y%H%M%S")}.zip' 
        temp_file_path = get_temp_dir()
        
        with zipfile.ZipFile(os.path.join(temp_file_path, temp_filename), 'w') as zipF:
            for rec in self.application_ids:
                for att in rec.attachment_ids:
                    try:
                        key_path = att._full_path(att.store_fname)
                        zipF.write(key_path, f'{rec.partner_name}_{rec.id}_{rec.partner_mobile}/{att.name}', compress_type=zipfile.ZIP_DEFLATED)
                    except:
                        pass

        temp_created_file = open(os.path.join(temp_file_path, temp_filename), "rb")
        export_id = self.env["hr.applicant.download.wizard"].sudo().create({
            "zip_file": base64.encodebytes(temp_created_file.read()),
            "file_name": f"Attachments_of_{self.name}_{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.zip",
            })
        temp_created_file.close()
        delete_directory(temp_file_path)

        return{
            "type": "ir.actions.act_window",
            "res_id": export_id.id,
            "res_model": "hr.applicant.download.wizard",
            "view_type": "form",
            "view_mode": "form",
            "target": "new",
            }


def get_temp_dir():
    """
        This method generate new directory in Temp directory
    """
    temp_directory = tempfile.TemporaryDirectory()
    parent_dir = temp_directory.name
    temp_directory.cleanup()
    while os.path.exists(parent_dir):
        temp_directory = tempfile.TemporaryDirectory()
        parent_dir = temp_directory.name
    dir_name = os.makedirs(parent_dir)
    return parent_dir

def delete_directory(filename):
    '''
        This method deletes directory from Temp directory

        Args:
            filename (str): filename which has to be deleted
    '''
    file_path = os.path.join(gettempdir(), filename)
    try:
        if os.path.exists(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        pass
