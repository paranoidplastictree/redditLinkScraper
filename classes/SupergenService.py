##########################################################################################
# file: SupergenService.py
# Collects, saves supergens
##########################################################################################

import os
from classes.NoiseMachineService import NoiseMachineService
from classes.SupergenFactory import SupergenFactory
from classes.SupergenRepository import SupergenRepository

nm_svc = NoiseMachineService()
sg_factory = SupergenFactory()

class SupergenService:
    output_path = ""
    sg_repo = {}

    def __init__(self, output_path):
        self.output_path = output_path
        self.sg_repo = SupergenRepository(output_path)
        
    def add(self, submission, title, url):
        noise_machines = nm_svc.get_noise_machines(url)
        supergen = sg_factory.create(submission, title, url, noise_machines)
        self.sg_repo.try_add_supergen(supergen)

    def save_all(self):
        self.sg_repo.save_all()