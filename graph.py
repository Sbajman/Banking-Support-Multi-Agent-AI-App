# graph.py
from langgraph.graph import Graph

from agents.classify import classify_agent
from agents.response import response_agent
from agents.ticketing import ticketing_agent

graph = Graph()

graph.add_node("classify", classify_agent)
graph.add_node("respond", response_agent)
graph.add_node("ticket", ticketing_agent)

graph.set_entry_point("classify")

graph.add_edge("classify", "respond")
graph.add_edge("respond", "ticket")
graph.set_finish_point("ticket")

support_graph = graph.compile()