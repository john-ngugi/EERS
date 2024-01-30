class Index():
    def __init__(self,casualty_no,spread,specific_res):
        casualty_no = self.casualty_no
        spread = self.spread
        specific_res =self.specific_res
        
        
    def indexer(self):
        if self.casualty_no >500 and self.spread > 5 :
            index = 10 
        if self.casualty_no >200 and self.spread > 3:
            index = 8 
        if self.casualty_no >100 and self.spread > 2 :
            index = 7 
        if self.casualty_no >50 and self.spread > 1 :
            index = 6                                        
        if self.casualty_no >25 and self.spread > 0.5 :
            index = 4
        if self.casualty_no >20 and self.spread < 0.5 :
            index = 3
        if self.casualty_no <10 and self.spread < 0.5 :
            index = 1

        return index 
    
                              