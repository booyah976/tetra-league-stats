import json
import os
import requests
import csv

current_dir = os.path.dirname(os.path.realpath(__file__))


def get_stats(player):
    # average apm
    apm = round(player["points"]["secondary"], 2)
    pps = round(player["points"]["tertiary"], 2)
    vs = round(player["points"]["extra"]["vs"], 2)

    a_apm = []
    a_vs = []
    a_pps = []

    # individual games apm
    for item in player["points"]["secondaryAvgTracking"]:
        item = round(item, 2)
        a_apm.append(item)
    for item in player["points"]["tertiaryAvgTracking"]:
        item = round(item, 2)
        a_vs.append(item)
    for item in player["points"]["extraAvgTracking"]["aggregatestats___vsscore"]:
        item = round(item, 2)
        a_pps.append(item)

    return (apm, pps, vs, a_apm, a_pps, a_vs)


def compile_stats(username):
    request_rating = "N/A"
    response = requests.get(f"https://ch.tetr.io/api/users/{username}")

    try:
        usable_response = response.json()
    except ValueError:
        print("Empty response, did you type in the correct username in gui.py?")
        usable_response = {"success": False}
        request_rating = "N/A"

    if usable_response["success"]:
        # request_ts = usable_response["data"]["user"]["ts"]
        request_rating = usable_response["data"]["user"]["league"]["rating"]
        # standing = usable_response["data"]["user"]["league"]["standing"]
        # gametime = usable_response["data"]
    replay_folder_path = current_dir + "/replays"
    entries = os.listdir(replay_folder_path)
    for replay_file in entries:
        f = open("replays/" + str(replay_file))
        usable_f = json.load(f)

        timestamp = usable_f["ts"]

        try:
            gametype = usable_f["gametype"]
        except KeyError:
            gametype = "custom"

        endcontext = usable_f["endcontext"]

        if endcontext[0]["user"]["username"] == f"{username}":
            user_index = 0
            opp_index = 1
        else:
            user_index = 1
            opp_index = 0

        player1 = endcontext[user_index]
        player2 = endcontext[opp_index]

        score1 = player1["wins"]
        score2 = player2["wins"]

        opponent = player2["user"]["username"]

        apm1, pps1, vs1, a_apm1, a_pps1, a_vs1 = get_stats(player1)
        apm2, pps2, vs2, a_apm2, a_pps2, a_vs2 = get_stats(player2)

        comments = ""
        comments = input(f"add comment (Versus {opponent})> ")

        exists = os.path.isfile("data.csv")
        csv_path = current_dir + "/data.csv"
        with open(csv_path, "a", newline="") as f:
            writer = csv.writer(f)
            header = [
                "Timestamp",
                "Opponent",
                "Score1",
                "Score2",
                "Apm1",
                "Pps1",
                "Vs1",
                "Apm2",
                "Pps2",
                "Vs2",
                "rating",
                "gametype",
                "comments",
            ]
            csv_data = [
                timestamp,
                opponent,
                score1,
                score2,
                apm1,
                pps1,
                vs1,
                apm2,
                pps2,
                vs2,
                request_rating,
                gametype,
                comments,
            ]
            if not exists:
                writer.writerow(header)
            writer.writerow(csv_data)
    try:
        os.rename("replays/" + str(replay_file), "saved_replays/" + str(replay_file))
    except FileNotFoundError:
        os.remove("replays/" + str(replay_file))
    return 0
