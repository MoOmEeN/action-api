#!/usr/bin/env python
# -*- coding: utf-8 -*-

import reader_api.token_generator as token_generator
from reader_api.handler.constants import OPERATION, TITLE, ARTICLE_ID, USER_ID, MARK_AS_READ, MARK_AS_UNREAD
from reader_api.config import SELF_URL

def handle(event):
    links = {}
    for id, actions in event['articles'].iteritems():
        for action in actions:
            link = generate_link({
                TITLE: action['title'],
                ARTICLE_ID: id,
                USER_ID: action['user_id'],
                OPERATION: _translate_operation(action['operation'])
            })
            res = {
                'action': action['operation'],
                'link': link
            }
            if id in links:
                links[id].append(res)
            else:
                links[id] = [res]
    return links


def _translate_operation(operation):
    if operation == 'mark_as_read':
        return MARK_AS_READ
    return MARK_AS_UNREAD


def generate_link(payload):
    token = token_generator.encode(payload)
    return SELF_URL + token

