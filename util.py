import numpy as np

class RiverState():
    def __init__(self, state = None, parent = None, action = None):
        if state is None:
            # cannibals, missionaries, boat
            self.state = np.array([3, 3, 1])
        else:
            self.state = state
        self.parent = parent
        self.action = action
    
    def is_goal_state(self):
        ''' checks to see if state passed is goal state'''
        return np.all(self.state == 0)
    
    def get_child_node(self, action):
        '''returns child node from inputted action'''
        new_state = self.state + action
        return RiverState(new_state,self,action)
    
    def possible_actions(self):
        '''provides valid actions'''
        left_bank_actions = [np.array([-1,0,-1]), np.array([-2,0,-1]), np.array([-1,-1,-1]), np.array([0,-1,-1]), np.array([0,-2,-1])]

        right_bank_actions = [np.array([1,0,1]), np.array([2,0,1]), np.array([1,1,1]), np.array([0,1,1]), np.array([0,2,1])]
        # illegal_states = [np.array([1,2,1]),np.array([1,2,0]),np.array([0,2,1]),np.array([0,2,0]),np.array([0,1,1]),np.array([0,1,0])]
        

        if self.state[2] == 1:
            valid_actions =[]
            for action in left_bank_actions:
                result = self.state + action
                
                if (self.check_conditions(result)):
                    valid_actions.append(action)
            return valid_actions
        elif self.state[2] == 0:
            valid_actions =[]
            for action in right_bank_actions:
                result = self.state + action
             
                if (self.check_conditions(result)):
                    valid_actions.append(action)
            return valid_actions
    
    def check_conditions(self, result):
        cannibals_num = (result[0] >= 0) and (result[0] < 4) # cannibals number 0-3
        missionaries_num = (result[1] >= 0) and (result[1] < 4) # missionaries number 0-3
        boat_num = (result[2] == 1) or (result[2] == 0) # boat number 0-1

        left_side = True
        if result[1] > 0:
            left_side = result[1] >= result[0] # missionaries are equal to or outnumber cannibals on left bank
        
        right_side_1 = True
        if result[1] == 1:
            right_side_1 = result[0] != 0
        
        right_side_2 = True
        if result[1] ==2:
            right_side_2 = result[0] != 0
        right_side_3 = True
        if result[1] ==2:
            right_side_3 = result[0] != 1

        if (cannibals_num == True) and (missionaries_num==True) and (boat_num==True) and left_side==True and right_side_1==True and right_side_2==True and right_side_3==True:
            return True


    def show_state(self):
        return self.state