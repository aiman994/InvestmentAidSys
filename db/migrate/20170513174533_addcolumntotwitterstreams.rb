class Addcolumntotwitterstreams < ActiveRecord::Migration[5.0]
  def change
  	add_column :twitter_streams, :updated_at, :datetime
  end
end
