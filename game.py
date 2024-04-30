import numpy as np
from util import RiverState

class Game():
    def __init__(self):
        self.initial_state = RiverState()

    def breadth_first_search(self):

        start_state = self.initial_state
        #goal_state = RiverState(np.array([0,0,0]))
        explored = []
        frontier = [start_state]

        current_state = frontier.pop(0)
        
        
        while not current_state.is_goal_state():
            
            explored.append(current_state)
            # find actions for current node - 
            actions = current_state.possible_actions()
            for action in actions:
                new_state = current_state.get_child_node(action)
                if new_state not in explored and new_state not in frontier:
                    frontier.append(new_state)
                    
            
            if len(frontier) == 0:
                print("No solution found")
                return None
            
            current_state = frontier.pop(0)
            

        finish_state = current_state

        '''final_path = []
        while current_state.parent is not None:
            final_path.append(current_state)
            current_state = current_state.parent
        
        final_path.append(current_state)

        for state in reversed(final_path):
            print(state.show_state())
'''

        print(finish_state.show_state())
        return finish_state
    
def find_path_to_start(goal_node):
    # Recursively check parent node(s) of the goal_node
    def get_parent_node(node):
        parent_node = node.parent
        #print("-->", parent_node.show_state())
        if parent_node == None:
            return parent_node
        else:
            print("-->", parent_node.show_state())
            get_parent_node(parent_node)
    print("Goal node:", goal_node.show_state())
    start_node = get_parent_node(goal_node)
    return start_node
    

def main():
    g = Game()
    goal_node = g.breadth_first_search()
    print("The goal node is", goal_node.show_state())
    start_node = find_path_to_start(goal_node)

if __name__ == "__main__":
    main()