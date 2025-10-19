print("Hokkei natizhelerin taldau zhüiesi")

teams = []
league_info = ("Qazaqstan Hokkei Ligasy", 2025)
results = {}

while True:
    print("Mazіr")
    print("1. Komanda qosu")
    print("2. Komandalar tizimin koru")
    print("3. Komanda natizhesin engizu")
    print("4. Komanda natizhesin koru")
    print("5. Shyǵu")

    choice = input("Tandaw engiziniz (1-5): ").strip()
    if choice == "1":
        team = input("Komanda atawyn engiziniz: ").strip().title()
        teams.append(team)
        teams = list(set(teams))
        print("Komanda qosyldy!")
    elif choice == "2":
        if teams:
            print("Komandalar tizimi:")
            for t in teams:
                print("-", t)
        else:
            print("Azirge komanda joq.")
    elif choice == "3":
        team_name = input("Natizhe engizu üshin komanda atyn engiziniz: ").strip().title()
        games = int(input("Oiyndar sany: "))

        while True:
            wins = int(input("Zhenister sany: "))
            draws = int(input("Ten oiyndar sany: "))
            losses = int(input("Zhenilister sany: "))

            total = wins + draws + losses
            if total > games:
                print("Qate! Jalpy zhenis, ten, zhenilis sany oiyndar sanynan aspauy kerek.")
            else:
                break

        points = wins * 2 + draws
        win_percent = (wins / games) * 100

        results[team_name] = {
            "games": games,
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "points": points,
            "win_percent": win_percent
        }

        print(f"{team_name} komandasynyń natizhesi saqtaldy!")
    elif choice == "4":
        if not results:
            print("Azirge natizhe joq.")
        else:
            team_name = input("Komanda atyn engiziniz: ").strip().title()
            if team_name in results:
                info = results[team_name]
                print("Komandanyń jalpy natizhesi:")
                print("Sport türі: hokkei")
                print("Komanda:", team_name)
                print("Oiyndar sany:", info["games"])
                print("Zhenis:", info["wins"])
                print("Ten oiyndar:", info["draws"])
                print("Zhenilis:", info["losses"])
                print("Upai:", info["points"])
                print(f"Zhenis paiyzy: {info['win_percent']:.1f}%")

                if info["win_percent"] >= 75:
                    print("Komanda lighada jetekshi oryndarda! Tamasha natizhe.")
                elif info["win_percent"] >= 50:
                    print("Komanda oratalyq dengeide, bіraq jetіlu múmkin.")
                else:
                    print("Komanda natizhesі jaman, oiyndardy taldau qajet.")
            else:
                print("Bul komanda tізimde tabylmady.")
    elif choice == "5":
        print("Bagdarlama ayaqtaldy.")
        break

    else:
        print("Qate! Tańdawdy durys engiziniz.")
