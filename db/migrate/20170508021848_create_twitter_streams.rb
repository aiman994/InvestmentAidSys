class CreateTwitterStreams < ActiveRecord::Migration[5.0]
  def change
    create_table :twitter_streams do |t|
    t.string :stock_name
    t.string :username
    t.string :tweets
    t.string :profile_pic_url

    t.timestamps
    end
  end
end
