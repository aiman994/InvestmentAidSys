class Changetwitterstreamcolumntype < ActiveRecord::Migration[5.0]
  def change
  	change_column :twitter_streams, :created_at, :string
  end
end
