class Changecolumnname < ActiveRecord::Migration[5.0]
  def change
  	rename_column :company, :company_sector, :enchange_sym
  end
end
