# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20170612155158) do

  create_table "bloomberg_streams", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "companyNme"
    t.string   "newsDate"
    t.string   "headlines"
    t.string   "story"
    t.string   "newsUrl"
    t.string   "polarity"
    t.string   "subjectivity"
    t.datetime "created_at",   null: false
    t.datetime "updated_at",   null: false
  end

  create_table "company", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "company_name"
    t.string   "stock_tickers"
    t.string   "exchange"
    t.string   "company_industry"
    t.datetime "created_at",       null: false
    t.datetime "updated_at",       null: false
    t.string   "company_sector"
    t.string   "IPOyear"
    t.string   "marketCap"
  end

  create_table "company_summaries", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "stock_tickers"
    t.string   "prevClose"
    t.string   "open"
    t.string   "bid"
    t.string   "ask"
    t.string   "dayRange"
    t.string   "fiftytwoWRange"
    t.string   "volume"
    t.string   "avgvol"
    t.string   "marketCap"
    t.string   "Beta"
    t.string   "PEratioTTM"
    t.string   "EPSttm"
    t.string   "earningDate"
    t.string   "DividentYield"
    t.string   "ExdivDate"
    t.string   "yearTargetEst"
    t.datetime "created_at",     null: false
    t.datetime "updated_at",     null: false
  end

  create_table "fb_streams", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "stock_name"
    t.string   "fb_user"
    t.string   "post"
    t.string   "pic_url"
    t.string   "posts_url"
    t.string   "time_posted"
    t.datetime "created_at",   null: false
    t.datetime "updated_at",   null: false
    t.string   "polarity"
    t.string   "subjectivity"
  end

  create_table "predicted_data", id: false, force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=latin1" do |t|
    t.string "stock_tickers",   limit: 20, null: false
    t.float  "price_close",     limit: 24, null: false
    t.float  "percentChange",   limit: 24, null: false
    t.float  "predicted_price", limit: 24, null: false
    t.string "updated_at",      limit: 30, null: false
  end

  create_table "prediction_data", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "stock_tickers"
    t.float    "price_close",     limit: 24
    t.float    "percentChange",   limit: 24
    t.float    "predicted_price", limit: 24
    t.datetime "created_at",                 null: false
    t.string   "updated_at",                 null: false
  end

  create_table "stock_historic_data", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "stock_tickers"
    t.string   "price_date"
    t.string   "price_close"
    t.string   "price_high"
    t.string   "price_low"
    t.string   "price_open"
    t.string   "volume"
    t.datetime "created_at",    null: false
    t.datetime "updated_at",    null: false
  end

  create_table "stock_industry", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "industry_name"
    t.string   "industry_sector"
    t.float    "dayprice_change",      limit: 24
    t.float    "market_cap",           limit: 24
    t.float    "p_earning",            limit: 24
    t.float    "returnEquity",         limit: 24
    t.float    "div_yield",            limit: 24
    t.float    "longTermDebttoEquity", limit: 24
    t.float    "priceTobook",          limit: 24
    t.float    "netProfitMargin",      limit: 24
    t.float    "priceToFreecashFlow",  limit: 24
    t.datetime "created_at",                      null: false
    t.datetime "updated_at",                      null: false
  end

  create_table "stock_sectors", primary_key: "sectors_id", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "sectors_name"
    t.float    "dayprice_change",      limit: 24
    t.float    "market_cap",           limit: 24
    t.float    "p_earning",            limit: 24
    t.float    "returnEquity",         limit: 24
    t.float    "div_yield",            limit: 24
    t.float    "longTermDebttoEquity", limit: 24
    t.float    "priceTobook",          limit: 24
    t.float    "netProfitMargin",      limit: 24
    t.float    "priceToFreecashFlow",  limit: 24
    t.datetime "created_at",                      null: false
    t.datetime "updated_at",                      null: false
  end

  create_table "stocks", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "twitter_streams", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "stock_name"
    t.string   "username"
    t.string   "tweets"
    t.string   "profile_pic_url"
    t.string   "created_at",      null: false
    t.datetime "updated_at"
  end

  create_table "users", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.integer "userId"
    t.string  "userFname"
    t.string  "password_digest"
    t.string  "user_Cntct"
    t.string  "user_email"
  end

end
