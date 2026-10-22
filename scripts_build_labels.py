import csv

# Each row: (text, label, note)
# label is my (AI) provisional label per label_definitions.txt — every row
# needs human review before it counts as real data, per the Milestone 4
# workflow ("read and correct every single one").

rows = []

def add(text, label, board, hard=None):
    note = f"pre-labeled ({board} board), needs review"
    if hard:
        note += f" — HARD CASE: {hard}"
    rows.append((text.strip(), label, note))

# ---------------- The Dark Knight ----------------
add("1. Bale sucked as Batman - if the titular character makes you laugh at how absurd he sounds every time he opens his mouth, you know there's something wrong\n2. Maggie Gyllenhaal - simply not attractive enough to play Batman's love interest and her performance was lousy too\n3. Dialogue - some of the dialogue is absolute cringe and clunky as hell. For example - \"he's the hero Gotham deserves, but not the one it needs...\" Blah blah blah\n4. The score is completely generic and forgettable - I like some of Hans Zimmer's past work but this was such a generic score. Was there even a theme? Could you hum it right now to save your life? Compare this to Batman 89 which had one of the most memorable and iconic themes of all time\n5. Visually uninspiring - the movie has a very plain aesthetic to it, like something you'd see in an episode of CSI.\n6. Heath Ledger - his performance was probably the best thing about the movie but also massively overrated because of his death. It was good don't get me wrong, but he wouldn't have got half the praise (or the Oscar) if he was still alive. Just facts.", "hot_take", "The Dark Knight")
add("Bingo", "reaction", "The Dark Knight")
add("I disagree.", "reaction", "The Dark Knight")
add("Well I agree with the OP.", "reaction", "The Dark Knight")
add("Yeah. Sums it up. Maggie was ok, but I never understood the praise this movie got. Just a meh superhero movie.", "reaction", "The Dark Knight")
add("I thought this movie was overrated in 2008 when I saw it, and I still think that today. However, over the years I've warmed up to its attempt to portray superhero's/supervillains as people that could actually exist in the real world. The scenes between Batman and Joker in the interrogation room are the best it has to offer, and the opening bank heist is visceral and well shot. But after that the movie begins to fall apart. What is not so forgivable are the insane amount of plot holes and ridiculous contrivances in the script. The Joker's plans require so many coincidences that it beggars belief, such as his phone-bomb escape from the police station and kidnapping Rachel and Harvey and having Batman setup in an elaborate plot. The Two-Face makeup effects on Eckhart also look ridiculous and lose any suspension of disbelief. The fact that he's missing the skin on half his face, with his bare eyeball, muscle, bone and tendons exposed, is just silly. He would have been dead from shock or an infection in minutes.", "analysis", "The Dark Knight")
add("You must be a big movie buff? Because you write like you are.", "reaction", "The Dark Knight")
add("Movie poster:\nhttp://www.imdb.com/title/tt0468569/mediaviewer/rm4023877632\n9/11 first plane impact:\nhttps://www.youtube.com/watch?v=MP5eFR97OX0", "theory", "The Dark Knight")
add("Yes. Beyond any hint of doubt or dispute. That's far from the only reference, visual and otherwise.", "hot_take", "The Dark Knight")
add("Yes, and there were huge arguments over on IMFB at the time about that.", "reaction", "The Dark Knight")

# ---------------- Pulp Fiction ----------------
add("Here we are again with Pulp Fiction. I started watching it again yesterday, third time I guess, and the more I watch it, the more I see this movie as a bunch of vignettes. There's no plot at all, there is a lot of mannerism in the characters and the scenes are wrapped with 60s and 70s songs to create an artificial atmosphere, an environment, but the movies still sounds empty. At the end of the day, this is a movie that romanticizes the drug lifestyle and its charachters. What made the alleged \"greatness\" of this movie? The critics, of course, who started hyping this movie describing it as a masterpiece when it's just a movie convoluted with gratuitios violence which heavily borrows from the Hong Kong B-movies. Nevertheless, critics didn't call Tarantino out. Nobody exposed the plagiarism and the lack of original ideas, not to mention the absolute lack or artistic quality.", "hot_take", "Pulp Fiction")
add("I still like this film, even with the overly verbose dialogues (which made it so \"hip\" at the time, at least in part). The major dip for me is Tarantino himself in the film -- as well as the lines he gives himself. Makes it almost unbearable. So I mute that part of the film upon rewatches. The nonlinear storytelling is fun. The other performances great. I'd still give it a 9/10 overall.", "hot_take", "Pulp Fiction")
add("9 out of 10 for a b-movie filled with garbage? As I said, if these movies became the \"masterpieces\" of modern cinema, cinema is in big trouble...", "reaction", "Pulp Fiction")
add("The non-linear structure means that the audience feels happy seeing John Travolta alive at the end.", "analysis", "Pulp Fiction")
add("Does it suffice to say that this is a good movie?", "reaction", "Pulp Fiction")
add("Sometimes people call a movie good because it makes them feel good.", "hot_take", "Pulp Fiction")
add("I cant see that at all", "reaction", "Pulp Fiction")
add("This movie rocks. Nuff said. I guarantee in 2026 moving forward, you won't see movies like this made ever again.", "hot_take", "Pulp Fiction")
add("Although it's not the mafia, Wallace's crew was still organized crime. You think he would have really let Jules leave to wander the world all willy-nilly after his spiritual awakening? I wonder if there's a theory that Wallace had Jules clipped for trying to leave.", "theory", "Pulp Fiction")
add("I feel like Marsellus actually would have, yes. I don't know why, but I get the impression that Jules would have been real respectful about it and Marsellus would have let him walk. It might be because Marsellus knows any assassins he sends after Jules just ain't coming back. It might be because Marsellus had a code of honour. I don't know. Ordinarily, not so much; most gangsters don't let you give them two weeks' notice, as it were; but I think Jules could have. Some people have fan theories that the piano player in Kill Bill (at the wedding, Vol.2) is Jules, walking the earth. I liked that theory for a while, but more and more I think... nah.", "analysis", "Pulp Fiction", hard="cites a specific checkable detail (the Kill Bill piano-player cameo theory) in support of an interpretation, but never actually endorses it — poses as open speculation while being built on a named, checkable reference")

