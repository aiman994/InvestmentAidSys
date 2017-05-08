Rails.application.routes.draw do
  get 'company/index'

    resource :user , :controller => 'user'
    resource :companies, :controller => 'company'
    resource :sessions

    root 'welcome#homepage'   

    get 'users/signup'
    get 'analyzer/centralAnalysis'
    get 'viewer/news'
    get 'viewer/company'
    get 'viewer/list'
    get 'welcome/about'
    get '/index' => 'companys#index'
    get 'company/index'
    post 'company/index'

    post '/users' => 'user#create'
    get '/users' => 'user#create'

    get    '/log_in',   to: 'session#create'
    post   '/log_in',   to: 'session#create'
    delete '/log_out',  to: 'session#destroy'

    
    get 'session/login'
    get 'welcome/homepage'
    
    get 'login' => 'session#login'
    post 'login' => 'session#login'

    get '/signup' => 'user#signup'
    post '/companies' => 'viewer#companies'

    get "/views/session/login.html", to: "session#login", as: "logins"

    post "/views/user/signup.html", to: "user#signup"
    get "/views/user/signup.html", to: "user#signup"

    get "/views/analyzer/centralAnalysis/:id", to: "analyzer#centralAnalysis", as: "analysis" , :constraints => { :id => /[^\/]+/ }
    get "/views/welcome/homepage", to: "welcome#homepage", as: "homepage"
    get "/views/welcome/about.html", to: "welcome#about", as: "about"
    get "/views/analyzer/data/", to: "analyzer#historic_data", as: "historic" , :constraints => { :tick => /[^\/]+/ }
    
    get "/views/company/index.html", to: "company#index"
    get "/views/company/searchView.html", to: "company#create", :defaults => { :format => 'html' }
    get "/views/company/show.html", to: "company#show"
    get "/views/viewer/news.html", to: "viewer#news", as: "news"
    get "/views/analyzer/centralAnalysis.html", to: "analyzer#centralAnalysis", as: "centralAnalysis"
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
