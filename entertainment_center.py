import fresh_tomatos
import media
toy_story=media.Movie("Toy Story",
                      "a story of a boy and his toys that come to life",
                      "https://cdn1.imggmi.com/uploads/2018/9/29/55f0bdf2d663a9d5f2a084861d3e1817-full.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar=media.Movie("Avatar",
                    "a marine on an alien planet",
                  "https://upload.wikimedia.org/wikipedia/commons/f/fb/James_cameron_avatar_by_ghostofzion2003.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
naruto=media.Movie("Itachi Uchiha",
                   "Genius Ninga who is work as a spy and killed his clan",
                   "https://upload.wikimedia.org/wikipedia/commons/1/10/Narutoniji.jpg"
                   ,"https://youtu.be/7RUylQDHQMk")

medoria=media.Movie("My Hero Academic",
                   "Izuku Midoriya, a boy born without quirks in a world where they are the norm, but who still dreams of becoming a hero himself. He is scouted by the world's greatest hero, who shares his quirk with Izuku after recognizing his value and later enrolls him in a high school for heroes in training.",
                   "https://upload.wikimedia.org/wikipedia/commons/f/fe/Boku_no_Hero_Academia_Heroes_Anime_Wallpaper_HD.0.jpg"
                   ,"https://www.youtube.com/watch?v=wIb3nnOeves")
yagami=media.Movie("Death Note",
                   "Light Yagami (Tatsuya Fujiwara) is a normal, undistinguished college student -- that is, until he discovers an odd notebook lying on the ground. He soon discovers that the notebook has magic powers: If someone's name is written on it while the writer imagines that person's face, he or she will die. Intoxicated with his new godlike power, Light kills those he deems unworthy of life. But a mysterious detective known only as L (Ken'ichi Matsuyama) becomes determined to put a stop to his reign.",
                   "https://upload.wikimedia.org/wikipedia/commons/5/54/Death_Note_Light_Up_the_New_World_poster.jpg"
                   ,"https://www.youtube.com/watch?v=gvxNaSIB_WI")
sata=media.Movie("Major2nd",
                   "Years after the previous series, Daigo Shigeno who is now in elementary school student, dreams to become a professional baseball player just like father and former major leaguer, Goro Shigeno. Following in his dad's footsteps, Daigo joined the little league team “Mifune Dolphins”, but finds his skills lacking and fell under the pressure from his peer players of becoming the second generation. Eventually, Daigo gave up baseball before even trying it out for a year and lived his life apathetically. Now in the 6th grade, he meets a new transfer student who returned home from America. The boy's name is Hikaru Sato, whose father is Toshiya Sato, a former major leaguer and a longtime friend of Goro. And the wheel of fate concerning these young lads is about to spin!",
                   "https://upload.wikimedia.org/wikipedia/commons/3/37/Major-2nd.jpg"
                   ,"https://www.youtube.com/watch?v=Sia72VndlZw")
movies=[toy_story ,avatar,naruto,medoria,yagami,sata]
fresh_tomatos.open_movies_page(movies)
#https://en.wikipedia.org/wiki/My_Hero_Academia#/media/File:Boku_no_Hero_Academia_Volume_1.png
#naruto.show_trailer()
#avatar_story=avatar.story
#print(avatar_story)
#avatar.show_trailer()