# ---------------- Whiplash ----------------
add("The plot was cartoonish at times. He gets hit by car but proceeds to go to band practice? ha! Jk Simmons character was way over the top. These things don't happen in real life. The dinner table and break-up scene was literally just there to push the narrative forward but again was not believable! Overrated movie!", "analysis", "Whiplash")
add("I agree!! Way too intense. That guy would never be able to treat his band like that. That scene after the car crash was, as you say, unbelievable. I think J.K. Simmons won a supporting Oscar because he had to exert so much energy.", "hot_take", "Whiplash")
add("I tend to agree. It was an interesting premise, but it was OTT. If it was done with a defter touch... it might've been an interesting film about obsession, ambition etc. One example is Andrew's relationship with Nicole. It was not given any real screen time to chart a rise and fall, so when Andrew breaks it off, it has little impact.", "analysis", "Whiplash")
add("Andrew's relationship was a blip on the screen because in the end, he didn't really care that much for her. It had \"little impact\" on him.", "reaction", "Whiplash")
add("While I thought it was a very good movie I disagree with the 8.5 rating that it gets, I feel it deserves a 7.0 rating at the most although I personally give Whiplash an 8/10.", "hot_take", "Whiplash")
add("I DO music. I would give this a 2/10 because I could not suspend my disbelief enough that an insane psychopath like that would not be fired or in jail after the first over the top abusive outbreak. It was like some cray cray nonexistent cartoon land. Too far from human reality for me.", "analysis", "Whiplash")
add("Fletcher (to me) implied his drill instructor narcissism was all an act at the coffee shop when he calmly explained to Andrew that his cruel methods was for motivation and bringing out the absolute best. In the same vein how drill sergeants are intentionally mean to cadets to mold them into soldiers. You also see him hug his friend and kindly greet his friend's daughter. I don't know if that was for irony or to show his real persona. Then again, it's also very possible that his calm nature was an act since he tries to sabotage (or test) Andrew's performance in the finale.", "analysis", "Whiplash", hard="cites three specific, checkable scenes (coffee-shop talk, the hug, the finale sabotage) but never settles on an answer — the hardest-boundary example used in the README (analysis vs. theory)")
add("When I was young, I had a friend who seemed to have a really cool father. It turns out that his father was abusive. I never saw any of that. Well, I think Fletcher was sick like that. Just because he was sick in the head didn't mean that he was complete evil.", "theory", "Whiplash")

# ---------------- The Godfather ----------------
add("You see, the boss of a crime family would always need a guy with a funeral parlor. It's the ultimate mop-up spot. You never know when you're gonna need a body to disappear, or get cleaned up nice. So, how do you get a squeaky-clean mortician in your pocket? You don't ask him. You back him into a corner. Bonasera's beautiful daughter goes out with a couple of punks... They beat her half to death and then it goes to court. And what happens? The judge suspends the sentence. The judge. A judge in New York in the 1940s giving a suspended sentence for that kind of beating? Come on. He says, \"Someday, and that day may never come, I'll call upon you to do a service for me.\" Now the guy's got Vito Corleone as a \"friend\".", "analysis", "The Godfather")

# ---------------- The Room ----------------
add("I mean, the guy is clearly a dumbass. How did he even manage to scrape together $6 million?", "theory", "The Room")
add("Yeah it definitely involves something dodgy/illegal.", "reaction", "The Room")
add("i'd bet on either drug money or some kinda pimp action.", "reaction", "The Room")
add("If the guys background is really such a mystery... and he is a dumbass (which sounds right to me)... Why not inherited money? I know a number of people who are thick as bricks but inherited tens of millions. Maybe some defective genes were involved.", "theory", "The Room")
add("Could also be lottery winners. They tend to waste thier money quickly or get killed by the mob (seriuosly, winning a lottery increases chances of you dying 800% and chances of people around you dying 270%).", "analysis", "The Room", hard="names a specific stat (800%/270%) to back the claim, but when challenged (\"do you have the specific data/quote?\") the only source turns out to be a random Reddit comment — tests whether a dubious or poorly-sourced fact still counts as 'checkable' for the analysis label")
add("What does it mean \"increase by 800%\"? You mean, in the next year or something similar? Do you have the specific data/quote?", "reaction", "The Room")
add("This is a long writeup but worth the read if you are really interested: https://www.reddit.com/r/AskReddit/comments/24vo34/whats_the_happiest_5word_sentence_you_could_hear/chb38xf/", "analysis", "The Room")
add("There are dozens of millionaire lottery winners every single week in most countries and to have a handful of instances where it's squandered or goes bad since the 80's refutes the claim that it's bad.", "analysis", "The Room")

