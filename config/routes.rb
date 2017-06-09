Rails.application.routes.draw do

    resource :user , :controller => 'user'
    resource :company, :controller => 'company'
    resource :sessions

    root 'welcome#homepage'   

    get 'users/signup'
    get 'analyzer/centralAnalysis'
    get 'viewer/news'
    get 'viewer/company'
    get 'viewer/list'
    get 'welcome/about'

    get '/index' => 'company#index'
    get 'company/index'
    post 'company/index'

    post '/users' => 'user#create'
    get '/users' => 'user#create'

    get    '/login',   to: 'session#login'
    post   '/login',   to: 'session#create'
    get '/logout',  to: 'session#destroy'

    
    #get 'session/login'
    get 'welcome/homepage'
    
    #get 'login' => 'session#login'
    #post 'login' => 'session#login'

    get '/signup' => 'user#signup'
    
    post '/companies' => 'company#show'
    get '/companies' => 'company#show'
    #get "/views/session/login.html", to: "session#login", as: "logins"

    post "/signup", to: "user#signup"
    get "/signup", to: "user#signup"

    get "/refreshtweets", to: "analyzer#refresh_tweets", as: "refresh"
    get "/centralAnalysis/:id", to: "analyzer#centralAnalysis", as: "analysis" , :constraints => { :id => /[^\/]+/ }
    get "/homepage", to: "welcome#homepage", as: "homepage"
    get "/about", to: "welcome#about", as: "about"

    get "/views/analyzer/data/", to: "analyzer#historic_data", as: "historic" , :constraints => { :tick => /[^\/]+/ }
    post "/views/analyzer/data/", to: "analyzer#historic_data", :constraints => { :tick => /[^\/]+/ }
    
    get "/index", to: "company#index"
    get "/views/company/searchView.html", to: "company#create", :defaults => { :format => 'html' }
    get "/views/company/show.html", to: "company#show"

    get "/news", to: "viewer#news", as: "news"
    #get "/views/analyzer/centralAnalysis.html", to: "analyzer#centralAnalysis", as: "centralAnalysis"
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
