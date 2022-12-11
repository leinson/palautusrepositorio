from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url) #Erottelee pelaajat player olioiksi, sijoittaa listaan & palauttaa listan.
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )
    for player in stats.matches(matcher):
        print(player)

    print("ALL")
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    print("NOT")
    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
        )
    for player in stats.matches(matcher):
        print(player)

    print("HAS FEWER THAN")
    matcher = And(
        HasFewerThan(1, "goals"), 
        PlaysIn("NYR")
        )
    for player in stats.matches(matcher):
        print(player)
   
    print("OR - HAS AT LEAST")
    matcher = Or(
        HasAtLeast(45, "goals"), 
        HasAtLeast(70, "assists")
        )
    for player in stats.matches(matcher):
        print(player)
    
    print("AND + OR")
    matcher = And(
    HasAtLeast(70, "points"),
    Or(
        PlaysIn("NYR"),
        PlaysIn("FLA"),
        PlaysIn("BOS")
        )
    )
    for player in stats.matches(matcher):
        print(player)
        
if __name__ == "__main__":
    main()