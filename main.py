class LeveredIndexing(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2019, 1, 1)  # Set Start Date
        self.SetEndDate(2021, 1, 1) #Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        
        spy = self.AddEquity("SPY", Resolution.Daily) #adds Tick Data for SPY
        
        spy.SetDataNormalizationMode(DataNormalizationMode.Raw) #sets to raw data
        
        self.spy = spy.Symbol #assigns symbol object
        
        self.SetBenchmark("SPY") #Sets SP500 Benchmark
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)
        
        self.entryPrice = 0 
        self.period = timedelta(31)
        self.nextEntryTime = self.Time

    def OnData(self, data):
        if not self.spy in data: #checks if data is available 
            return
        
        price = data[self.spy].Close #close price of day before 
        
        if not self.Portfolio.Invested: #checks if already invested 
            if self.nextEntryTime <= self.Time:
                self.SetHoldings(self.spy, 1) #sets holding to 100% of portfolio
                self.Log("Buy Spy @" + str(price)) #logs buy order
                self.entryPrice = price
                
        elif self.entryPrice * 0.9 > price: 
            self.SetHoldings(self.spy, 1.5) #sets holdings to 150% of portfolio
            self.Log("Buy SPY @" + str(price))
            
            
            
