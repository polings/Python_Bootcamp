import sys
import argparse
import logging
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote, unquote
import networkx as nx
import json

from src.utils import get_env_var, check_env_var


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--page', type=str, default="Erdős number",
                        help='The name of an existing article')
    parser.add_argument('-d', '--depth', type=int, default=3,
                        help='Max number of links followed in depth')
    return parser.parse_args()


def extract_links(content, graph: list):
    excluded_keywords = ('help:ipa', 'language')
    for link in content.find_all('a', href=True):
        href = link.get('href')
        if href.startswith('/wiki/') and not any(keyword in href.lower() for keyword in excluded_keywords):
            graph.append(unquote(href))


def read_page(page: str, depth: int):
    reqs = requests.get(f"https://en.wikipedia.org/wiki/{quote(page)}")
    links = []
    logging.info(f"Parsing page: {page}")
    if reqs.status_code == 200:
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for paragraph in soup.find_all('p'):
            extract_links(paragraph, links)

        if soup.find('h2', id='See_also'):
            see_also = soup.find('h2', id='See_also').find_next('ul')
            extract_links(see_also, links)

    return links


def create_graph(graph, page, depth):
    if depth == 0:
        return graph

    page = page.removeprefix('/wiki/')
    links = read_page(page, depth)
    for link in links:
        if link.removeprefix('/wiki/') in graph:
            graph.add_edge(page, link.removeprefix('/wiki/'))
        else:
            graph.add_node(link.removeprefix('/wiki/'))
            graph.add_edge(page, link.removeprefix('/wiki/'))
            if graph.number_of_nodes() >= 1000:
                return graph
            else:
                create_graph(graph, link, depth - 1)
    return graph


def main():
    check_env_var()
    args = parse_arguments()
    logging.basicConfig(stream=sys.stdout, level='INFO')

    G = nx.DiGraph(directed=True)
    graph = create_graph(G, args.page, args.depth)
    logging.info(graph)
    data = nx.node_link_data(graph)
    wiki_file = get_env_var("WIKI_FILE")
    with open(wiki_file, "w") as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    main()