# ---------------- Inception ----------------
add("She was convinced that she was still dreaming so she killed herself... At the end of the film, the focus was shifted on the never-ending spinning totem, which points towards the conclusion that Cobb was still dreaming after all of the occurred events... So Mal woke up from her dream as she prophesied...Cobb was wrong and continued living in his dream... So in the end, was Mal right?", "theory", "Inception")
add("Nope.", "reaction", "Inception")
add("Yes and no. The key to understanding the ending is to ignore whether the top is spinning or not and to focus on WHOSE totem the top was. We are told Cobb found Mal's totem, then just casually decided to make it his own totem. But that's not how totems work. What was Cobb's original totem? We are never shown or told. The top was and will always remain Mal's totem. Therefore, the person who is really dreaming all that we see is Mal.", "analysis", "Inception")
add("If you watch this now, it sucks, contrary to what happened to Source Code, amazing movie, less pretentious and millions of times more fun to watch. So why the rating hasn't dropped down? Lazy people left their original ratings. But it deserves a 2.1", "hot_take", "Inception")
add("Source Code was a good movie, except the ending dragged on. Inception is not dated -- not in the least. The rating did drop down when the movie came out on video (as almost all movies do.)", "hot_take", "Inception")
add("Yeah, I would have ended that movie just 2 seconds after defreezing the frames, without saying 'it worked'. Cause to me, that's real closure.", "reaction", "Inception")
add("\"immature\" describes your post perfectly. I wish there were more adults online.", "reaction", "Inception")
add("Nolan was riding a hot streak because Heath Ledger's death added some fanfair to his previous film, and thus with his new film, there was chatter that it was so smart and brilliant.", "analysis", "Inception")

# ---------------- Fight Club ----------------
add("I have seen it three times trying desperately to figure out what makes this film so special but i just reached the conclusion that Fight Club is the most overhyped and overated film of all times since for some reason it is included in the top ten films in imdb. I personally gave it a 6/10 and got rid of my original dvd copy.", "hot_take", "Fight Club")
add("OK. You've expressed your opinions. Overhyped, overated (sic), weakest, can't believe its(sic) rated higher than..., 6/10. Now. WHY do you believe what you do? This is how to make a cogent OP, please work with this in the future. 1) state your opinion 2) state WHY you hold the opinion 3) give EXAMPLES of WHY you hold the opinion 4) restate your opinion and close", "reaction", "Fight Club")
add("In the car scene, when Tyler's telling the Narrator to just let go, why does Tyler put on the seat belt? It seems to be a direct rebuttal of his philosophy. My guess is that Tyler has limits (eg when Narrator shot at the van full of Nitroglycerin, he freaked out) and doesn't want to die. Any thoughts?", "analysis", "Fight Club", hard="phrased as an open question (\"Any thoughts?\") but the guess is built on a specific, checkable scene (the nitroglycerin van) — tests whether question-framing or cited evidence decides the analysis/theory boundary")
add("Uh, consdering the plot twist, it sounds like you and others don't understand how multiple personality disorder works.", "reaction", "Fight Club")
add("I get the concept of split personality. Still, I don't buy that. If that is the case, then the Narrator is the scared personality, and Tyler is the fearless personality. But if he's totally fearless, why would he put his seat belt on?", "analysis", "Fight Club")
add("The other personality took over briefly.", "hot_take", "Fight Club")

# ---------------- Parasite ----------------
add("Boring movie, wasn't funny, wasn't shocking. What was the point of this movie? How the heck did this film win Best Picture? And how can it be described as a dark comedy when I didn't even chuckle once?", "hot_take", "Parasite")
add("Alright, guys. Stop calling this a dark comedy because 6248 didn't chuckle once.", "reaction", "Parasite")
add("Ok, it's a light comedy now.", "reaction", "Parasite")
add("Well, there's plenty of lights being turned on and off.", "reaction", "Parasite")
add("I totally disagree. I thought it was entertaining and well made. The actors did a great job and the screenplay was excellent.", "hot_take", "Parasite")
add("Yeah, we found it sort of disappointing also. 6/10 and not of sufficient caliber to be the Oscar winner.", "hot_take", "Parasite")
add("It started off interesting but didn't pay off in the end IMO", "hot_take", "Parasite")
add("I thought it was unconventional, entertaining and thought provoking. And at times darkly funny.", "hot_take", "Parasite")
add("Well at least you got something right.", "reaction", "Parasite")
add("\"it went all Tarantino\" .. doesnt Tarantino admit to steal vision and material from the Koreans all the time tho? Or Japanese, I dont remember...", "theory", "Parasite")
add("You'd think they'd be rich already with this massive talent", "theory", "Parasite")
add("Because that's not the story the creators were telling. DUH!", "hot_take", "Parasite")
add("Were they good? They got caught.", "reaction", "Parasite")

