class Index():
    def __init__(self,casualty_no,spread,specific_res):
        self.casualty_no = int(casualty_no)
        self.spread = int(spread)
        self.specific_res = specific_res
        
        
    def indexer(self):
        if self.casualty_no >500 and self.spread > 5 :
            index = 10 
            return index 
        if self.casualty_no >200 and self.spread > 3:
            index = 8 
            return index 
        if self.casualty_no >100 and self.spread > 2 :
            index = 7 
            return index 
        if self.casualty_no >50 and self.spread > 1 :
            index = 6                    
            return index                     
        if self.casualty_no >25 and self.spread > 0.5 :
            index = 4
            return index 
        if self.casualty_no >20 and self.spread < 0.5 :
            index = 3
            return index 
        if self.casualty_no <10 and self.spread < 0.5 :
            index = 1
            return index 
        
                              