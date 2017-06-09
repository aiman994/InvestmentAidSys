class CreateBloombergStreams < ActiveRecord::Migration[5.0]
  def change
    create_table :bloomberg_streams do |t|
      t.string :companyNme
      t.string :newsDate
      t.string :headlines
      t.string :story
      t.string :newsUrl
      t.string :polarity
      t.string :subjectivity
      t.timestamps
    end
  end
end
