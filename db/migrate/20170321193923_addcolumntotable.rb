class Addcolumntotable < ActiveRecord::Migration[5.0]
  def change
  	add_column :stock_historic_data, :updated_at, :datetime
  end
end
