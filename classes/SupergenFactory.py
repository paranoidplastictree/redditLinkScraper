##########################################################################################
# file: NoiseMachineService.py
# Serves up noise machine meta (gathered by supergen_scraper project)
##########################################################################################

import modules.logger as logger
import json

class SupergenFactory:
    required_nm_per_supergen = 2

    def __validate_noise_machines(self, post_id, noise_machines):
        if len(noise_machines) < self.required_nm_per_supergen:
            msg = "Not enough noise machines for post_id " + str(post_id)
            logger.warn(msg)
            print(msg)
            return False
        return True

    def create(self, post, title, url, noise_machines):
        validated = self.__validate_noise_machines(post["id"], noise_machines)
        if (validated == False): return

        return {
            "post_id": post["id"],
            "author": post["author"],
            "created_utc": post["created_utc"],
            "reddit_url": post["full_link"],
            "url": url,
            "title": title,
            "noise_machines": noise_machines
        }