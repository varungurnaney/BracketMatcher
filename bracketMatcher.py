class BracketsMatcher: 
    def __init__(self):
        self.map_brackets = {
            "(":")",
            "[":"]",
            "{":"}"
        } 

        #create sets of open and close brackets
        self.open_brackets = set(self.map_brackets.keys())
        self.close_brackets = set(self.map_brackets.values())
        self.the_stack = []
    
    def matcher(self, input_string:str) -> bool: 
        if len(input_string) <=1: return False
        for c in input_string:
            if c in self.open_brackets: 
                self.the_stack.append(c)
            elif c in self.close_brackets: 
                if len(self.the_stack)==0:
                    return False
                else: 
                    if c == self.map_brackets[self.the_stack.pop()]:
                       continue
                    else: 
                        return False

        
        return True if self.the_stack == [] else False



## checking the test cases
test_cases = ["((((((((((a))))))))))", "{[(]}", "{{{{{{{{{{}}}}}}}}}}","[[[[[[[[[[]]]]]]]]]]","[one [two [three [four [five [six [seven [eight [nine [ten ]]]]]]]]]]"]
b_obj = BracketsMatcher()
for i in test_cases:
    print(i,b_obj.matcher(i))