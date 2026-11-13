from drafter import *
from dataclasses import dataclass
import random
from bakery import assert_equal

set_website_title("Romance Generator")
set_site_information(
    author="Keira Fidgeon",
    description="Generates a book based off selected characteristics",
    sources="Drafter Docs",
    planning=["CS1 Final Project 1_ Design.pdf",'CS1 Final Project 0_ Pick a Problem.pdf'],
    links=[]
)
hide_debug_information()
set_website_framed(False)


@dataclass
class Book:
    title:str
    author:str
    genres:list[str]
    tropes:list[str]
    
    
@dataclass
class State:
    books: list[Book]
    selected_genres: list[str]
    selected_tropes: list[str]
    recommended_book: Book | None


add_website_css("body", """
    background-color: #fff0f5;
    color: #71334d;
    font-family: Georgia, serif;
""")

add_website_css("h1, h2, h3", """
    color: #d63384;
    text-align: center;
""")

add_website_css("button", """
    background-color: #f4a6c1;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 12px 22px;
    font-size: 16px;
    cursor: pointer;
""")

add_website_css("button:hover", """
    background-color: #e75480;
""")

add_website_css("input[type='checkbox']", """
    accent-color: #e75480;
""")

add_website_css("button", """
    background-color: #f4a6c1 !important;
    color: white !important;
    border: none;
    border-radius: 20px;
    padding: 12px 22px;
    font-size: 16px;
""")

add_website_css("button:hover", """
    background-color: #e75480 !important;
""")

add_website_css("button", """
    display: block;
    margin-left: auto !important;
    margin-right: auto !important;
    background-color: #f4a6c1 !important;
    color: white !important;
    border: none;
    border-radius: 20px;
    padding: 12px 22px;
""")

add_website_css("div:has(> button)", """
    text-align: center;
""")

