import os
import json
import networkx as nx


def set_env_var(var_name: str, value: str):
    os.environ[var_name] = value


def get_env_var(var_name: str) -> str:
    return os.getenv(var_name, "")


def check_env_var():
    """
    Ensures the WIKI_FILE environment variable is set. Dynamically sets it
    if not already defined, based on the current operating system.
    """
    var_name = "WIKI_FILE"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_path = os.path.abspath(os.path.join(script_dir, "resources", "wiki.json"))
    if not os.getenv(var_name):
        set_env_var(var_name, default_path)


def load_graph(non_directed: bool = False) -> nx.Graph:
    check_env_var()
    file_path = get_env_var("WIKI_FILE")
    if not os.path.exists(file_path):
        print("Database not found.")
        exit(-1)
    if not os.path.getsize(file_path):
        print("Database is empty.")
        exit(-1)
    with open(file_path, "r") as json_file:
        G = nx.node_link_graph(json.load(json_file))
    if non_directed:
        G = G.to_undirected()
    return G
