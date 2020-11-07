# TSP Spotify Playlist
Cohort 19 Capstone Project for the Graduate Certificate of Data Science at Georgetown University School of Continuing Studies.

# Members
Adam Goldstein (Project Coordinator) - https://www.linkedin.com/in/adammgoldstein1/
<br />
Patricia Merino - merinopc@gmail.com | www.linkedin.com/in/patriciamerino7 
<br />
Navneet Sandhu - nav.sandhu03@gmail.com | www.linkedin.com/in/navneetksandhu
<br />
Nicholas Merkling (Statistician) - merknc08@gmail.com | https://www.linkedin.com/in/nicholas-merkling/

# Hypothesis Statements
We believe that creating playlists driven by lyrical content can give the user a glimpse into thematic sequences that exist within their “liked” tracks.

We believe sonic variation in a playlist can be achieved by ordering the tracks according to a valence-energy curve, thus delivering a captivating listening experience.

# Abstract
Spotify offers a plethora of playlists ranging from types of moods to genres.  However, some playlists, such as “POLLEN”, declare itself as a genre-less playlist. Our playlist methodology expands on the idea of a genre-less playlist by connecting tracks through their lyrical message and themes rather than genre.  Our product is called a Thematic Sequence Playlist (TSP).  The TSP is created by collaborating with a Spotify user’s “liked tracks” to create a ten to twenty track playlist where tracks are linked through a structured lyrical theme.

POLLEN is “a playlist based around a radical premise: It was not organized by genre.” This playlist has 410,000 followers and is made up of 120 tracks. A testimony to Pollen’s listeners from Hope Tala, a producer of an artist with 450,000 monthly listeners, exclaims “We’ve been on other playlists that have higher follower numbers, but the engagement on Pollen is mad….This is not like a mid-day cafe background playlist; this is a, I-need-to-listen-to-this-today” (1).


# Limitation
Tracks are chosen by uni-gram.  Improvement would be by n-grams.

# Deliverables

1. [Presentation](https://github.com/georgetown-analytics/Spotify/blob/master/7_Reports/Spotify-TSP%20Presentation.pdf) 
2. [Final Report](https://github.com/georgetown-analytics/Spotify/blob/master/7_Reports/Spotify-TSP-FinalReport.pdf)


# Data Sources
Personal Music Collection Database - Train model to find features of “importance” to learn in order to generate TSPs.
<br />
Spotify API - Use liked tracks to make TSPs based on trained model from Personal Music Collection Database
<br />
Kaggle Data File - Train model on lyrics
