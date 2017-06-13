class CreateCompanySummaries < ActiveRecord::Migration[5.0]
  def change
    create_table :company_summaries do |t|
      t.string :stock_tickers
      t.string :prevClose
      t.string :open
      t.string :bid
      t.string :ask
      t.string :dayRange
      t.string :fiftytwoWRange
      t.string :volume
      t.string :avgvol
      t.string :marketCap
      t.string :Beta
      t.string :PEratioTTM
      t.string :EPSttm
      t.string :earningDate
      t.string :DividentYield
      t.string :ExdivDate
      t.string :yearTargetEst
      t.timestamps
    end
  end
end
