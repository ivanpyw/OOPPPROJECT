class Request:
   #patient_id, bed_no, ward, assitant_required , nurse_id

    def __init__(self, patient_id, bed_no, ward, assitant_required):
        self.patient_id = patient_id
        self.bed_no = bed_no
        self.ward = ward
        self.assitant_required = assitant_required
        self.nurse_id = ''
        self.status = 'NEW' #completed, attended, new

