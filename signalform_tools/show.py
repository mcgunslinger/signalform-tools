# -*- coding: utf-8 -*-
import json
from itertools import chain


SIGNALFX_API = 'https://app.signalfx.com/#/'


TYPE_MAPPING = {
    'signalform_detector': 'detector',
    'signalform_time_chart': 'chart',
    'signalform_heatmap_chart': 'chart',
    'signalform_single_value_chart': 'chart',
    'signalform_list_chart': 'chart',
    'signalform_text_chart': 'chart',
    'signalform_dashboard': 'dashboard',
}


def show(resource):
    try:
        res_type = TYPE_MAPPING[resource['type']]
        print(res_type)
        print(resource['primary']['attributes']['name'])
        url = SIGNALFX_API + res_type \
            + '/' + resource['primary']['attributes']['id']
        if res_type == 'detector':
            url += '/edit'
        print(url + '\n')
    except KeyError:
        pass


def parse_resources(state):
    return chain.from_iterable(module['resources'].values()
                               for module in state['modules'])


def parse_state(state_file):
    state = json.load(state_file)
    resources = parse_resources(state)
    [show(resource) for resource in resources]


def show_signalform(args):
    try:
        with open("terraform.tfstate", "r") as state:
            parse_state(state)
    except FileNotFoundError:
        print('No state')