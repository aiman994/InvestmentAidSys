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

ActiveRecord::Schema.define(version: 20170406090056) do

  create_table "companies", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci" do |t|
    t.string   "company_name"
    t.string   "stock_tickers"
    t.string   "company_sector"
    t.string   "company_industry"
    t.datetime "updated_at",       null: false
  end

  create_table "prediction_data", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci" do |t|
    t.string   "stock_tickers"
    t.float    "price_close",     limit: 24
    t.float    "percentChange",   limit: 24
    t.float    "predicted_price", limit: 24
    t.datetime "created_at",                 null: false
    t.datetime "updated_at",                 null: false
  end

  create_table "stock_historic_data", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=latin1" do |t|
    t.string   "stock_tickers"
    t.string   "price_date"
    t.float    "price_close",   limit: 24
    t.float    "price_high",    limit: 24
    t.float    "price_low",     limit: 24
    t.float    "price_open",    limit: 24
    t.float    "volume",        limit: 24
    t.datetime "updated_at"
  end

  create_table "stock_industry", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=latin1" do |t|
    t.string   "industry_name"
    t.string   "industry_sector"
    t.string   "dayprice_change",      limit: 49
    t.string   "market_cap",           limit: 50
    t.string   "p_earning",            limit: 49
    t.string   "returnEquity",         limit: 49
    t.string   "div_yield",            limit: 49
    t.string   "longTermDebttoEquity", limit: 49
    t.string   "priceTobook",          limit: 49
    t.string   "netProfitMargin",      limit: 49
    t.string   "priceToFreecashFlow",  limit: 49
    t.datetime "updated_at",                      null: false
  end

  create_table "stock_sectors", primary_key: "sectors_id", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=latin1" do |t|
    t.string "sectors_name"
    t.bigint "dayprice_change"
    t.string "market_cap",           limit: 100
    t.bigint "p_earning"
    t.bigint "returnEquity"
    t.bigint "div_yield"
    t.bigint "longTermDebttoEquity"
    t.bigint "priceTobook"
    t.bigint "netProfitMargin"
    t.bigint "priceToFreecashFlow"
  end

  create_table "stocks", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=latin1" do |t|
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "users", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=latin1" do |t|
    t.integer  "userId"
    t.string   "userFname"
    t.string   "password_digest"
    t.string   "user_Cntct"
    t.string   "user_email"
    t.datetime "updated_at",      null: false
  end

end