# ---------------- Joker ----------------
add("Almost unheard of for any kind of movie but especially a CBM. Just...wow.", "hot_take", "Joker")
add("There are over 200 movies with a lower 2nd weekend. Passion of the Christ. Avatar. Lord of the Rings: The Fellowship of the Rings. Aquaman: (-23.2). The Incredibles. American Sniper. Big Hero 6 (-38.3) Just missed the cut-off! The list is from BoxofficeMojo.com.", "analysis", "Joker")
add("Quite a few of those movies had their second weekend fall during the the very lucrative Christmas holiday week. Also, I said \"especially a CBM\" and the only CBM on your list was Aquaman which...had it's second weekend land during Christmas break.", "analysis", "Joker")
add("No Norrinrad...its well known that many of them had their second weekend fall during Christmas week which famously gooses grosses to the high heaven. Nice try, though.", "reaction", "Joker")
add("So are you saying they are disqualified from being in the -37% or lower club? You're hilarious. The Joker is special to you for some reason.", "reaction", "Joker")
add("I think there was nothing wrong with making fun of Arthur's video. He didn't know he had a medical condition, but even if he did, that still wouldn't be wrong. Comedy often offends people, that's what comedy is. Inviting him on the show to make fun of him did cross the line though. It would've been OK if he was honest about his intentions from the start.", "hot_take", "Joker", hard="reasons carefully from stated premises but never cites a specific checkable fact (a line, a date, a production detail) — tests whether well-reasoned argument alone is enough for analysis, or whether a named checkable detail is required")
add("A normal person would have seen Murray's invite on the show for what it was - a parody of his video. A normal person would have either declined to go on the show or go and be man enough to laugh it off.", "hot_take", "Joker")

# ---------------- No Country for Old Men ----------------
add("why does lewelyn moss even go to shady motels and just sit around? just take the money out of the bag, put it in a new bag, head for costa rica or something", "analysis", "No Country for Old Men")
add("Movie would be over", "reaction", "No Country for Old Men")
add("they should make an honest movie, even if it was 5 minutes long, it would be refreshing to see it just end with common sense.", "reaction", "No Country for Old Men")
add("Are you serious Mr T you better rethink that. Movies aren't about common sense they are about magic.", "hot_take", "No Country for Old Men")
add("ok, well maybe we could show more realism in films... I think it would be a breath of fresh air to see Anton or someone sitting for 25 minutes reading a newspaper, or taking a crap or brushing there teeth, flossing and then using mouthwash.", "analysis", "No Country for Old Men")
add("Mr T just doesn't understand movies. Thank goodness very few filmmakers listen to him. He doesn't understand the power of fiction.", "reaction", "No Country for Old Men")
add("Sitting on the crapper and reading a newspaper is \"real life grit?\" I thought escaping that type of mundane nothingness was why people went to the movies.", "reaction", "No Country for Old Men")
add("I've probably rewatched this movie about 10 times I first discovered it in 2018 and I almost never rewatch movies unless they're this good. The plot and acting are 100% on point and kept me engaged the whole movie.", "hot_take", "No Country for Old Men")
add("I feel exactly the same. I watch it once a year and have for several years. It's a masterpiece.", "reaction", "No Country for Old Men")
add("Blood father is good movie with Melvin Gibson", "reaction", "No Country for Old Men")
add("I'm sorry but that honor goes to \"Ernest Scared Stupid\".", "reaction", "No Country for Old Men")
add("I love movies like this where just one little mistake snowballs into a massive clusterf***. If the protagonist had simply stayed home with the money instead going back to help nasty drug dealers he would have lived a long and prosperous life.", "analysis", "No Country for Old Men")
add("I prefer Platoon, Jaws, Mad Max 2 but I agree NCFOM ranks very high in the great movie category.", "hot_take", "No Country for Old Men")

# ---------------- The Matrix ----------------
add("Forget grand philosophical conspiracy theories about reality being a giant computer simulation. The most rational way to interpret this movie is that Neo is a shy, socially-awkward computer nerd who spends way too much time sitting in front of his computer screen. The \"Matrix\" is the Internet. Gradually, Neo finds the courage and strength to venture out into the real world.", "theory", "The Matrix")
add("I don't find politics particularly rational at all. This is just a planet of insane people, so it's easy to forget that politics originally exists JUST to 'create policy', and that's it.", "hot_take", "The Matrix")
add("I didn't particularly love this film upon first viewing; I got very bored with it and I did not see much that was special in it besides some of the innovative action. As this film has a huge fan base, I would love to hear why you love it.", "theory", "The Matrix")
add("Judging by your comments your favourite movie would be the Twilight series..", "reaction", "The Matrix")
add("I simply stated that I enjoyed the action but was bored. How exactly would you surmise that from two general statements?", "reaction", "The Matrix")
add("Because it has amazing action scenes and an innovative story. Its hard to believe anyone with intelligence would be \"bored\" by it.", "hot_take", "The Matrix")
add("After seeing your other posts, you seem post solely about people's intelligence. Action movies are typically inherently stupid, and I did not open my eyes enough.", "reaction", "The Matrix")
add("You are dumb, so everything you do is inherently wrong. If a creative, innovative, visually stunning movie bores you, the things that would cater to a mind like that, are a plague on society.", "hot_take", "The Matrix")

