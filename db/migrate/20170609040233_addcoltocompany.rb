class Addcoltocompany < ActiveRecord::Migration[5.0]
  def change
  	add_column :company, :company_sector, :string
  	add_column :company, :IPOyear, :string
  	add_column :company, :marketCap, :string

  	rename_column :company, :enchange_sym, :exchange
  end
end
