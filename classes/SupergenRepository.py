##########################################################################################
# file: SupergenRepository.py
# Collects, saves supergens. Acted upon by the SupergenService
##########################################################################################

import modules.fileIO as fileIo
import modules.logger as logger

class SupergenRepository:
    supergen_posts = []
    output_path = ""
    output_filename = "supergenPosts.json"

    def __init__(self, output_path):
        self.output_path = output_path

    def try_add_supergen(self, supergen):
        if (supergen):
            self.supergen_posts.append(supergen)
            return True
        else:
            logger.error("Failed to build supergen")
            return False

    def save_all(self):
        return fileIo.try_write_array(self.supergen_posts, self.output_path, self.output_filename)