##########################################################################################
# file: NoiseMachineService.py
# Serves up noise machine meta (gathered by supergen_scraper project)
##########################################################################################

import modules.logger as logger
import json
import re
from urllib.parse import urlparse, parse_qsl

# hydrated file is generated and hydrated by the supergen_scraper project
ng_info_filename = "c:/dev/redditLinkScraper/data/noiseGeneratorInfo_hydrated.json"

class NoiseMachineService:
    __noise_machines = {}
    __noise_machine_categories = []

    def __init__(self):
        self.__load_noise_machine_info()

    def __load_noise_machine_info(self):
        f = open(ng_info_filename)
        data = json.loads(f)
        f.close()
        pattern = r"(?i)(?<=(.*NoiseMachines/)).+"
        for nm in data.noiseMachines:
            nm_name = re.search(pattern, nm["href"])
            # need to handle custom.php: [Can't Take The Sky From Me](https://mynoise.net/NoiseMachines/custom.php?l=3035403037323015253200&amp;m=CINEMATIC1~INTERGALACTIC1~BATTLE1~EASTASIA2~CINEMATIC3~CANYON5~EASTASIA6~CANYON7~EASTASIA7~CINEMATIC9&amp;d=0&amp;title=Can't%20Take%20The%20Sky%20From%20Me)",
            if (nm_name):
                if nm_name not in self.__noise_machines:
                   self. __noise_machines[nm_name] = nm
                else:
                    logger.info("Noise machine already exists for: {}".format(nm_name))
            else:
                logger.info("Could not parse noise machine HREF: {}".format(nm["href"]))

    def __parse_noise_machines_from_url(self, url):
        noise_gens = []
        o = urlparse(url)
        if o.netloc != "mynoise.net":
            return []
        qs = parse_qsl(o.query)
        for param in qs:
            match = re.search(r".+\.php", param[1])
            if match:
                noise_gens.append(match.group())
        return noise_gens
    
    def get_noise_machines(self, url):
        supergen_nms = []
        noise_machine_names = self.__parse_noise_machines_from_url(url)
        for noise_machine_name in noise_machine_names:
            if noise_machine_name not in self.__noise_machines:
                logger.error("Couldn't find noise machine {}. Consider scraping title at url: {}".format(noise_machine_name, url))
                # TODO: attempt scrape automatically?
            else:
                nm = self.__noise_machines[noise_machine_name]
                if (nm):
                    supergen_nms.append({nm})
        return supergen_nms