# ---------------- Titanic ----------------
add("Rose didn't really meet Jack until after 1 day. So in 3 days she cheats on her fiance, has sex with a stranger, gets him to draw her naked and seals a multi million piece of jewel off him. In 3 fkn days!", "analysis", "Titanic")
add("Reminds me of the Craig David song: https://www.youtube.com/watch?v=P5lmb5-tnM0", "reaction", "Titanic")
add("Craige David took 7 days! lol That's called taking things slowly by Jack and Rose's standards", "reaction", "Titanic")
add("No, he met this girl on Monday and was making love to her by Wednesday, that's only 3 days :)", "analysis", "Titanic")
add("You should watch True Romance (starring Christian Slater and Patricia Arquette). Things escalate really quickly in that movie. Two people meet today, get married tomorrow, and next thing you know they are killing people for each other.", "reaction", "Titanic")
add("Rose was written as a young woman engaged to a man she didn't love, or perhaps even like. She was a women in crisis at a turning point in her life. She very seriously contemplated suicide. Becoming fascinated than smitten with a young, honest, free, and HOT young man isn't as far fetched as one might think.", "analysis", "Titanic")
add("That is so 2024", "reaction", "Titanic")
add("True. And he refused to attend the ceremony because of that.", "analysis", "Titanic")
add("I can't believe he thought that was an Oscar worthy performance. Wow.", "hot_take", "Titanic")
add("He didn't deserve a nomination. His performance was fine but nothing crazy good. Then again, this film should not have swept the way it did.", "hot_take", "Titanic")
add("lol! whuy?", "reaction", "Titanic")
add("Maybe because some of us prefer L.A Confidential, As Good as it gets, and Good Will Hunting.", "hot_take", "Titanic")
add("I guess because feminism is popular now.", "hot_take", "Titanic")
add("Being too good looking is its own curse, Katie Holmes's Rachel Dawes was heavily criticised, but Maggie Gyllenhaal's in the subsequent film was praised. I don't think Maggie Gyllenhaal's Rachel Dawes was better, at all. The OK looking actors did something good, it is because their acting abilities. But the very good looking ones are of course because of the pretty faces.", "hot_take", "Titanic")
add("I liked Gyllenhaal a lot better, although I think some of that is her natural presence vs. Katie Holmes'. Gyllenhaal felt like a professional, young attorney working in the DA's office, Katie Holmes felt like a trust fund kid.", "hot_take", "Titanic")

# ---------------- Seven ----------------
add("People saying Mills would get a life sentence or even 10 years is absurd. There's no way it would even go to trial. Cops kill people on the streets on a daily basis with no consequences. No jury would ever convict Mills. I mean he was clearly provoked, he just found out that John Doe had murdered his wife and baby and then he brought her head out to him.", "analysis", "Seven")
add("I agree. Considering the fact his wife and unborn baby were murdered and his wife's head was delievered in a box no jury would convict him. Safe to say he really was temporarily insane.", "analysis", "Seven")
add("He shot an unarmed, handcuffed suspect in police custody. There's no way it would even go to trial. Lots of crimes don't go to trial. Doesn't mean the accused doesn't do some time.", "analysis", "Seven")
add("A man was standing in front of his wife's killer just moments after finding out he beheaded her while she was pregnant... Not a single judge on this planet with any form of empathy and sanity would sentence a man broken like that. There was a man who gunned down his daughters rapist a few years ago and only got probation.", "analysis", "Seven")
add("I think it would be a plea deal of not guilty by reason of temporary insanity. He'd probably get a suspended sentence or something, but his career as a cop would be over.", "analysis", "Seven")
add("This is another great example of how movies were overdone in the 1990s, just like The Matrix. They tried to make NYC look gloomy and bleak. Well, it rains all the time and everyone's offices look like they haven't been tidied up in 10 years. Take this scene: cab driver:\"where are we going?\". Somerset: \"very far from here\". Turns out they were just going to the city library. Brad Pitt was a terrible actor back then.", "analysis", "Seven")

# ---------------- Memento ----------------
add("I've seen this film over 20 times and have come to the conclusion that Leonard IS in fact faking his illness. He does not actually have brain damage. I based this on: 1. Even though he \"cannot\" make ANY new memories, he still remembers certain things, such as knowing he has a photograph of everything and an entire file on his wife's murder. 2. Every time he meets someone new, his memory instantly resets. 3. The scene where he meets Natalie at the restaurant, he clearly looks right at her as if he knows its her, yet then keeps walking by. 4. If he cant remember anything, how does he know he has no short term memory?", "analysis", "Memento")
add("I can live with that.", "reaction", "Memento")
add("Essentially yes", "reaction", "Memento")
add("Regarding all the people he has killed, he believed that they were the ones who killed his wife. His conscience never arose because he thought he was killing his wife's murderer", "analysis", "Memento")

