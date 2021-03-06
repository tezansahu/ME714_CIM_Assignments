from graphviz import Digraph

g1 = Digraph('a4_q2_1', filename='a4_q2_1', format="png", node_attr={'shape': 'circle'})
g1.attr(rankdir='LR', ratio='0.5')
g1.edge('1', '2', label='A (2)')
g1.edge('1', '3', label='B (6)')
g1.edge('1', '4', label='C (4)')
g1.edge('2', '5', label='D (3)')
g1.edge('2', '6', label='F (4)')
g1.edge('4', '7', label='E (5)')
g1.edge('5', '8', style="dashed")
g1.edge('3', '8', style="dashed")
g1.edge('7', '8', style="dashed")
g1.edge('8', '9', label='G (2)')
g1.edge('6', '10', style="dashed")
g1.edge('9', '10', style="dashed")
g1.view()

g2 = Digraph('a4_q2_2', filename='a4_q2_2', format="png", node_attr={'shape': 'circle'})
g2.attr(rankdir='LR', ratio='0.5')
g2.edge('1', '2', label='A (2)')
g2.edge('1', '4', label='B (6)')
g2.edge('1', '3', label='C (4)')
g2.edge('2', '4', label='D (3)')
g2.edge('2', '5', label='F (4)')
g2.edge('3', '4', label='E (5)')
g2.edge('4', '5', label='G (2)')
g2.view()