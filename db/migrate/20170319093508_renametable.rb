class Renametable < ActiveRecord::Migration[5.0]
  def change
  	 rename_table :company_tables, :companies
  end
end