# ---------------- Donnie Darko ----------------
add("Like another Millennial classic, Napoleon Dynamite, I just don't get the big deal, yet so many people seem to love this.", "hot_take", "Donnie Darko")
add("I agree about both. I never bought into the hype of either one.", "reaction", "Donnie Darko")
add("\"Donnie Darko\" was a very good movie IMHO. It did speak to cultural trends at the time. It was relevant.", "hot_take", "Donnie Darko")
add("The rabbit appears to be -- for whatever reason -- used as a metaphor for various mental illnesses. I think of films such as Harvey, Lynch's Inland Empire, Watership Down, that have used rabbits to exhibit/symbolize some form of psychological/mental issue. There's also \"Jack Rabbit Slims\" in Pulp Fiction.", "analysis", "Donnie Darko")
add("It has a very unique vibe/atmosphere, set up right from the beginning with \"The Killing Moon\". Replacing it with \"Never Tear Us Apart\" in the Director's Cut was a huge mistake.", "analysis", "Donnie Darko")
add("It is one of the most intelligent films I've ever seen. The re-release dumbed it down significantly. The original gives the absolute bare minimum amount of information to piece together what is an incredibly complex, elaborate, and deep story.", "hot_take", "Donnie Darko")
add("shouldn't review movies anymore. This is not the type of movie that deserves a 1 star rating. I could understand someone not getting this film, but giving it a 1 star rating, just seems laughable to me.", "hot_take", "Donnie Darko")
add("I liked You Don't mess with the Zohan..", "reaction", "Donnie Darko")
add("Therefore, the OP was referring to viewers such as yourself.", "reaction", "Donnie Darko")
add("Well I gave Donnie Darko a 10/10, so no.", "reaction", "Donnie Darko")
add("Then it would've been helpful for you to include that information in your post in order to make your point.", "reaction", "Donnie Darko")
add("Shut up.", "reaction", "Donnie Darko")
add("Make me.", "reaction", "Donnie Darko")

# ---------------- The Shining ----------------
add("There's been a lot of talk about the miscasting of Shelley Duvall up here, and I must agree. But did they HAVE to have her look like she never....ever washed her hair?? Now that I mention it, they ALL looked silly hair-wise.", "hot_take", "The Shining")
add("If you were isolated with no human contact besides your husband and son for 6 months, do you REALLY give a crap how your hair looks, etc? Quite frankly, if I were the winter caretaker in that kind of lengthy isolation, I'd pack a handful of outfits and spend the rest of the winter in my pajamas!", "theory", "The Shining")
add("for me, not looked but felt. ugh! although she might be wanting to ration her soap/shampoo/conditioner during that time. I hope the hotel provided them with a budget for laundry and body soap.", "theory", "The Shining")
add("I think Kubrick wanted her hair to look that way. It goes with the atmosphere of terror and isolation. Kubrick was a realist and understand that if you are being terrorized mentally and physically by a mad man your hair is not going to be perfect.", "analysis", "The Shining")
add("I agree with both of you about hair while at the hotel...although I'd still keep it rather clean. But I was referring to before they even went to the Overlook. Wendy looked greasy & disheveled even while in Boulder.", "hot_take", "The Shining")
add("What the hell kind of hotel in the mountains of Colorado closes in the winter? Instead of hiring someone to babysit the hotel for five months straight, how about you just hire someone to plow the goddamn road?", "theory", "The Shining")
add("Agreed", "reaction", "The Shining")
add("Isn't this specifically addressed in the interview scene? The explanation given seemed perfctly adequate to me.", "theory", "The Shining")
add("ULLMAN: Let's see, where were we? Yes. I was about to explain that eh... our season here runs from oh May 15th to October 30th and then we close down completely until the following May. JACK: Do you mind if I ask why you do that? ULLMAN: the problem is the enormous cost it would be to keep the road to the Sidewinder open. It's a 25 mile stretch of road, gets an average of 20 feet of snow during the winter, and there's just no way to make it economically feasible to keep it clear.", "analysis", "The Shining")
add("That last line basically answered all the topic creator's questions lol", "reaction", "The Shining")

# ---------------- Interstellar ----------------
add("\"From the director who apparently gets a lifetime pass to make crap simply because he made The Dark Knight.\" HONESTLY, setting aside the wave of disappointment that hit when this thing was released in theatres, the movie itself is just flat out moronic. It's poorly written and about as entertaining as watching paint dry.", "hot_take", "Interstellar")
add("THANKFULLY somebody saw the movie I just watched and felt the same exact way about it! It was horrible! I fast forwarded thru some of it because it was just that freaking bad!!", "reaction", "Interstellar")
add("It's not just us. I'd say a vast majority were disappointed in this film and a lot of those flat out hated the experience. That's reality.", "hot_take", "Interstellar")
add("I thought it was fantastic. Film is subjective.. You simply cannot TELL people they ARE wrong.", "hot_take", "Interstellar")
add("the monster plot hole of this movie is that they decide to go to Millers planet first. Millers planet has such a huge timeshift and closeness to Grgantua that it is ruled out regardless of organics etc. To spend 7 years an hour when Earth is dying is straight up crazy and no crew would have ever even bothered to investigate.", "analysis", "Interstellar")
add("This exactly, and the fact they spent over hundred earth years in space and never aged a day.", "reaction", "Interstellar")
add("They did not spend over a hundred years in space, they were just gone over a hundred years.", "analysis", "Interstellar")
add("Yep. Just one of the many absurdities. I keep watching this movie occasionally for the visual effects, and it gets more ridiculous every viewing.", "hot_take", "Interstellar")
add("The visual effects are stunning though! Too bad it's just increadibly difficult to get it right on all fronts: audio, visual, script, acting, editing, etc...", "hot_take", "Interstellar")
add("Plus the fact that a planet covered in water isn't the easiest option for colonization anyhow. If it's salt water they'd need to spend a lot of effort removing the salt. You'd need to build tons of platforms and dredge up dirt from the ocean floor.", "analysis", "Interstellar")

