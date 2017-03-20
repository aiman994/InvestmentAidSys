class Renamecolumn < ActiveRecord::Migration[5.0]
  def change
  	rename_column :stock_sectors, :id, :sectors_id
  end

end
