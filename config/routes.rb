Rails.application.routes.draw do
    resources :users
    
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
    
    get "/views/session/login.html", to: "session#login", as: "logins"
    
    get "/views/analyzer/centralAnalysis.html", to: "analyzer#centralAnalysis", as: "analysis"
    
    get "/views/welcome/homepage.html", to: "welcome#homepage", as: "homepage"
    
    get "/views/welcome/about.html", to: "welcome#about", as: "about"
    
    get "/views/analyzer/data", to: "analyzer#for_graph", as: "for_graph"
    
    get "/views/viewer/company.html", to: "viewer#company", as: "companies"
    get "/views/viewer/news.html", to: "viewer#news", as: "news"
    
    get "/views/analyzer/centralAnalysis.html", to: "analyzer#centralAnalysis", as: "centralAnalysis"
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