# ---------------- Shutter Island ----------------
add("I mean why would Dr.Cawley spent so much time, energy and manpower creating a delusional world just to cure 'only one patient' ?! Its just ridiculous. Teddy actually came into island for investigating a missing person which is of course created and planned by Dr. Cawley and his friends to trap Teddy. And hence those final words \"To live as monster or to die as good man\"..Monster meaning Chuck since he has betrayed him and joined those doctors. Open debates and arguments welcome.", "analysis", "Shutter Island")
add("Ok, I'll try to spout necessary sense to prove you're wrong: the gruesome vivid memories of _how_ he killed his wife, how could Teddy have been manipulating into producing all those details? The movie depicts the scene of him killing his wife as _his_ own memories, not someone else's story. Which corroborates his pathological behavior: fear of water, his wife \"let me go\" mantra in his hallucinations.", "analysis", "Shutter Island")
add("Doesn't it seem irresponsible for the writers to slight the power of suggestion, it being the most underrated force of manipulation in the universe? If the story plays only as you see it, I'd call this film a missed opportunity. Is this to be an empathy test?", "theory", "Shutter Island")
add("TLDR - Since this is fiction and the role play requires suspension of disbelief, why can't we suspend disbelief for the idea of false memories if they are unrealistic, too?", "theory", "Shutter Island")
add("He committed second degree murder, a crime that gets you send to prison. Why is he in a mental institute?", "theory", "Shutter Island")
add("... Ever heard of somebody murdering someone, and after evaluation a doctor concluded that the perpetrator was clinically insane?", "reaction", "Shutter Island")
add("Laeddis did nothing wrong. He belongs in a mental institution because he can't live with what he did, but he actually did nothing immoral by killing his child-murdering psychopath wife.", "hot_take", "Shutter Island")
add("Not guilty by reason of insanity.", "hot_take", "Shutter Island")
add("He remembered Tartaria and the world that was.", "reaction", "Shutter Island")

# ---------------- American Psycho ----------------
add("Quite a twist at the end LOL.", "reaction", "American Psycho")
add("No, he killed them. The director explained that the last scene wasn't meant to raise doubt about it.", "analysis", "American Psycho")
add("What happened to the bodies?", "theory", "American Psycho")
add("I think that it's just that this is a really expensive, sought after apartment, with a lovely view of Central Park. I think that the owners wanted to get someone living there as soon as possible. Instead of calling the police, the owners quietly have the mess taken care of. The agent became really suspicious of Bateman when he stopped by.", "analysis", "American Psycho")
add("I've always interpreted the ending as being intentionally ambiguous, but yes, I still thought he actually killed them and the main reason was the shady behavior of the real estate agent.", "analysis", "American Psycho")
add("I think that it's a combination of both. I know that Mary Harron has said that she didn't mean to go so far with the ending, that there was supposed to be some ambiguity, but no where near as much.", "analysis", "American Psycho")
add("So the ATM didn't actually display \"FEED ME A STRAY CAT\"?", "reaction", "American Psycho")
add("Mine asked for a dog the other day. :)", "reaction", "American Psycho")

# ---------------- Get Out ----------------
add("I don't get why the white family focused solely on blacks. It seems like they wanted the most genetically superior qualities, but those qualities don't necessarily exclusively reside with blacks. Why not seek out genetic rarities from every race?", "theory", "Get Out")
add("Yeah, I had some problems with the end of this movie too. Seems like a very flimsy way to end it. But I liked it up until then.", "hot_take", "Get Out")
add("Well the dude that was hosting grandpa looked quite big and he could run. The main character was chosen because of his eyes (talent for taking photos). Also when looking for new subjects she was looking at NCAA basketball players which often have a unique physique.", "analysis", "Get Out")
add("Good point about the eyes, I forgot about that scene with the blind photographer. But it's not like his eyes were anything special. How do you explain the housekeeper lady?", "analysis", "Get Out")
add("He kind of said that to main character that he didn't care about race but he did mention that he had a gift (with his eyes) that he himself did not possess. Throughout the movie it is implied that the white folks feel superiour to blacks in all other aspects than the physical realm.", "analysis", "Get Out")

# ---------------- Joker (2) ----------------
add("I've heard that the shooting on the subway was heavily inspired by the subway shooting from the original \"Death Wish\" movie. Here's a link to the original scene if you haven't watched it.", "theory", "Joker")
add("I felt it was a little bit, but really more based on the real life Bernie Goetz incident (which itself may have been inspired somewhat by Death Wish).", "analysis", "Joker")
add("This thing wasn't inspired by anything. Especially the Joker in the comics.", "hot_take", "Joker")

# ---------------- The Godfather (2) ----------------
add("Okay so Vito sends Luca as a spy, pretending he isn't happy with the Corleone's and would be interested in switching sides. Problem is everyone knows how loyal Luca is and whack him. But if Luca went about it in a different way would he still have been whacked, for instance he makes it clear he won't betray Vito but wants to get in the drug business as a side hustle because its easy money?", "theory", "The Godfather")
add("Pretty much. Luca was well known in the underworld. He was fiercely loyal and very dangerous. The turk's plan would always encompass getting rid of Luca, no matter if Luca tried or not to act like a spy.", "hot_take", "The Godfather")
add("This question was asked before, and BullSchmidt answered it. There is a wonderful discussion between two former chatters. It's a great read about Luca.", "reaction", "The Godfather")

