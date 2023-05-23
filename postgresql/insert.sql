insert into artists(name)
values ('The Weekend'), ('Rihanna'), ('Adele'), ('Schwefelgelb'),
('Flume'), ('IC3PEAK'), ('Кровосток'), ('Kero Kero Bonito');

insert into genres(name)
values ('Pop'), ('Rap'), ('Experimental'), ('Industrial techno'), ('Soul');

insert into artists_genres(artist_id, genre_id)
values (1, 1), (1, 5), (2, 1), (3, 1),
(4, 4), (5, 3), (6, 1), (7, 2), (8, 1), (8, 3)

insert into albums(name, release_year)
values ('Das Ende vom Kreis', 2010), ('Anti', 2016), ('21', 2011), ('Starboy', 2016),
('Arrived Anxious, Left Bored', 2013), ('Студень', 2012),
('До Свидания', 2020), ('Intro Bonito', 2014);

insert into albums(name, release_year)
values ('Aus Den Falten', 2018)

insert into albums_artists(artist_id, album_id)
values (1, 4), (2, 2), (3, 3), (4, 1),
(5, 5), (6, 7), (7, 6), (8, 8);

insert into tracks(name, duration, album_id)
values ('Id rather sleep', 115, 8), ('Sick Beat', 179, 8), ('Wie ich heis', 236, 1),
('Zu zweit', 290, 1), ('Schwarz Weis', 341, 1), ('Regen aus Rosenquarz', 258, 1),
('Ganz egal was ich mach', 261, 1), ('Starboy', 230, 4), ('Rolling in the Deep', 228, 3),
('Someone Like You', 285, 3), ('Work', 219, 2), ('No other', 287, 5),
('Думай позитивно', 221, 6), ('Душно', 209, 6), ('Весело и грустно', 194, 7);

insert into tracks(name, duration, album_id)
values ('My party', 167, 8)

insert into collections(name, release_year)
values ('Nightsleep', 2022), ('For work', 2023), ('In case of feelings', 2021),
('Ambient', 2020), ('lo-fi', 2019), ('Rap', 2018),
('Running', 2016), ('Sadface', 2017);

insert into collections_tracks(collection_id, track_id)
values (1, 1), (1, 6), (2, 7), (2, 5),
 (3, 4), (3, 10), (4, 11), (4, 1), (5, 3),
 (6, 13), (6, 14), (7, 2), (7, 3), (7, 8), (8, 9);


































