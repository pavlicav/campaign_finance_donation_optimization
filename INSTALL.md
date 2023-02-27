# Campaign Finance 

The purpose of the application is to allow users of the website to be able to select political issues that are important to them and match with candidates that could benefit the most from their donation.   

## Installation 

  

Clone the project: 

  

    git clone https://github.com/pavlicag/campaign_finance_donation_optimization 

  

get all the submodules 

  

    cd myapp 

    git submodule update --init --recursive 

     

This will initialise and clone the esprit and magnificent octopus libraries, and their submodules in turn. 

  

Create your virtualenv and activate it 

  

    virtualenv /path/to/venv 

    source /path/tovenv/bin/activate 

  

Install the dependencies and this app in the correct order: 

  

    pip install -r requirements.txt 

     

Create your local config 

  

    cd myapp 

    touch local.cfg 

  

Then you can override any config values that you need to 

  

To start the application, you'll also need to install it into the virtualenv just this first time 

  

    cd myapp 

    pip install -e . 

  

Then, start your app with 

  

    python service/streamlitapp.py 

  

If you want to specify your own root config file, you can use 

  

    APP_CONFIG=path/to/rootcfg.py python service/ streamlitapp.py
