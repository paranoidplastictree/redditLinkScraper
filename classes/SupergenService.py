##########################################################################################
# file: SupergenService.py
# Collects, saves supergens
##########################################################################################

import os
import modules.fileIO as io
import modules.logger as logger
from classes.NoiseMachineService import NoiseMachineService
from classes.SupergenFactory import SupergenFactory
from classes.SupergenRepository import SupergenRepository

output_path = "c:/tim/paranoidplastictree/redditLinkScraper/data/output/"
nm_svc = NoiseMachineService()
sg_factory = SupergenFactory()

class SupergenService:
    output_path = ""
    sg_repo = {}

    def __init__(self, output_path):
        self.output_path = output_path
        self.sg_repo = SupergenRepository(output_path)
        
    def add(self, submission, title, url):
        undefined_noise_machine_names = []
        try:
            noise_machines, undefined_noise_machine_names = nm_svc.get_noise_machines(url)
            assert(len(undefined_noise_machine_names) == 0), "A referenced noise machine is not defined"
        except ValueError as e:
            # Url not a noise machine
            logger.info("{}: post Id: {} - {}".format(e, submission["id"], url))
            return
        except AssertionError as e:
            # Not all noise machine references were found in lookup/noseGeneratorInfo_hydrated.json
            # Some (maybe all?) of these are legitimate and need to be added to the lookup.
            logger.error("{}: post Id: {} - {}".format(e, submission["id"], url))
            print("Post Id: {} - {} ".format(submission["id"], e))
            json = {
                "post": submission,
                "undefined_noise_machines": undefined_noise_machine_names
            }
            io.write_dict(json, output_path, "posts_with_undefined_noise_machines.jsonl")
            return

        supergen = sg_factory.create(submission, title, url, noise_machines)
        self.sg_repo.try_add_supergen(supergen)

    def save_all(self):
        self.sg_repo.save_all()