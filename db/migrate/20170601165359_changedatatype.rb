class Changedatatype < ActiveRecord::Migration[5.0]
  def change
  	change_column :stock_historic_data, :price_close, :string
  	change_column :stock_historic_data, :price_high, :string
  	change_column :stock_historic_data, :price_low, :string
  	change_column :stock_historic_data, :price_open, :string
  	change_column :stock_historic_data, :volume, :string
  end
end
