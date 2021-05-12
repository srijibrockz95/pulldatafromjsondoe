"""
This script runs the PulloutfromJson application using a development server.
"""

import Pullout
from Pullout import configs
from Pullout.views import jmonitor

bp_list = [jmonitor,]

app = Pullout.create_app(config_map_list= configs.prod_configs_from_file,
                      blue_print_list=bp_list)
