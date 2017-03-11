class Stock < ApplicationRecord
    
    def getStockInfo
        path = File.expand_path('../../../../GetOrders', __FILE__)
        output = 'python2 /assets/technicalAnalysis.py'
        print output
        ## str = JSON.parse(output)
       ## print str
    end
end
