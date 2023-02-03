import requests

req = requests.get('https://bamper.by/zchbu/zapchast_bamper-peredniy/marka_acura/model_cl/')

print(req.text)