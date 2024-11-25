import matplotlib.pyplot as plt
import random
import networkx as nx
from bokeh.palettes import Category20
from bokeh.plotting import figure, from_networkx, show, output_file, save
from bokeh.models import Circle, MultiLine, HoverTool

from src.utils import load_graph


def kamada_kawai_graph(G, in_degrees, out_degrees):
    pos = nx.kamada_kawai_layout(G, scale=5)
    node_sizes = {node: in_degrees[node] * 300 for node in G.nodes()}
    filtered_labels = {
        node: node
        for node in G.nodes()
        if in_degrees[node] > 1 or out_degrees[node] >= 2
    }
    plt.figure(figsize=(30, 30))
    nx.draw_networkx_nodes(G, pos, node_size=[node_sizes[node] for node in G.nodes()], alpha=0.85)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos, labels=filtered_labels, font_size=8, font_color="darkblue")
    plt.savefig('wiki_graph.png', dpi=300)


def spring_graph(G, in_degrees, out_degrees):
    node_sizes = {node: degree * 0.1 for node, degree in in_degrees.items()}
    nx.set_node_attributes(G, in_degrees, "in_degree")
    nx.set_node_attributes(G, out_degrees, "out_degrees")
    nx.set_node_attributes(G, node_sizes, "node_size")
    random_colors = [random.choice(Category20[20]) for _ in G.nodes()]

    # Plot
    plot = figure(
        title="Wiki Graph Visualization with Bokeh",
        width=1000,
        height=1000,
        tools="pan,box_zoom,wheel_zoom,reset,save",
        active_scroll="wheel_zoom",
        match_aspect=True,
        sizing_mode="scale_both"
    )
    plot.axis.visible = False
    plot.grid.visible = False

    # Layout
    layout = nx.spring_layout(G, seed=42, k=0.3)
    scale_factor = 5
    scaled_layout = {node: (pos[0] * scale_factor, pos[1] * scale_factor) for node, pos in layout.items()}
    graph_renderer = from_networkx(G, scaled_layout)

    # Node attributes
    node_source = graph_renderer.node_renderer.data_source
    node_source.data["node_size"] = [node_sizes[node] for node in G.nodes()]
    node_source.data["in_degree"] = [in_degrees[node] for node in G.nodes()]
    node_source.data["out_degree"] = [out_degrees[node] for node in G.nodes()]
    node_source.data["color"] = random_colors

    # Node style
    graph_renderer.node_renderer.glyph = Circle(radius="node_size", fill_color="color")
    graph_renderer.node_renderer.hover_glyph = Circle(radius="node_size", fill_color="red")

    # Edges style
    graph_renderer.edge_renderer.glyph = MultiLine(line_color="black", line_alpha=0.4, line_width=1)

    # Hoover tool for nodes
    hover_tool = HoverTool(tooltips=[("Node", "@index"), ("In degree", "@in_degree"), ("Out degree", "@out_degree")])
    plot.add_tools(hover_tool)

    plot.renderers.append(graph_renderer)
    output_file("wiki_graph.html")
    save(plot)
    show(plot)


def main():
    G = load_graph(non_directed=False)
    in_deg = dict(G.in_degree())
    out_deg = dict(G.out_degree())

    kamada_kawai_graph(G, in_deg, out_deg)
    spring_graph(G, in_deg, out_deg)


if __name__ == '__main__':
    main()
