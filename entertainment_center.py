import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A boy's toys come to life!",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")


avatar = media.Movie("Avatar",
                     "Aliens and humans do the love dance!",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


lord_of_the_rings = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                                "Frodo takes the ring back to Mt. Doom!",
                                "https://www.movieposter.com/posters/archive/main/105/MPW-52979",
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")


rogue_one = media.Movie("Rogue One: A Star Wars Story",
                        "A Prequel to the 'Star Wars' Series",
                        "http://www.heavymetal.com/v2/wp-content/uploads/2016/01/star_wars_anthology__rogue_one_by_dan_zhbanov-d9b0ezn.jpg",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

the_shining = media.Movie("The Shining",
                          "A Man Goes Nuts in a Hotel!",
                          "http://i.ebayimg.com/images/i/222001098953-0-1/s-l1000.jpg",
                          "https://www.youtube.com/watch?v=1G7Ju035-8U")

scott_pilgrim = media.Movie("Scott Pilgrim v.s. the World",
                            "Scott Pilgrim fights many ex boyfriends",
                            "http://images.moviepostershop.com/scott-pilgrim-vs-the-world-movie-poster-2010-1010673017.jpg",
                            "https://www.youtube.com/watch?v=7wd5KEaOtm4")


movies = [toy_story,avatar,lord_of_the_rings,rogue_one,the_shining,scott_pilgrim]


#opens the html page with movie data populated
fresh_tomatoes.open_movies_page(movies)