books = [
    Book("The Love Hypothesis", "Ali Hazelwood", ["Contemporary Romance"], ["Fake Dating", "Grumpy x Sunshine", "Forced Proximity"]),
    Book("Love on the Brain", "Ali Hazelwood", ["Contemporary Romance"], ["Enemies to Lovers", "Workplace Romance", "Forced Proximity"]),
    Book("The Bride Test", "Helen Hoang", ["Contemporary Romance"], ["Arranged Marriage", "Opposites Attract"]),
    Book("The Kiss Quotient", "Helen Hoang", ["Contemporary Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Heart Principle", "Helen Hoang", ["Contemporary Romance"], ["Forced Proximity", "Opposites Attract"]),
    Book("The Hating Game", "Sally Thorne", ["Contemporary Romance", "Romantic Comedy"], ["Enemies to Lovers", "Workplace Romance", "Forced Proximity"]),
    Book("Beach Read", "Emily Henry", ["Contemporary Romance"], ["Rivals to Lovers", "Forced Proximity", "Slow Burn"]),
    Book("People We Meet on Vacation", "Emily Henry", ["Contemporary Romance"], ["Friends to Lovers", "Opposites Attract", "Slow Burn"]),
    Book("Book Lovers", "Emily Henry", ["Contemporary Romance"], ["Enemies to Lovers", "Workplace Romance", "Opposites Attract"]),
    Book("Happy Place", "Emily Henry", ["Contemporary Romance"], ["Second Chance Romance", "Forced Proximity", "Friends to Lovers"]),
    Book("Funny Story", "Emily Henry", ["Contemporary Romance", "Romantic Comedy"], ["Opposites Attract", "Forced Proximity", "Friends to Lovers"]),
    Book("The Spanish Love Deception", "Elena Armas", ["Contemporary Romance"], ["Fake Dating", "Enemies to Lovers", "Forced Proximity"]),
    Book("The American Roommate Experiment", "Elena Armas", ["Contemporary Romance", "Romantic Comedy"], ["Friends to Lovers", "Forced Proximity", "Slow Burn"]),
    Book("The Unhoneymooners", "Christina Lauren", ["Contemporary Romance", "Romantic Comedy"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("Josh and Hazel's Guide to Not Dating", "Christina Lauren", ["Contemporary Romance", "Romantic Comedy"], ["Friends to Lovers", "Opposites Attract"]),
    Book("The Soulmate Equation", "Christina Lauren", ["Contemporary Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Paradise Problem", "Christina Lauren", ["Contemporary Romance"], ["Fake Dating", "Marriage of Convenience", "Forced Proximity"]),
    Book("The True Love Experiment", "Christina Lauren", ["Contemporary Romance"], ["Friends to Lovers", "Opposites Attract"]),
    Book("The Wedding Date", "Jasmine Guillory", ["Contemporary Romance", "Romantic Comedy"], ["Fake Dating", "Opposites Attract"]),
    Book("The Proposal", "Jasmine Guillory", ["Contemporary Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Wedding Party", "Jasmine Guillory", ["Contemporary Romance"], ["Enemies to Lovers", "Friends with Benefits"]),
    Book("The Flatshare", "Beth O'Leary", ["Contemporary Romance", "Romantic Comedy"], ["Forced Proximity", "Friends to Lovers", "Slow Burn"]),
    Book("The Switch", "Beth O'Leary", ["Contemporary Romance"], ["Opposites Attract", "Small-Town Romance"]),
    Book("The Road Trip", "Beth O'Leary", ["Contemporary Romance"], ["Second Chance Romance", "Forced Proximity"]),
    Book("The No-Show", "Beth O'Leary", ["Contemporary Romance"], ["Love Triangle", "Slow Burn"]),
    Book("The Bodyguard", "Katherine Center", ["Contemporary Romance", "Romantic Comedy"], ["Bodyguard Romance", "Forced Proximity", "Opposites Attract"]),
    Book("The Lost Husband", "Katherine Center", ["Contemporary Romance"], ["Small-Town Romance", "Slow Burn"]),
    Book("The Rom-Commers", "Katherine Center", ["Contemporary Romance", "Romantic Comedy"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("The Friend Zone", "Abby Jimenez", ["Contemporary Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("The Happy Ever After Playlist", "Abby Jimenez", ["Contemporary Romance"], ["Unexpected Romance", "Slow Burn"]),
    Book("Life's Too Short", "Abby Jimenez", ["Contemporary Romance"], ["Opposites Attract", "Forced Proximity"]),
    Book("Part of Your World", "Abby Jimenez", ["Contemporary Romance"], ["Opposites Attract", "Small-Town Romance"]),
    Book("Yours Truly", "Abby Jimenez", ["Contemporary Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("Just for the Summer", "Abby Jimenez", ["Contemporary Romance"], ["Fake Dating", "Forced Proximity"]),
    Book("The Cheat Sheet", "Sarah Adams", ["Contemporary Romance", "Romantic Comedy"], ["Friends to Lovers", "He Falls First"]),
    Book("When in Rome", "Sarah Adams", ["Contemporary Romance", "Romantic Comedy"], ["Opposites Attract", "Small-Town Romance"]),
    Book("The Bodyguard", "Katherine Center", ["Contemporary Romance"], ["Bodyguard Romance", "Forced Proximity"]),
    Book("The Love Wager", "Lynn Painter", ["Contemporary Romance", "Romantic Comedy"], ["Friends to Lovers", "Fake Dating"]),
    Book("Better Than the Movies", "Lynn Painter", ["Young Adult Romance", "Romantic Comedy"], ["Friends to Lovers", "Opposites Attract"]),
    Book("Nothing Like the Movies", "Lynn Painter", ["Young Adult Romance"], ["Second Chance Romance", "Friends to Lovers"]),
    Book("The Do-Over", "Lynn Painter", ["Young Adult Romance", "Romantic Comedy"], ["Opposites Attract", "Slow Burn"]),
    Book("The Statistical Probability of Love at First Sight", "Jennifer E. Smith", ["Young Adult Romance"], ["Love at First Sight", "Forced Proximity"]),
    Book("This Is What Happy Looks Like", "Jennifer E. Smith", ["Young Adult Romance"], ["Celebrity Romance", "Secret Identity"]),
    Book("The Geography of You and Me", "Jennifer E. Smith", ["Young Adult Romance"], ["Long-Distance Romance", "Love at First Sight"]),
    Book("Anna and the French Kiss", "Stephanie Perkins", ["Young Adult Romance"], ["Friends to Lovers", "Love Triangle"]),
    Book("Lola and the Boy Next Door", "Stephanie Perkins", ["Young Adult Romance"], ["Friends to Lovers", "Second Chance Romance"]),
    Book("Isla and the Happily Ever After", "Stephanie Perkins", ["Young Adult Romance"], ["Friends to Lovers", "Love at First Sight"]),
    Book("To All the Boys I've Loved Before", "Jenny Han", ["Young Adult Romance"], ["Fake Dating", "Friends to Lovers"]),
    Book("P.S. I Still Love You", "Jenny Han", ["Young Adult Romance"], ["Love Triangle", "Friends to Lovers"]),
    Book("Always and Forever, Lara Jean", "Jenny Han", ["Young Adult Romance"], ["Friends to Lovers", "Second Chance Romance"]),
    Book("The Summer I Turned Pretty", "Jenny Han", ["Young Adult Romance"], ["Love Triangle", "Friends to Lovers"]),
    Book("It's Not Summer Without You", "Jenny Han", ["Young Adult Romance"], ["Second Chance Romance", "Love Triangle"]),
    Book("We'll Always Have Summer", "Jenny Han", ["Young Adult Romance"], ["Love Triangle", "Second Chance Romance"]),
    Book("Since You've Been Gone", "Morgan Matson", ["Young Adult Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("The Unexpected Everything", "Morgan Matson", ["Young Adult Romance"], ["Friends to Lovers", "Opposites Attract"]),
    Book("Save the Date", "Morgan Matson", ["Young Adult Romance", "Romantic Comedy"], ["Forced Proximity", "Family"]),
    Book("When Dimple Met Rishi", "Sandhya Menon", ["Young Adult Romance"], ["Arranged Marriage", "Opposites Attract"]),
    Book("There's Something About Sweetie", "Sandhya Menon", ["Young Adult Romance"], ["Friends to Lovers", "Opposites Attract"]),
    Book("Today Tonight Tomorrow", "Rachel Lynn Solomon", ["Young Adult Romance"], ["Rivals to Lovers", "Enemies to Lovers"]),
    Book("The Ex Talk", "Rachel Lynn Solomon", ["Contemporary Romance"], ["Fake Dating", "Workplace Romance", "Enemies to Lovers"]),
    Book("See You Yesterday", "Rachel Lynn Solomon", ["Young Adult Romance", "Science Fiction Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("A Cuban Girl's Guide to Tea and Tomorrow", "Laura Taylor Namey", ["Young Adult Romance"], ["Opposites Attract", "Small-Town Romance"]),
    Book("Tweet Cute", "Emma Lord", ["Young Adult Romance", "Romantic Comedy"], ["Enemies to Lovers", "Rivals to Lovers"]),
    Book("You Have a Match", "Emma Lord", ["Young Adult Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("The Start of Me and You", "Emery Lord", ["Young Adult Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("Open Road Summer", "Emery Lord", ["Young Adult Romance"], ["Friends to Lovers", "Celebrity Romance"]),
    Book("The Sun Is Also a Star", "Nicola Yoon", ["Young Adult Romance"], ["Love at First Sight", "Opposites Attract"]),
    Book("Everything, Everything", "Nicola Yoon", ["Young Adult Romance"], ["Forbidden Love", "Forced Proximity"]),
    Book("Instructions for Dancing", "Nicola Yoon", ["Young Adult Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Fault in Our Stars", "John Green", ["Young Adult Romance"], ["Unexpected Romance", "First Love"]),
    Book("Five Feet Apart", "Rachael Lippincott", ["Young Adult Romance"], ["Forbidden Love", "Forced Proximity"]),
    Book("If I Stay", "Gayle Forman", ["Young Adult Romance"], ["First Love", "Love After Loss"]),
    Book("Where She Went", "Gayle Forman", ["Young Adult Romance"], ["Second Chance Romance", "Love After Loss"]),
    Book("The Sky Is Everywhere", "Jandy Nelson", ["Young Adult Romance"], ["Love Triangle", "Love After Loss"]),
    Book("I'll Give You the Sun", "Jandy Nelson", ["Young Adult Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("Aristotle and Dante Discover the Secrets of the Universe", "Benjamin Alire Sáenz", ["Young Adult Romance", "LGBTQ+ Romance"], ["Friends to Lovers", "Slow Burn", "Coming of Age"]),
    Book("The Sunbearer Trials", "Aiden Thomas", ["Young Adult Romance", "Fantasy Romance", "LGBTQ+ Romance"], ["Slow Burn", "Opposites Attract"]),
    Book("Cemetery Boys", "Aiden Thomas", ["Young Adult Romance", "Fantasy Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Forced Proximity"]),
    Book("The Lesbiana's Guide to Catholic School", "Sonora Reyes", ["Young Adult Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("She Gets the Girl", "Rachael Lippincott and Alyson Derrick", ["Young Adult Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Friends to Lovers"]),
    Book("I Kissed Shara Wheeler", "Casey McQuiston", ["Young Adult Romance", "LGBTQ+ Romance"], ["Enemies to Lovers", "Rivals to Lovers"]),
    Book("Red, White & Royal Blue", "Casey McQuiston", ["Contemporary Romance", "LGBTQ+ Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("One Last Stop", "Casey McQuiston", ["Contemporary Romance", "LGBTQ+ Romance", "Science Fiction Romance"], ["Forced Proximity", "Slow Burn"]),
    Book("The Charm Offensive", "Alison Cochrun", ["Contemporary Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Forced Proximity"]),
    Book("Written in the Stars", "Alexandria Bellefleur", ["Contemporary Romance", "LGBTQ+ Romance"], ["Fake Dating", "Opposites Attract"]),
    Book("Count Your Lucky Stars", "Alexandria Bellefleur", ["Contemporary Romance", "LGBTQ+ Romance"], ["Second Chance Romance", "Friends to Lovers"]),
    Book("Delilah Green Doesn't Care", "Ashley Herring Blake", ["Contemporary Romance", "LGBTQ+ Romance"], ["Enemies to Lovers", "Small-Town Romance"]),
    Book("Astrid Parker Doesn't Fail", "Ashley Herring Blake", ["Contemporary Romance", "LGBTQ+ Romance"], ["Rivals to Lovers", "Forced Proximity"]),
    Book("Iris Kelly Doesn't Date", "Ashley Herring Blake", ["Contemporary Romance", "LGBTQ+ Romance"], ["Friends to Lovers", "Fake Dating"]),
    Book("Something to Talk About", "Meryl Wilsner", ["Contemporary Romance", "LGBTQ+ Romance"], ["Workplace Romance", "Slow Burn"]),
    Book("Honey Girl", "Morgan Rogers", ["Contemporary Romance", "LGBTQ+ Romance"], ["Marriage of Convenience", "Opposites Attract"]),
    Book("The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", ["Contemporary Romance"], ["Forbidden Love", "Love Triangle"]),
    Book("The Light We Lost", "Jill Santopolo", ["Contemporary Romance"], ["First Love", "Second Chance Romance"]),
    Book("Love and Other Words", "Christina Lauren", ["Contemporary Romance"], ["Friends to Lovers", "Second Chance Romance"]),
    Book("Every Summer After", "Carley Fortune", ["Contemporary Romance"], ["Friends to Lovers", "Second Chance Romance"]),
    Book("Meet Me at the Lake", "Carley Fortune", ["Contemporary Romance"], ["Second Chance Romance", "Small-Town Romance"]),
    Book("This Summer Will Be Different", "Carley Fortune", ["Contemporary Romance"], ["Forbidden Love", "Friends to Lovers"]),
    Book("The Notebook", "Nicholas Sparks", ["Contemporary Romance"], ["First Love", "Second Chance Romance"]),
    Book("A Walk to Remember", "Nicholas Sparks", ["Contemporary Romance"], ["Opposites Attract", "First Love"]),
    Book("The Lucky One", "Nicholas Sparks", ["Contemporary Romance"], ["Love at First Sight", "Small-Town Romance"]),
    Book("The Choice", "Nicholas Sparks", ["Contemporary Romance"], ["Friends to Lovers", "Second Chance Romance"]),
    Book("The Longest Ride", "Nicholas Sparks", ["Contemporary Romance"], ["Opposites Attract", "Second Chance Romance"]),
    Book("The Wedding", "Nicholas Sparks", ["Contemporary Romance"], ["Marriage in Trouble", "Second Chance Romance"]),
    Book("The Blue Castle", "L. M. Montgomery", ["Historical Romance"], ["Opposites Attract", "Small-Town Romance"]),
    Book("Anne of the Island", "L. M. Montgomery", ["Historical Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("A Room with a View", "E. M. Forster", ["Historical Romance"], ["Opposites Attract", "Forbidden Love"]),
    Book("Pride and Prejudice", "Jane Austen", ["Historical Romance"], ["Enemies to Lovers", "Grumpy x Sunshine"]),
    Book("Sense and Sensibility", "Jane Austen", ["Historical Romance"], ["Opposites Attract", "Second Chance Romance"]),
    Book("Emma", "Jane Austen", ["Historical Romance"], ["Friends to Lovers", "Opposites Attract"]),
    Book("Persuasion", "Jane Austen", ["Historical Romance"], ["Second Chance Romance", "Slow Burn"]),
    Book("Northanger Abbey", "Jane Austen", ["Historical Romance", "Gothic Romance"], ["Friends to Lovers", "Opposites Attract"]),
    Book("Jane Eyre", "Charlotte Brontë", ["Historical Romance", "Gothic Romance"], ["Grumpy x Sunshine", "Forbidden Love"]),
    Book("Wuthering Heights", "Emily Brontë", ["Historical Romance", "Gothic Romance"], ["Forbidden Love", "Second Chance Romance"]),
    Book("The Tenant of Wildfell Hall", "Anne Brontë", ["Historical Romance"], ["Forbidden Love", "Second Chance Romance"]),
    Book("The Grand Sophy", "Georgette Heyer", ["Historical Romance"], ["Enemies to Lovers", "Opposites Attract"]),
    Book("Arabella", "Georgette Heyer", ["Historical Romance"], ["Opposites Attract", "Grumpy x Sunshine"]),
    Book("Frederica", "Georgette Heyer", ["Historical Romance"], ["Friends to Lovers", "Opposites Attract"]),
    Book("The Duchess Deal", "Tessa Dare", ["Historical Romance"], ["Marriage of Convenience", "Grumpy x Sunshine"]),
    Book("A Week to Be Wicked", "Tessa Dare", ["Historical Romance"], ["Forced Proximity", "Opposites Attract"]),
    Book("The Wallflower Wager", "Tessa Dare", ["Historical Romance"], ["Friends to Lovers", "Opposites Attract"]),
    Book("The Governess Game", "Tessa Dare", ["Historical Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Duchess War", "Courtney Milan", ["Historical Romance"], ["Opposites Attract", "Forbidden Love"]),
    Book("The Suffragette Scandal", "Courtney Milan", ["Historical Romance"], ["Enemies to Lovers", "Opposites Attract"]),
    Book("Bringing Down the Duke", "Evie Dunmore", ["Historical Romance"], ["Opposites Attract", "Forbidden Love"]),
    Book("A Rogue of One's Own", "Evie Dunmore", ["Historical Romance"], ["Enemies to Lovers", "Rivals to Lovers"]),
    Book("Portrait of a Scotsman", "Evie Dunmore", ["Historical Romance"], ["Marriage of Convenience", "Opposites Attract"]),
    Book("The Viscount Who Loved Me", "Julia Quinn", ["Historical Romance"], ["Enemies to Lovers", "Grumpy x Sunshine"]),
    Book("An Offer from a Gentleman", "Julia Quinn", ["Historical Romance"], ["Opposites Attract", "Forbidden Love"]),
    Book("Romancing Mister Bridgerton", "Julia Quinn", ["Historical Romance"], ["Friends to Lovers", "He Falls First"]),
    Book("When He Was Wicked", "Julia Quinn", ["Historical Romance"], ["Forbidden Love", "Slow Burn"]),
    Book("The Duke and I", "Julia Quinn", ["Historical Romance"], ["Fake Dating", "Marriage of Convenience"]),
    Book("The Secret Diaries of Miss Miranda Cheever", "Julia Quinn", ["Historical Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("The Lady's Guide to Celestial Mechanics", "Olivia Waite", ["Historical Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Care and Feeding of Waspish Widows", "Olivia Waite", ["Historical Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Small-Town Romance"]),
    Book("The Queer Principles of Kit Webb", "Cat Sebastian", ["Historical Romance", "LGBTQ+ Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("The Perfect Crimes of Marian Hayes", "Cat Sebastian", ["Historical Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Forced Proximity"]),
    Book("The Secret Lives of Country Gentlemen", "K. J. Charles", ["Historical Romance", "LGBTQ+ Romance"], ["Forbidden Love", "Opposites Attract"]),
    Book("A Marvellous Light", "Freya Marske", ["Historical Romance", "Fantasy Romance", "LGBTQ+ Romance"], ["Forced Proximity", "Enemies to Lovers"]),
    Book("The Undertaking of Hart and Mercy", "Megan Bannen", ["Fantasy Romance"], ["Enemies to Lovers", "Pen Pals"]),
    Book("Emily Wilde's Encyclopaedia of Faeries", "Heather Fawcett", ["Fantasy Romance"], ["Grumpy x Sunshine", "Forced Proximity"]),
    Book("The Very Secret Society of Irregular Witches", "Sangu Mandanna", ["Fantasy Romance"], ["Found Family", "Opposites Attract"]),
    Book("The Ex Hex", "Erin Sterling", ["Fantasy Romance"], ["Second Chance Romance", "Small-Town Romance"]),
    Book("The Kiss Curse", "Erin Sterling", ["Fantasy Romance"], ["Enemies to Lovers", "Small-Town Romance"]),
    Book("The Night Circus", "Erin Morgenstern", ["Fantasy Romance"], ["Rivals to Lovers", "Forbidden Love"]),
    Book("Stardust", "Neil Gaiman", ["Fantasy Romance"], ["Adventure", "Opposites Attract"]),
    Book("The Princess Bride", "William Goldman", ["Fantasy Romance"], ["True Love", "Adventure"]),
    Book("The Cruel Prince", "Holly Black", ["Young Adult Romance", "Fantasy Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("The Wicked King", "Holly Black", ["Young Adult Romance", "Fantasy Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("The Queen of Nothing", "Holly Black", ["Young Adult Romance", "Fantasy Romance"], ["Enemies to Lovers", "Second Chance Romance"]),
    Book("Once Upon a Broken Heart", "Stephanie Garber", ["Young Adult Romance", "Fantasy Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("The Ballad of Never After", "Stephanie Garber", ["Young Adult Romance", "Fantasy Romance"], ["Slow Burn", "Forbidden Love"]),
    Book("A Curse for True Love", "Stephanie Garber", ["Young Adult Romance", "Fantasy Romance"], ["Second Chance Romance", "Forbidden Love"]),
    Book("The Wrath and the Dawn", "Renée Ahdieh", ["Young Adult Romance", "Fantasy Romance"], ["Enemies to Lovers", "Arranged Marriage"]),
    Book("The Rose and the Dagger", "Renée Ahdieh", ["Young Adult Romance", "Fantasy Romance"], ["Forbidden Love", "Arranged Marriage"]),
    Book("The Winner's Curse", "Marie Rutkoski", ["Young Adult Romance", "Fantasy Romance"], ["Forbidden Love", "Opposites Attract"]),
    Book("The Winner's Crime", "Marie Rutkoski", ["Young Adult Romance", "Fantasy Romance"], ["Forbidden Love", "Slow Burn"]),
    Book("The Winner's Kiss", "Marie Rutkoski", ["Young Adult Romance", "Fantasy Romance"], ["Forbidden Love", "Second Chance Romance"]),
    Book("Daughter of Smoke and Bone", "Laini Taylor", ["Young Adult Romance", "Fantasy Romance"], ["Forbidden Love", "Star-Crossed Lovers"]),
    Book("Days of Blood and Starlight", "Laini Taylor", ["Young Adult Romance", "Fantasy Romance"], ["Forbidden Love", "Second Chance Romance"]),
    Book("Dreams of Gods and Monsters", "Laini Taylor", ["Young Adult Romance", "Fantasy Romance"], ["Star-Crossed Lovers", "Forbidden Love"]),
    Book("The Selection", "Kiera Cass", ["Young Adult Romance", "Dystopian Romance"], ["Love Triangle", "Royal Romance"]),
    Book("The Elite", "Kiera Cass", ["Young Adult Romance", "Dystopian Romance"], ["Love Triangle", "Royal Romance"]),
    Book("The One", "Kiera Cass", ["Young Adult Romance", "Dystopian Romance"], ["Love Triangle", "Royal Romance"]),
    Book("The Betrothed", "Kiera Cass", ["Young Adult Romance", "Fantasy Romance"], ["Arranged Marriage", "Love Triangle"]),
    Book("The Betrayed", "Kiera Cass", ["Young Adult Romance", "Fantasy Romance"], ["Forbidden Love", "Royal Romance"]),
    Book("Matched", "Ally Condie", ["Young Adult Romance", "Dystopian Romance"], ["Love Triangle", "Forbidden Love"]),
    Book("Crossed", "Ally Condie", ["Young Adult Romance", "Dystopian Romance"], ["Love Triangle", "Forbidden Love"]),
    Book("Reached", "Ally Condie", ["Young Adult Romance", "Dystopian Romance"], ["Love Triangle", "Second Chance Romance"]),
    Book("Delirium", "Lauren Oliver", ["Young Adult Romance", "Dystopian Romance"], ["Forbidden Love", "Star-Crossed Lovers"]),
    Book("Pandemonium", "Lauren Oliver", ["Young Adult Romance", "Dystopian Romance"], ["Forbidden Love", "Love Triangle"]),
    Book("Requiem", "Lauren Oliver", ["Young Adult Romance", "Dystopian Romance"], ["Love Triangle", "Forbidden Love"]),
    Book("The Time Traveler's Wife", "Audrey Niffenegger", ["Science Fiction Romance"], ["Time Travel", "Forbidden Love"]),
    Book("Winter's Orbit", "Everina Maxwell", ["Science Fiction Romance", "LGBTQ+ Romance"], ["Marriage of Convenience", "Forced Proximity"]),
    Book("Ocean's Echo", "Everina Maxwell", ["Science Fiction Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Forced Proximity"]),
    Book("This Is How You Lose the Time War", "Amal El-Mohtar and Max Gladstone", ["Science Fiction Romance", "LGBTQ+ Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("The Darkness Outside Us", "Eliot Schrefer", ["Young Adult Romance", "Science Fiction Romance", "LGBTQ+ Romance"], ["Forced Proximity", "Enemies to Lovers"]),
    Book("Crier's War", "Nina Varela", ["Young Adult Romance", "Fantasy Romance", "LGBTQ+ Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("Iron Heart", "Nina Varela", ["Young Adult Romance", "Fantasy Romance", "LGBTQ+ Romance"], ["Forbidden Love", "Second Chance Romance"]),
    Book("The Sound of Stars", "Alechia Dow", ["Young Adult Romance", "Science Fiction Romance"], ["Forbidden Love", "Opposites Attract"]),
    Book("Across the Universe", "Beth Revis", ["Young Adult Romance", "Science Fiction Romance"], ["Forced Proximity", "Mystery"]),
    Book("Shards of Honor", "Lois McMaster Bujold", ["Science Fiction Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("Cordelia's Honor", "Lois McMaster Bujold", ["Science Fiction Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("The Golem and the Jinni", "Helene Wecker", ["Fantasy Romance", "Historical Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Undertaking of Hart and Mercy", "Megan Bannen", ["Fantasy Romance"], ["Enemies to Lovers", "Pen Pals"]),
    Book("The House in the Cerulean Sea", "TJ Klune", ["Fantasy Romance", "LGBTQ+ Romance"], ["Found Family", "Opposites Attract"]),
    Book("Under the Whispering Door", "TJ Klune", ["Fantasy Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("Boyfriend Material", "Alexis Hall", ["Contemporary Romance", "LGBTQ+ Romance", "Romantic Comedy"], ["Fake Dating", "Opposites Attract"]),
    Book("Husband Material", "Alexis Hall", ["Contemporary Romance", "LGBTQ+ Romance"], ["Second Chance Romance", "Friends to Lovers"]),
    Book("The Charm Offensive", "Alison Cochrun", ["Contemporary Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Forced Proximity"]),
    Book("The Wisteria Society of Lady Scoundrels", "India Holton", ["Historical Romance", "Fantasy Romance"], ["Enemies to Lovers", "Opposites Attract"]),
    Book("The League of Gentlewomen Witches", "India Holton", ["Historical Romance", "Fantasy Romance"], ["Enemies to Lovers", "Opposites Attract"]),
    Book("The Secret Service of Tea and Treason", "India Holton", ["Historical Romance", "Fantasy Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("The Dead Romantics", "Ashley Poston", ["Contemporary Romance", "Paranormal Romance"], ["Opposites Attract", "Love After Loss"]),
    Book("The Seven Year Slip", "Ashley Poston", ["Contemporary Romance", "Fantasy Romance"], ["Time Travel", "Forced Proximity"]),
    Book("The Love of My Afterlife", "Kirsty Greenwood", ["Contemporary Romance", "Paranormal Romance"], ["Unexpected Romance", "Opposites Attract"]),
    Book("The Beautiful Ones", "Silvia Moreno-Garcia", ["Historical Romance", "Fantasy Romance"], ["Opposites Attract", "Forbidden Love"]),
    Book("The Invisible Life of Addie LaRue", "V. E. Schwab", ["Fantasy Romance"], ["Forbidden Love", "Slow Burn"]),
    Book("A Discovery of Witches", "Deborah Harkness", ["Fantasy Romance", "Paranormal Romance"], ["Forbidden Love", "Opposites Attract"]),
    Book("The Serpent and the Wings of Night", "Carissa Broadbent", ["Fantasy Romance", "Paranormal Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("The Ashes and the Star-Cursed King", "Carissa Broadbent", ["Fantasy Romance"], ["Second Chance Romance", "Forbidden Love"]),
    Book("From Blood and Ash", "Jennifer L. Armentrout", ["Fantasy Romance"], ["Forbidden Love", "Bodyguard Romance"]),
    Book("A Kingdom of Flesh and Fire", "Jennifer L. Armentrout", ["Fantasy Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("The Bridge Kingdom", "Danielle L. Jensen", ["Fantasy Romance"], ["Enemies to Lovers", "Arranged Marriage"]),
    Book("The Traitor Queen", "Danielle L. Jensen", ["Fantasy Romance"], ["Second Chance Romance", "Forbidden Love"]),
    Book("Radiance", "Grace Draven", ["Fantasy Romance"], ["Arranged Marriage", "Friends to Lovers"]),
    Book("Eidolon", "Grace Draven", ["Fantasy Romance"], ["Marriage of Convenience", "Opposites Attract"]),
    Book("The Winter King", "C. L. Wilson", ["Fantasy Romance"], ["Arranged Marriage", "Enemies to Lovers"]),
    Book("The Bird and the Sword", "Amy Harmon", ["Fantasy Romance"], ["Forbidden Love", "Opposites Attract"]),
    Book("The Queen of All That Dies", "Laura Thalassa", ["Fantasy Romance", "Dystopian Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("The Bargainer", "Laura Thalassa", ["Fantasy Romance", "Paranormal Romance"], ["Second Chance Romance", "Fated Mates"]),
    Book("The Cruelest Mercy", "Natalie Mae", ["Young Adult Romance", "Fantasy Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("The Shadows Between Us", "Tricia Levenseller", ["Young Adult Romance", "Fantasy Romance"], ["Enemies to Lovers", "Royal Romance"]),
    Book("The Dark Wife", "Sarah Diemer", ["Fantasy Romance", "LGBTQ+ Romance"], ["Forbidden Love", "Opposites Attract"]),
    Book("The Midnight Lie", "Marie Rutkoski", ["Young Adult Romance", "Fantasy Romance", "LGBTQ+ Romance"], ["Forbidden Love", "Opposites Attract"]),
    Book("The Jasmine Throne", "Tasha Suri", ["Fantasy Romance", "LGBTQ+ Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("The Oleander Sword", "Tasha Suri", ["Fantasy Romance", "LGBTQ+ Romance"], ["Forbidden Love", "Slow Burn"]),
    Book("The Priory of the Orange Tree", "Samantha Shannon", ["Fantasy Romance", "LGBTQ+ Romance"], ["Forbidden Love", "Slow Burn"]),
    Book("A Day of Fallen Night", "Samantha Shannon", ["Fantasy Romance", "LGBTQ+ Romance"], ["Forbidden Love", "Slow Burn"]),
    Book("The Girl Who Fell Beneath the Sea", "Axie Oh", ["Young Adult Romance", "Fantasy Romance"], ["Arranged Marriage", "Opposites Attract"]),
    Book("XOXO", "Axie Oh", ["Young Adult Romance"], ["Celebrity Romance", "Opposites Attract"]),
    Book("The Sun and the Void", "R. S. A. Garcia", ["Fantasy Romance"], ["Forbidden Love", "Opposites Attract"]),
    Book("A Far Wilder Magic", "Allison Saft", ["Young Adult Romance", "Fantasy Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("Down Comes the Night", "Allison Saft", ["Young Adult Romance", "Fantasy Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("The Witch Haven", "Sasha Peyton Smith", ["Young Adult Romance", "Fantasy Romance"], ["Love Triangle", "Forbidden Love"]),
    Book("The Once and Future Witches", "Alix E. Harrow", ["Fantasy Romance"], ["Found Family", "Forbidden Love"]),
    Book("The Very Secret Society of Irregular Witches", "Sangu Mandanna", ["Fantasy Romance"], ["Found Family", "Opposites Attract"]),
    Book("The Ex Hex", "Erin Sterling", ["Fantasy Romance"], ["Second Chance Romance", "Small-Town Romance"]),
    Book("The Kiss Curse", "Erin Sterling", ["Fantasy Romance"], ["Enemies to Lovers", "Small-Town Romance"]),
    Book("The Wedding Date", "Jasmine Guillory", ["Contemporary Romance"], ["Fake Dating", "Opposites Attract"]),
    Book("The Wedding Crasher", "Mia Sosa", ["Contemporary Romance", "Romantic Comedy"], ["Fake Dating", "Opposites Attract"]),
    Book("The Worst Best Man", "Mia Sosa", ["Contemporary Romance", "Romantic Comedy"], ["Enemies to Lovers", "Workplace Romance"]),
    Book("The Roommate", "Rosie Danan", ["Contemporary Romance"], ["Forced Proximity", "Opposites Attract"]),
    Book("The Intimacy Experiment", "Rosie Danan", ["Contemporary Romance"], ["Friends to Lovers", "Opposites Attract"]),
    Book("The Bromance Book Club", "Lyssa Kay Adams", ["Contemporary Romance", "Romantic Comedy"], ["Marriage in Trouble", "Second Chance Romance"]),
    Book("Undercover Bromance", "Lyssa Kay Adams", ["Contemporary Romance", "Romantic Comedy"], ["Friends to Lovers", "Opposites Attract"]),
    Book("The Dating Plan", "Sara Desai", ["Contemporary Romance", "Romantic Comedy"], ["Fake Dating", "Friends to Lovers"]),
    Book("The Singles Table", "Sara Desai", ["Contemporary Romance", "Romantic Comedy"], ["Opposites Attract", "Forced Proximity"]),
    Book("The Wedding Ringer", "Kerry Rea", ["Contemporary Romance", "Romantic Comedy"], ["Fake Dating", "Friends to Lovers"]),
    Book("The Love Act", "Zara Bell", ["Contemporary Romance", "Romantic Comedy"], ["Fake Dating", "Celebrity Romance"]),
    Book("The Nanny", "Lana Ferguson", ["Contemporary Romance"], ["Forced Proximity", "Single Parent"]),
    Book("The No-Show", "Beth O'Leary", ["Contemporary Romance"], ["Love Triangle", "Slow Burn"]),
    Book("The Roughest Draft", "Emily Wibberley and Austin Siegemund-Broka", ["Contemporary Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("The Break-Up Tour", "Emily Wibberley and Austin Siegemund-Broka", ["Contemporary Romance"], ["Second Chance Romance", "Musician Romance"]),
    Book("The Do-Over", "Lynn Painter", ["Young Adult Romance", "Romantic Comedy"], ["Second Chance Romance", "Opposites Attract"]),
    Book("The Summer of Broken Rules", "K. L. Walther", ["Young Adult Romance"], ["Friends to Lovers", "Summer Romance"]),
    Book("The Matchbreaker Summer", "Annie Rains", ["Contemporary Romance"], ["Small-Town Romance", "Friends to Lovers"]),
    Book("The Mistletoe Motive", "Chloe Liese", ["Holiday Romance", "Contemporary Romance"], ["Enemies to Lovers", "Workplace Romance"]),
    Book("In a Holidaze", "Christina Lauren", ["Holiday Romance", "Contemporary Romance"], ["Friends to Lovers", "Time Travel"]),
    Book("The Holiday Swap", "Maggie Knox", ["Holiday Romance", "Contemporary Romance"], ["Opposites Attract", "Forced Proximity"]),
    Book("A Merry Little Meet Cute", "Julie Murphy and Sierra Simone", ["Holiday Romance", "Contemporary Romance"], ["Celebrity Romance", "Opposites Attract"]),
    Book("The Christmas Bookshop", "Jenny Colgan", ["Holiday Romance", "Contemporary Romance"], ["Small-Town Romance", "New Beginnings"]),
    Book("The Twelve Dates of Christmas", "Jenny Bayliss", ["Holiday Romance", "Contemporary Romance"], ["Friends to Lovers", "Small-Town Romance"]),
    Book("The Tourist Attraction", "Sarah Morgenthaler", ["Contemporary Romance", "Small-Town Romance"], ["Opposites Attract", "Grumpy x Sunshine"]),
    Book("The Simple Wild", "K. A. Tucker", ["Contemporary Romance"], ["Opposites Attract", "Small-Town Romance"]),
    Book("Wild at Heart", "K. A. Tucker", ["Contemporary Romance"], ["Second Chance Romance", "Small-Town Romance"]),
    Book("The Happy Ever After Playlist", "Abby Jimenez", ["Contemporary Romance"], ["Unexpected Romance", "Slow Burn"]),
    Book("The Cactus", "Sarah Haywood", ["Contemporary Romance"], ["Opposites Attract", "Single Parent"]),
    Book("The Bookish Life of Nina Hill", "Abbi Waxman", ["Contemporary Romance", "Romantic Comedy"], ["Opposites Attract", "Found Family"]),
    Book("The Rosie Project", "Graeme Simsion", ["Contemporary Romance", "Romantic Comedy"], ["Opposites Attract", "Slow Burn"]),
    Book("The Rosie Effect", "Graeme Simsion", ["Contemporary Romance", "Romantic Comedy"], ["Marriage in Trouble", "Opposites Attract"]),
    Book("The Flatshare", "Beth O'Leary", ["Contemporary Romance", "Romantic Comedy"], ["Forced Proximity", "Slow Burn"]),
    Book("The Switch", "Beth O'Leary", ["Contemporary Romance"], ["Small-Town Romance", "Opposites Attract"]),
    Book("The Secret Life of Albert Entwistle", "Matt Cain", ["Contemporary Romance", "LGBTQ+ Romance"], ["Second Chance Romance", "Coming of Age"]),
    Book("The Guncle", "Steven Rowley", ["Contemporary Fiction", "LGBTQ+ Romance"], ["Found Family", "Healing Together"]),
    Book("The Music of What Happens", "Bill Konigsberg", ["Young Adult Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Friends to Lovers"]),
    Book("What If It's Us", "Becky Albertalli and Adam Silvera", ["Young Adult Romance", "LGBTQ+ Romance"], ["Love at First Sight", "Opposites Attract"]),
    Book("Here's to Us", "Becky Albertalli and Adam Silvera", ["Young Adult Romance", "LGBTQ+ Romance"], ["Second Chance Romance", "Friends to Lovers"]),
    Book("Felix Ever After", "Kacen Callender", ["Young Adult Romance", "LGBTQ+ Romance"], ["Love Triangle", "Coming of Age"]),
    Book("The Gravity of Us", "Phil Stamper", ["Young Adult Romance", "LGBTQ+ Romance"], ["Celebrity Romance", "Opposites Attract"]),
    Book("Heartstopper: Volume One", "Alice Oseman", ["Young Adult Romance", "LGBTQ+ Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("Heartstopper: Volume Two", "Alice Oseman", ["Young Adult Romance", "LGBTQ+ Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("Heartstopper: Volume Three", "Alice Oseman", ["Young Adult Romance", "LGBTQ+ Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("Loveless", "Alice Oseman", ["Young Adult Romance"], ["Coming of Age", "Found Family"]),
    Book("Radio Silence", "Alice Oseman", ["Young Adult Romance"], ["Friends to Lovers", "Found Family"]),
    Book("The Upside of Unrequited", "Becky Albertalli", ["Young Adult Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("Simon vs. the Homo Sapiens Agenda", "Becky Albertalli", ["Young Adult Romance", "LGBTQ+ Romance"], ["Secret Identity", "Friends to Lovers"]),
    Book("The Miseducation of Cameron Post", "Emily M. Danforth", ["Young Adult Romance", "LGBTQ+ Romance"], ["Forbidden Love", "Coming of Age"]),
    Book("The Henna Wars", "Adiba Jaigirdar", ["Young Adult Romance", "LGBTQ+ Romance"], ["Rivals to Lovers", "Opposites Attract"]),
    Book("Hani and Ishu's Guide to Fake Dating", "Adiba Jaigirdar", ["Young Adult Romance", "LGBTQ+ Romance"], ["Fake Dating", "Opposites Attract"]),
    Book("Last Night at the Telegraph Club", "Malinda Lo", ["Young Adult Romance", "Historical Romance", "LGBTQ+ Romance"], ["Forbidden Love", "Coming of Age"]),
    Book("A Scatter of Light", "Malinda Lo", ["Young Adult Romance", "LGBTQ+ Romance"], ["Coming of Age", "Forbidden Love"]),
    Book("The Falling in Love Montage", "Ciara Smyth", ["Young Adult Romance", "LGBTQ+ Romance"], ["Fake Dating", "Friends to Lovers"]),
    Book("You Should See Me in a Crown", "Leah Johnson", ["Young Adult Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Lesbiana's Guide to Catholic School", "Sonora Reyes", ["Young Adult Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Coming of Age"]),
    Book("The Henna Artist", "Alka Joshi", ["Historical Romance"], ["Forbidden Love", "New Beginnings"]),
    Book("The Night Tiger", "Yangsze Choo", ["Historical Romance", "Fantasy Romance"], ["Forbidden Love", "Opposites Attract"]),
    Book("The Bird King", "G. Willow Wilson", ["Historical Romance", "Fantasy Romance"], ["Forbidden Love", "Adventure"]),
    Book("The Secret Garden", "Frances Hodgson Burnett", ["Historical Romance"], ["Found Family", "New Beginnings"]),
    Book("The Enchanted April", "Elizabeth von Arnim", ["Historical Romance"], ["New Beginnings", "Opposites Attract"]),
    Book("The Scarlet Pimpernel", "Baroness Orczy", ["Historical Romance"], ["Marriage of Convenience", "Secret Identity"]),
    Book("The Masqueraders", "Georgette Heyer", ["Historical Romance"], ["Secret Identity", "Opposites Attract"]),
    Book("The Corinthian", "Georgette Heyer", ["Historical Romance"], ["Forced Proximity", "Opposites Attract"]),
    Book("The Nonesuch", "Georgette Heyer", ["Historical Romance"], ["Grumpy x Sunshine", "Opposites Attract"]),
    Book("The Talisman Ring", "Georgette Heyer", ["Historical Romance"], ["Forced Proximity", "Enemies to Lovers"]),
    Book("The Reluctant Widow", "Georgette Heyer", ["Historical Romance"], ["Marriage of Convenience", "Secret Identity"]),
    Book("The Rake", "Mary Jo Putney", ["Historical Romance"], ["Opposites Attract", "Second Chance Romance"]),
    Book("The Spymaster's Lady", "Joanna Bourne", ["Historical Romance", "Romantic Suspense"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("The Black Hawk", "Joanna Bourne", ["Historical Romance", "Romantic Suspense"], ["Friends to Lovers", "Second Chance Romance"]),
    Book("The Rogue Not Taken", "Sarah MacLean", ["Historical Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("A Scot in the Dark", "Sarah MacLean", ["Historical Romance"], ["Opposites Attract", "Forced Proximity"]),
    Book("Brazen and the Beast", "Sarah MacLean", ["Historical Romance"], ["Grumpy x Sunshine", "Opposites Attract"]),
    Book("Nine Rules to Break When Romancing a Rake", "Sarah MacLean", ["Historical Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Duchess Hunt", "Jennifer Haymore", ["Historical Romance"], ["Friends to Lovers", "Forbidden Love"]),
    Book("The Secret of Pembrooke Park", "Julie Klassen", ["Historical Romance", "Gothic Romance"], ["Mystery", "Slow Burn"]),
    Book("The Lost Letter", "Mimi Matthews", ["Historical Romance"], ["Second Chance Romance", "Forbidden Love"]),
    Book("The Matrimonial Advertisement", "Mimi Matthews", ["Historical Romance"], ["Marriage of Convenience", "Opposites Attract"]),
    Book("The Work of Art", "Mimi Matthews", ["Historical Romance"], ["Marriage of Convenience", "Grumpy x Sunshine"]),
    Book("The Belle of Belgrave Square", "Mimi Matthews", ["Historical Romance"], ["Marriage of Convenience", "Opposites Attract"]),
    Book("The Siren of Sussex", "Mimi Matthews", ["Historical Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Lily of Ludgate Hill", "Mimi Matthews", ["Historical Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("The Winter Sea", "Susanna Kearsley", ["Historical Romance"], ["Time Travel", "Forbidden Love"]),
    Book("The Rose Garden", "Susanna Kearsley", ["Historical Romance", "Fantasy Romance"], ["Time Travel", "Second Chance Romance"]),
    Book("The Firebird", "Susanna Kearsley", ["Historical Romance", "Fantasy Romance"], ["Time Travel", "Forbidden Love"]),
    Book("The Outlander", "Diana Gabaldon", ["Historical Romance", "Fantasy Romance"], ["Time Travel", "Forced Proximity"]),
    Book("Dragonfly in Amber", "Diana Gabaldon", ["Historical Romance", "Fantasy Romance"], ["Time Travel", "Second Chance Romance"]),
    Book("Voyager", "Diana Gabaldon", ["Historical Romance", "Fantasy Romance"], ["Time Travel", "Second Chance Romance"]),
    Book("The Highlander's Touch", "Karen Marie Moning", ["Historical Romance", "Fantasy Romance"], ["Time Travel", "Opposites Attract"]),
    Book("Beyond the Highland Mist", "Karen Marie Moning", ["Historical Romance", "Fantasy Romance"], ["Time Travel", "Forbidden Love"]),
    Book("The Dark Highlander", "Karen Marie Moning", ["Historical Romance", "Fantasy Romance"], ["Time Travel", "Opposites Attract"]),
    Book("The Secret", "Julie Garwood", ["Historical Romance"], ["Enemies to Lovers", "Arranged Marriage"]),
    Book("The Bride", "Julie Garwood", ["Historical Romance"], ["Arranged Marriage", "Opposites Attract"]),
    Book("The Wedding", "Julie Garwood", ["Historical Romance"], ["Marriage of Convenience", "Opposites Attract"]),
    Book("Ransom", "Julie Garwood", ["Historical Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("The Lion's Lady", "Julie Garwood", ["Historical Romance"], ["Opposites Attract", "Secret Identity"]),
    Book("The Princess", "Julie Garwood", ["Historical Romance"], ["Opposites Attract", "Royal Romance"]),
    Book("The Gift", "Julie Garwood", ["Historical Romance"], ["Arranged Marriage", "Opposites Attract"]),
    Book("The Wedding", "Julie Garwood", ["Historical Romance"], ["Marriage of Convenience", "Opposites Attract"]),
    Book("The Bride Test", "Helen Hoang", ["Contemporary Romance"], ["Arranged Marriage", "Opposites Attract"]),
    Book("The Kiss Quotient", "Helen Hoang", ["Contemporary Romance"], ["Opposites Attract", "Slow Burn"]),
    Book("The Hating Game", "Sally Thorne", ["Contemporary Romance"], ["Enemies to Lovers", "Workplace Romance"]),
    Book("Beach Read", "Emily Henry", ["Contemporary Romance"], ["Rivals to Lovers", "Forced Proximity"]),
    Book("People We Meet on Vacation", "Emily Henry", ["Contemporary Romance"], ["Friends to Lovers", "Slow Burn"]),
    Book("The Spanish Love Deception", "Elena Armas", ["Contemporary Romance"], ["Fake Dating", "Enemies to Lovers"]),
    Book("The Unhoneymooners", "Christina Lauren", ["Contemporary Romance"], ["Enemies to Lovers", "Forced Proximity"]),
    Book("To All the Boys I've Loved Before", "Jenny Han", ["Young Adult Romance"], ["Fake Dating", "Friends to Lovers"]),
    Book("The Summer I Turned Pretty", "Jenny Han", ["Young Adult Romance"], ["Love Triangle", "Friends to Lovers"]),
    Book("Pride and Prejudice", "Jane Austen", ["Historical Romance"], ["Enemies to Lovers", "Grumpy x Sunshine"]),
    Book("The Duchess Deal", "Tessa Dare", ["Historical Romance"], ["Marriage of Convenience", "Grumpy x Sunshine"]),
    Book("The Cruel Prince", "Holly Black", ["Young Adult Romance", "Fantasy Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("The Selection", "Kiera Cass", ["Young Adult Romance", "Dystopian Romance"], ["Love Triangle", "Royal Romance"]),
    Book("Red, White & Royal Blue", "Casey McQuiston", ["Contemporary Romance", "LGBTQ+ Romance"], ["Enemies to Lovers", "Forbidden Love"]),
    Book("Cemetery Boys", "Aiden Thomas", ["Young Adult Romance", "Fantasy Romance", "LGBTQ+ Romance"], ["Opposites Attract", "Forced Proximity"]),
]

    

GENRES = [
    "Contemporary Romance",
    "Historical Romance",
    "Fantasy Romance",
    "Paranormal Romance",
    "Romantic Comedy",
    "Young Adult Romance",
    "LGBTQ+ Romance",
    "Romantic Suspense",
    "Science Fiction Romance",
    "Gothic Romance",
    "Small-Town Romance",
    "Holiday Romance",
    "Dystopian Romance",
    "Contemporary Fiction"
]

TROPES = [
    "Enemies to Lovers",
    "Friends to Lovers",
    "Rivals to Lovers",
    "Grumpy x Sunshine",
    "Opposites Attract",
    "Forced Proximity",
    "Fake Dating",
    "Fake Engagement",
    "Marriage of Convenience",
    "Arranged Marriage",
    "Second Chance Romance",
    "Slow Burn",
    "Love Triangle",
    "Forbidden Love",
    "Friends with Benefits",
    "One Bed",
    "He Falls First",
    "She Falls First",
    "Mutual Pining",
    "Found Family",
    "Small-Town Romance",
    "Secret Identity",
    "Single Parent",
    "Bodyguard Romance",
    "Love at First Sight",
    "Celebrity Romance",
    "Time Travel",
    "Pen Pals",
    "Unexpected Romance",
    "First Love",
    "Love After Loss",
    "Coming of Age",
    "Family",
    "Adventure",
    "True Love",
    "Royal Romance",
    "Fated Mates",
    "Mystery",
    "Star-Crossed Lovers",
    "Musician Romance",
    "Marriage in Trouble",
    "Healing Together",
    "New Beginnings",
    "Summer Romance",
    "Workplace Romance",
    "Holiday Romance"
]


def filter_books(books,selected_genres,selected_tropes):
    '''
    matching_books creates an empty listn to store books that match the users prefrences
    the first for loop checks every book
    the second loop checks whether the book has any of the user's selected genres
    the third loop checks whether the book has any of the user's selectedn tropes
    the if statement only adds books that match at least one selected genres and trope
    '''
    matching_books = []
    
    for book in books:
        genre_match=False
        trope_match=False
        
        for genre in selected_genres:
            if genre in book.genres:
                genre_match=True
        
        for trope in selected_tropes:
            if trope in book.tropes:
                trope_match=True
        
        if genre_match and trope_match:
            matching_books.append(book)
    
    return matching_books

assert_equal(
    filter_books(books, ["Contemporary Romance"], ["Enemies to Lovers"]),
    [book for book in books if "Contemporary Romance" in book.genres
     and "Enemies to Lovers" in book.tropes]
)

assert_equal(
    filter_books(books, ["Nonexistent Genre"], ["Nonexistent Trope"]),
    [])

@route
def index(state:State)->Page:
    '''
    Displays the home page of the Romance Book Generator.
    Introduces the website and gives the user a Start button
    that takes them to the genre selection page.
    '''
    return Page(state,[
        Header("♡ Romance Book Generator ♡ "),
        "Can't decide what to read next? Let us pick a random book for you!",
        "\n",
        "Choose your favorite genres and tropes to get a random recommendation!💗",
        "\n",
        Button("Start!","genre_page")
        ])

@route
def genre_page(state:State)->Page:
    '''
    Displays a list of romance genres using checkboxes.
    Allows the user to select multiple genres that they would
    like to see in their book recommendation.
    When the user clicks Continue, their selections are sent
    to the save_genres function
    the RelatedCheckBox allows users to pick multiple genres
    * puts all the gerneated checkboxes into the page as separate components
    
    '''
    return(Page(state, [
        Header("Choose Your Favorite Genres!"),
        "Select all the genres you would want in a book <3:",
        "\n",
    RelatedCheckBox("picks", "Contemporary Romance"),
        "Contemporary Romance",

        RelatedCheckBox("picks", "Historical Romance"),
        "Historical Romance",

        RelatedCheckBox("picks", "Fantasy Romance"),
        "Fantasy Romance",

        RelatedCheckBox("picks", "Paranormal Romance"),
        "Paranormal Romance",

        RelatedCheckBox("picks", "Romantic Comedy"),
        "Romantic Comedy",

        RelatedCheckBox("picks", "Young Adult Romance"),
        "Young Adult Romance",

        RelatedCheckBox("picks", "New Adult Romance"),
        "New Adult Romance",

        RelatedCheckBox("picks", "LGBTQ+ Romance"),
        "LGBTQ+ Romance",

        RelatedCheckBox("picks", "Romantic Suspense"),
        "Romantic Suspense",

        RelatedCheckBox("picks", "Dark Romance"),
        "Dark Romance",

        RelatedCheckBox("picks", "Sports Romance"),
        "Sports Romance",

        RelatedCheckBox("picks", "Science Fiction Romance"),
        "Science Fiction Romance",

        RelatedCheckBox("picks", "Gothic Romance"),
        "Gothic Romance",

        RelatedCheckBox("picks", "Small-Town Romance"),
        "Small-Town Romance",

        RelatedCheckBox("picks", "Workplace Romance"),
        "Workplace Romance",

        RelatedCheckBox("picks", "Western Romance"),
        "Western Romance",

        RelatedCheckBox("picks", "Holiday Romance"),
        "Holiday Romance",

        RelatedCheckBox("picks", "Dystopian Romance"),
        "Dystopian Romance",
        "\n",

        Button("Continue", "save_genres")
    ]))

@route
def save_genres(state: State, picks: list[str]) -> Page:
    '''
    Saves the genres selected by the user into the selected_genres
    list in the State dataclass. If the user does not select any
    genres, all available genres are selected by default.
    Then, takes the user to the trope selection page.
    '''
    if len(picks) == 0:
        state.selected_genres = GENRES
    else:
        state.selected_genres = picks
    return trope_page(state)

@route
def trope_page(state:State)->Page:
    '''
     Displays a list of romance tropes using checkboxes.
    Allows the user to select multiple tropes they would
    like included in their book recommendation.
    When the user clicks Find My Book, their selections
    are sent to the save_tropes function
    the RelatedCheckBox allows users to pick multiple genres
    * puts all the gerneated checkboxes into the page as separate components
    '''
    return(Page(state, [
        Header("Choose Your Favorite Tropes!"),
        "Select all the tropes you would want in a book <3:",
        "\n",
        RelatedCheckBox("picks", "Enemies to Lovers"),
        "Enemies to Lovers",

        RelatedCheckBox("picks", "Friends to Lovers"),
        "Friends to Lovers",

        RelatedCheckBox("picks", "Rivals to Lovers"),
        "Rivals to Lovers",

        RelatedCheckBox("picks", "Grumpy x Sunshine"),
        "Grumpy x Sunshine",

        RelatedCheckBox("picks", "Opposites Attract"),
        "Opposites Attract",

        RelatedCheckBox("picks", "Forced Proximity"),
        "Forced Proximity",

        RelatedCheckBox("picks", "Fake Dating"),
        "Fake Dating",

        RelatedCheckBox("picks", "Fake Engagement"),
        "Fake Engagement",

        RelatedCheckBox("picks", "Marriage of Convenience"),
        "Marriage of Convenience",

        RelatedCheckBox("picks", "Arranged Marriage"),
        "Arranged Marriage",

        RelatedCheckBox("picks", "Second Chance Romance"),
        "Second Chance Romance",

        RelatedCheckBox("picks", "Slow Burn"),
        "Slow Burn",

        RelatedCheckBox("picks", "Love Triangle"),
        "Love Triangle",

        RelatedCheckBox("picks", "Forbidden Love"),
        "Forbidden Love",

        RelatedCheckBox("picks", "Friends with Benefits"),
        "Friends with Benefits",

        RelatedCheckBox("picks", "One Bed"),
        "One Bed",

        RelatedCheckBox("picks", "He Falls First"),
        "He Falls First",

        RelatedCheckBox("picks", "She Falls First"),
        "She Falls First",

        RelatedCheckBox("picks", "Mutual Pining"),
        "Mutual Pining",

        RelatedCheckBox("picks", "Found Family"),
        "Found Family",

        RelatedCheckBox("picks", "Small-Town Romance"),
        "Small-Town Romance",

        RelatedCheckBox("picks", "Secret Identity"),
        "Secret Identity",

        RelatedCheckBox("picks", "Single Parent"),
        "Single Parent",
        
        "\n",

        Button("Find My Book! 💗", "save_tropes")
        ]))

@route
def save_tropes(state: State, picks: list[str]) -> Page:
    '''
    Saves the tropes selected by the user into the selected_tropes
    list in the State dataclass. If the user does not select any
    tropes, all available tropes are selected by default.
    Then, takes the user to the recommendation page.
    '''
    if len(picks) == 0:
        state.selected_tropes = TROPES
    else:
        state.selected_tropes = picks
    return recommendation_page(state)

@route
def recommendation_page(state:State)->Page:
    '''
    Filters the books based on the user's selected genres and tropes.
    If no books match the user's preferences, displays a message
    explaining that there are no matching books and provides a
    button to start over.
    If matching books are found, randomly selects one book and
    displays its title, author, genres, and tropes.
    Also gives the user the option to get another recommendation
    or return to the home page.
    '''
    matching_books = filter_books(
        state.books,
        state.selected_genres,
        state.selected_tropes)
    
    if len(matching_books)==0:
        return Page(state,[
            Header("No Matching Books :("),
            "We are so sorry!",
            Button("Start Over","index")
            ])
    
    state.recommended_book = random.choice(matching_books)
    book = state.recommended_book
    
    return Page(state, [
        Header("💕 Your Book Match! 💕"),
        "Title: " + book.title,
        "\n",
        "Author: " + book.author,
        "\n",
        "Genres: " + ", ".join(book.genres),
        "\n",
        "Tropes: " + ", ".join(book.tropes),
        "\n",
        Button("New Recommendation", "new_recommendation_page"),
        Button("Start Over", "index")
    ])

@route
def new_recommendation_page(state: State) -> Page:
    '''
    Generates a new book recommendation by calling the
    recommendation_page function again. The function uses
    the user's previously selected genres and tropes to
    find another random book that matches their preferences.
    '''
    return recommendation_page(state)

from bakery import assert_equal

# Test filter_books
assert_equal(
    filter_books(books, ["Contemporary Romance"], ["Enemies to Lovers"]),
    [book for book in books if "Contemporary Romance" in book.genres
     and "Enemies to Lovers" in book.tropes]
)

# Test filter_books with no matches
assert_equal(
    filter_books(books, ["Nonexistent Genre"], ["Nonexistent Trope"]),
    []
)

# Test save_genres
state = State(books, [], [], None)
save_genres(state, ["Contemporary Romance"])
assert_equal(state.selected_genres, ["Contemporary Romance"])

# Test save_genres with no selections
state = State(books, [], [], None)
save_genres(state, [])
assert_equal(state.selected_genres, GENRES)

# Test save_tropes
state = State(books, ["Contemporary Romance"], [], None)
save_tropes(state, ["Enemies to Lovers"])
assert_equal(state.selected_tropes, ["Enemies to Lovers"])

# Test save_tropes with no selections
state = State(books, ["Contemporary Romance"], [], None)
save_tropes(state, [])
assert_equal(state.selected_tropes, TROPES)

start_server(State(books,[],[],None))