# ---------------- The Sixth Sense ----------------
add("Almost everybody familiar with this movie is familiar with the twist at the end. But, the question for the movie is does Cole know? Cole seemed to be talking to him just like anybody else. I think Cole did, and in the last scene he and Malcolm are in, Cole tells Malcolm to talk to his wife when she's asleep for her to listen. That indicates that Cole knew.", "analysis", "The Sixth Sense")
add("Yes, he knew. The thing you mentioned is one of the hints. Cole also fled from Malcolm in the beginning when he went inside the church. And he described a feeling he gets when there's a dead person around, it's not just that he SEES they're dead.", "analysis", "The Sixth Sense")
add("The actual EXPLANATION of the twist is used by Night to say to the viewer 'see what happens if you don't think outside the circle'. For the real meaning which is Sertraline abuse, Cole is having hallucinations as is his mother but she is on a lesser dose.", "theory", "The Sixth Sense")
add("That poor psychic kid. Where did his dad go?", "theory", "The Sixth Sense")
add("If he was dead, but how was he hired to the boy?", "theory", "The Sixth Sense")
add("He was not hired. He was drawn to Cole because of his sixth sense and imagined him to be his patient.", "hot_take", "The Sixth Sense")
add("Do how did he not know he was a ghost?", "theory", "The Sixth Sense")
add("Like the movie said, ghosts only see what they want to see. Those ghosts walking around exist is some kind of dream state, in which they just go along with the strange things that happen and time doesn't pass normally.", "analysis", "The Sixth Sense")
add("In the same sense that you sometimes don't realize you're dreaming. You just 'accept' it as moving from scene to scene without any logical connection.", "theory", "The Sixth Sense")
add("Malcolm was part of the shrink army that get appointed to all boys that are Family Law inflicted. They then diagnose Attention Deficit stuff and feed them drugs. Malcolm did that to Vincent so in Night's rules he had to die at the hands of his victim. Night shows us M staring at a huge fake bottle of Zoloft but he is unable to use it.", "theory", "The Sixth Sense")

# ---------------- Cold-labeled batch (20 posts, labeled by the student alone, no AI) ----------------
cold_texts = [
    "I can think of at least 4 films that are more deserving of Best Picture than Forrest Gump (Pulp Fiction, Shawshank Redemption, Ed Wood, Clerks) although for arguments sake I think we can all agree that Pulp Fiction should have won instead of this stupid movie.",
    "It's 2023. About time to wake the fuck up and realize that oscars=shit. Or ANY 'award' for arts, for that matter.",
    "Oscar for Clerks? The fuck are you smoking?",
    "Clerks was great, even if you don't think it's Oscar worthy it's definitely more Oscar worthy than Forrest Gump.",
    "No. Ill take Pulp over Gump. But nobody thinks Clerks deserves an Oscar except for you and maybe Kevin Smith. But I've come to expect nothing less from you.",
    "Yes it was, Clerks is an overall solid film and the limited budget makes it even more impressive. Forrest Gump is just downright stupid and didn't cover any themes that hadn't already been covered much better by Back To The Future Part III.",
    "LOL go watch your stupid Forrest Gump movie, I bet you think it intellectually deep or something.",
    "I disagree. Forrest Gump checks a lot of boxes: 1) unique story 2) great soundtrack (both composed music and pop music) 3) use of ground breaking technology (Forrest placed with historical footage of celebrities) 4) some great cinematic shots 5) An amazing performance by Tom Hanks. Also it was a box office hit, 678.2 million USD.",
    "I know they gave him a diploma for whatever it is he went to school for which is also questionable. Haven't watched the movie in years and it just crossed my mind. Where did he go or what he was doing while in school?",
    "Hard to say. This was before college football was big money but certainly within the time frame of wealthy alums greasing the skids for a ringer. I am thinking that somehow Gump took some basic courses such as auto mechanics but somebody twisted the arms of Alabama administrators to inflate Gump's grades to maintain academic eligibility.",
    "After 5 years of playing football I got a college degree. Love that line, its so true. Gump was one fast sob so I am sure Bear Bryant had someone take his tests, so his all-american could play.",
    "I know this is an old imdb post but it reminds that in the book, Bear Bryant is his football coach when he is in college. Unlike the movie, he flunks out of college.",
    "OK, not a football or sports fan - can you explain that joke for me?",
    '"What does that mean?" (in reply to the line "Stupid is as stupid does.")',
    "That people with normal and high intelligence can do dumb things too.",
    "I guess it could also be a way of saying 'no one is perfect'.",
    "It means, 'I might be slow mentally but that doesn't mean I'm stupid.'",
    "I think it means it's OK to be stupid as long as you don't do stupid things. If you can't help being slow, it's better to not draw negative attention to it.",
    "I always thought it meant stupid is an action, not a state of being. He always responded with that statement when he was asked if he 'was stupid or something' — he was saying stupid is achieved by actions, not a way of thought.",
    "It means his mother knows he is stupid to work it out. But being stupid he thinks it's some kind of compliment.",
]
cold_labels = [
    "hot_take", "hot_take", "reaction", "hot_take", "hot_take", "analysis", "reaction",
    "analysis", "theory", "theory", "analysis", "analysis", "theory", "theory", "theory",
    "theory", "theory", "theory", "analysis", "theory",
]
for text, label in zip(cold_texts, cold_labels):
    rows.append((text, label, "cold"))

with open("labels.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label", "note"])
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to labels.csv")

from collections import Counter
counts = Counter(r[1] for r in rows)
for label, count in counts.most_common():
    print(f"  {label}: {count} ({count/len(rows)*100:.1f}%)")
