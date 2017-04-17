Rails.application.routes.draw do
    resources :users
    resources :companies
    
  get 'user/signup'

  get 'analyzer/centralAnalysis'

  get 'viewer/news'

  get 'viewer/company'

  get 'welcome/about'
    post '/users' => 'users#create'
    root 'welcome#homepage'    
    get 'session/login'
    get 'welcome/homepage'
    
    get 'login' => 'session#login'
    post 'login' => 'session#login'
    #get '/signup' => 'users#new'
    post '/companies' => 'viewer#ccompanies'

    get "/views/session/login.html", to: "session#login", as: "logins"
    
    get "/views/analyzer/centralAnalysis/:id", to: "analyzer#centralAnalysis", as: "analysis" , :constraints => { :id => /[^\/]+/ }
    
    get "/views/welcome/homepage", to: "welcome#homepage", as: "homepage"
    
    get "/views/welcome/about.html", to: "welcome#about", as: "about"
    
    #get "/views/analyzer/data/:tock", to: "analyzer#historic_data", as: "historic_data", :constraints => { :tock => /[^\/]+/ }

    get "/views/analyzer/data/", to: "analyzer#historic_data", as: "historic" , :constraints => { :tick => /[^\/]+/ }
    
    get "/views/viewer/company.html", to: "viewer#list"

    get "/views/viewer/news.html", to: "viewer#news", as: "news"
    
    get "/views/analyzer/centralAnalysis.html", to: "analyzer#centralAnalysis", as: "centralAnalysis"
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
