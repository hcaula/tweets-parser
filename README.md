# Tweets Parser
## A parser for tweets collected via the Twitter API, using the (search_tweets)[https://github.com/twitterdev/search-tweets-python] helper.

### How to run
- Follow the inscrutions in the search tweets repository to collect the desired tweets.
  - Alternatively, (ask me)[mailto:lhtc@cin.ufpe.br] for my API keys and I can give it to you.
- Change the search parameters on the `config_file` for your personalized search. There's an example there you can use as a basis.
- Run `python3 json_parser.py` to parse the returned file to a proper JSON list.
- Run `python3 remove_columns.py` to remove the unecessary JSON attributes and create CSV files with them.
