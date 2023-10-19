# Year	Animal		Year	Animal
# 2000	Dragon		2006	Dog
# 2001	Snake		2007	Pig
# 2002	Horse		2008	Rat
# 2003	Sheep		2009	Ox
# 2004	Monkey		2010	Tiger
# 2005	Rooster		2011	Hare



year = int(input())

if (year - 2000) % 12 == 0:
    print("Dragon")
elif (year - 2001) % 12 == 0:
    print("Snake")
elif (year - 2002) % 12 == 0:
    print("Horse")
elif (year - 2003) % 12 == 0:
    print("Sheep")
elif (year - 2004) % 12 == 0:
    print("Monkey")
elif (year - 2005) % 12 == 0:
    print("Rooster")
elif (year - 2006) % 12 == 0:
    print("Dog")
elif (year - 2007) % 12 == 0:
    print("Pig")
elif (year - 2008) % 12 == 0:
    print("Rat")
elif (year - 2009) % 12 == 0:
    print("Ox")
elif (year - 2010) % 12 == 0:
    print("Tiger")
elif (year - 2011) % 12 == 0:
    print("Hare")
