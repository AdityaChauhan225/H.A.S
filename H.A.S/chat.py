import os
import openai
openai.organization = "org-e3OOgN5jmLJj5ofvmhnee2do"
openai.api_key = os.getenv("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")
openai.Model.list()