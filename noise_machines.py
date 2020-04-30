
class NoiseMachineManager
    noise_machines = {}
    def __init__():
        __load_noise_machine_info()

    def __load_noise_machine_info():
        # todo: read in from file

    def __parse_noise_machines(url):
        noise_gens = []
        o = urlparse(url)
        if o.netloc != "mynoise.net":
            return []
        qs = parse_qsl(o.query)
        for param in qs:
            match = re.search(".+\.php", param[1])
            if match:
                noise_gens.append(match.group())
        return noise_gens
    
    def __log_missing_noise_machine(noise_machine, url):

    def get_sounds(url):
        sounds = []
        noise_machines = __parse_noise_machines(url)
        for noise_machine_name in noise_machines:
            if noise_machine_name not in noise_machines:



