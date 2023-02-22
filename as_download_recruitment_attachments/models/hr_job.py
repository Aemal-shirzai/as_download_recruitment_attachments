from odoo import fields, models, api
from odoo.tools.translate import _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from datetime import datetime


import os, base64, zipfile
import tempfile
from tempfile import gettempdir

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




class JobExtended(models.Model):
    _inherit = 'hr.job'


    def open_download_attachments(self):
        self.ensure_one()
        if not self.application_ids:
            return
            
        context = dict(self._context) or {}
        temp_filename = f'aemal.zip' 
        temp_file_path = get_temp_dir()
        
        with zipfile.ZipFile(os.path.join(temp_file_path, temp_filename), 'w') as zipF:
            for rec in self.application_ids:
                for att in rec.attachment_ids:
                    try:
                        key_path = att._full_path(att.store_fname)
                        zipF.write(key_path, f'{rec.name}_{rec.partner_mobile}_{rec.id}/{att.name}', compress_type=zipfile.ZIP_DEFLATED)
                    except:
                        pass

            zipF.close()