# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

search_engine_edge = {
    'color': {
        'color': 'green'
    },
    'title': 'Searching-related Parsing Functions',
    'label': 'Search'
}

def run(unfurl, node):
    if node.data_type == 'url.query.pair':
        if 'google' in unfurl.find_preceding_domain(node):
            if node.key == 'oq':
                unfurl.add_to_queue(
                    data_type='descriptor', key=None, value='"Original" Search Query: {}'.format(node.value),
                    hover='Original terms entered by the user; auto-complete or suggestions <br>'
                          'may have been used to reach the actual search terms (in <b>q</b>)',
                    parent_id=node.node_id, incoming_edge_config=search_engine_edge)

            elif node.key == 'q':
                unfurl.add_to_queue(
                    data_type='descriptor', key=None, value='Search Query: {}'.format(node.value),
                    hover='Terms used in the Google search', parent_id=node.node_id, incoming_edge_config=search_engine_edge)

            elif node.key == 'start':
                unfurl.add_to_queue(
                    data_type='descriptor', key=None, value='Starting Result: {}'.format(node.value),
                    hover='Google search by default shows 10 results per page; higher <br>'
                          '"start" values may indicate browsing more subsequent results pages.',
                    parent_id=node.node_id, incoming_edge_config=search_engine_edge)

        elif 'bing' in unfurl.find_preceding_domain(node):
            if node.key == 'pq':
                unfurl.add_to_queue(
                    data_type='descriptor', key=None, value='"Previous" Search Query: {}'.format(node.value),
                    hover='Previous terms entered by the user; auto-complete or suggestions <br>'
                          'may have been used to reach the actual search terms (in <b>q</b>)',
                    parent_id=node.node_id, incoming_edge_config=search_engine_edge)

            elif node.key == 'q':
                unfurl.add_to_queue(
                    data_type='descriptor', key=None, value='Search Query: {}'.format(node.value),
                    hover='Terms used in the Google search', parent_id=node.node_id, incoming_edge_config=search_engine_edge)

            elif node.key == 'first':
                unfurl.add_to_queue(
                    data_type='descriptor', key=None, value='Starting Result: {}'.format(node.value),
                    hover='Bing search by default shows 8 results per page; higher <br>'
                          '"first" values may indicate browsing more subsequent results pages.',
                    parent_id=node.node_id, incoming_edge_config=search_engine_edge)