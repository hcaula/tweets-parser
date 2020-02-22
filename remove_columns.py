import os
import json
import csv

whitelist = [
  "created_at",
  "id_str",
  "text",
  "truncated",
  "quote_count",
  "reply_count",
  "retweet_count",
  "favorite_count",
  "user_description"
]

for filename in os.listdir('./parsed'):
  output = "csv/{}.csv".format(os.path.splitext(filename)[0])

  with open(output, 'w') as f:
    w = csv.DictWriter(f, whitelist)
    w.writeheader()

    in_dir = "./parsed/{}".format(filename)
    with open(in_dir, 'r') as r:
      data = json.load(r)

      for row in data:
        if 'extended_tweet' in row:
          row['text'] = row['extended_tweet']['full_text']

        row['user_description'] = row['user']['description']

        row = { key: row[key] for key in whitelist }
        w.writerow(row)




