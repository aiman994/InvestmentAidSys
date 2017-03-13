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

ActiveRecord::Schema.define(version: 20170312095144) do

  create_table "stock_historic_data", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=latin1" do |t|
    t.string "stock_tickers"
    t.string "price_date"
    t.float  "price_close",   limit: 24
    t.float  "price_high",    limit: 24
    t.float  "price_low",     limit: 24
    t.float  "price_open",    limit: 24
    t.float  "volume",        limit: 24
  end

  create_table "stock_sectors", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=latin1" do |t|
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
    t.datetime "created_at",      null: false
    t.datetime "updated_at",      null: false
  end

end
