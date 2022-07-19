import subprocess

resp, err = subprocess.Popen(["curl",  "-X", "GET", "https://uscg-web-wordy-w7vmh474ha-uc.a.run.app/api/game"], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()

game_id = resp.decode().split(":")[1][:-2]

resp, err = subprocess.Popen(["curl",  "-X", "POST", "https://uscg-web-wordy-w7vmh474ha-uc.a.run.app/api/guess", "--header", "Content-Type: application/json", "-d", "{\"guess\":\"gaudy\",\"game_id\":"+ game_id + "}"], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()

correct_word = resp.decode().split(":")[1].split(",")[0]

resp, err = subprocess.Popen(["curl",  "-X", "POST", "https://uscg-web-wordy-w7vmh474ha-uc.a.run.app/api/guess", "--header", "Content-Type: application/json", "-d", "{\"guess\":" + correct_word + ",\"game_id\":"+ game_id + "}"], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()

print(resp.decode())
