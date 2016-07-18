# -*- coding: utf-8 -*-
'''
Salt only merges top.sls contained in differents `saltenv`, but SUSE Manager
provides the feature of define differents top.sls files in the differents
`file_roots` directories of the `base` saltenv.

This module merge top.sls files contained in the differents `file_roots`
defined for the `base` saltenv and returns a the entire highstate information
contained in the differents top.sls files.

.. code-block:: yaml

    master_tops:
        - susemanager_mastertops: True
'''

# Import python libs
from __future__ import absolute_import
import logging
import yaml
import os
import copy
from salt.state import HighState

# Define the module's virtual name
__virtualname__ = 'susemanager_mastertops'

log = logging.getLogger(__name__)


def __virtual__():
    '''
    Ensure the module name.
    '''
    return __virtualname__


def top(**kwargs):
    '''
    Returns state information for a minion based on merged top.sls files
    of `base` salt environment in `file_roots`.
    '''
    if kwargs['opts']['environment'] not in [None, "base"]:
        log.debug('Omitting merge of top.sls files outside "base" saltenv: %s',
                  kwargs['opts']['environment'])
        return {}

    log.debug('Merging top.sls files in: %s', __opts__['file_roots']['base'])

    top_tree = {"base": []}
    opts = copy.deepcopy(__opts__)
    opts['id'] = kwargs['grains']['id']
    opts['grains'] = kwargs['grains']
    opts['environment'] = "base"

    for top_path in __opts__['file_roots']['base']:
        top_file = os.path.join(top_path, "top.sls")
        if os.path.isfile(top_file):
            file_roots_prio = [top_path] + list(set(__opts__['file_roots']['base']) - set([top_path]))
            opts['file_roots'] = {"base": file_roots_prio}

            st_ = HighState(opts)
            top_ = st_.get_top()
            top_info = st_.top_matches(top_)
            top_tree['base'].extend(top_info.get("base"))
    return top_tree
